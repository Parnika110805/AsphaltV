from supabase import create_client
from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image

SUPABASE_URL = "https://cxkojfhujepehbdhxiqq.supabase.co"
SUPABASE_KEY = ""
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

model = YOLO("yolov8n.pt")

def compute_grid(lat, lon):
    return f"{round(lat, 3)}_{round(lon, 3)}"

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    img = Image.open(file)

    lat = float(request.form.get("lat", 0))
    lon = float(request.form.get("lon", 0))
    fleet = request.form.get("fleet", "demo_vehicle")

    results = model(img)
    max_confidence = 0.0

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            max_confidence = max(max_confidence, conf)

    if max_confidence == 0:
        return jsonify({"message": "No defect detected"}), 200

    grid_id = compute_grid(lat, lon)

    existing = (
        supabase.table("defects")
        .select("*")
        .eq("grid_id", grid_id)
        .execute()
    )

    if existing.data:
        record = existing.data[0]
        new_count = record["confirmation_count"] + 1
        confirmed = new_count >= 2

        supabase.table("defects").update({
            "confirmation_count": new_count,
            "is_confirmed": confirmed,
            "confidence": max(record["confidence"], max_confidence)
        }).eq("id", record["id"]).execute()

        status = "VERIFIED" if confirmed else "PENDING"

    else:
        supabase.table("defects").insert({
            "defect_type": "road_anomaly",
            "latitude": lat,
            "longitude": lon,
            "confidence": max_confidence,
            "source_fleet": fleet,
            "grid_id": grid_id,
            "confirmation_count": 1,
            "is_confirmed": False
        }).execute()

        status = "NEW"

    return jsonify({
        "grid_id": grid_id,
        "confidence": max_confidence,
        "status": status
    })

if __name__ == "__main__":
    app.run(debug=True)
