from supabase import create_client

url = ""
key = ""
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
