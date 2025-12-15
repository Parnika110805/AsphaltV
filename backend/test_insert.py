from supabase import create_client

url = "https://cxkojfhujepehbdhxiqq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN4a29qZmh1amVwZWhiZGh4aXFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU3MDc5NjgsImV4cCI6MjA4MTI4Mzk2OH0.IiyiIsRXUoX2W5s7oB-p4mHR3FSoKU6GadRkgtt8cGk"

supabase = create_client(url, key)

data = {
    "defect_type": "anomaly",
    "latitude": 12.9716,
    "longitude": 77.5946,
    "confidence": 0.3,
    "source_fleet": "test_vehicle"
}

response = supabase.table("defects").insert(data).execute()
print(response)
