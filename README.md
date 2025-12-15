AsphaltV – AI-Powered Road Risk Intelligence System

AsphaltV is an AI-driven road condition monitoring platform that detects, verifies, and prioritizes road defects using computer vision and spatial consensus logic. Unlike traditional pothole detection systems that rely on single-user reports, AsphaltV aggregates multiple observations across vehicles to minimize false positives and provide actionable insights for municipalities.

🧩 Problem Statement

Road defects such as potholes and surface anomalies pose serious safety risks, increase vehicle maintenance costs, and often go unreported or are reported inconsistently. Existing solutions typically rely on manual reporting or isolated AI detections, resulting in unreliable data and inefficient repair prioritization.

💡 Solution Overview

AsphaltV combines AI-based visual anomaly detection with spatial consensus verification to create a reliable, scalable road risk intelligence system.
Key Innovations:

>AI-Assisted Detection: Uses YOLOv8 to analyze road images and identify potential anomalies.

>Spatial Consensus Logic: Groups nearby detections into grid cells and verifies defects only after multiple confirmations.

>False-Positive Reduction: Single reports remain “pending” until corroborated.

>Real-Time Dashboard: Visualizes verified and pending road defects on an interactive map.

>Fleet-Agnostic Design: Can ingest data from any vehicle source (delivery fleets, public transport, ride-hailing, etc.).

🛠️ System Architecture

1. Driver Input (Simulation):
Image + GPS data submitted via API

2. Backend (Flask + YOLOv8):
>Performs AI inference
>Computes confidence score
>Applies spatial grid-based consensus

3. Database (Supabase / PostgreSQL):
>Stores defect records
>Tracks confirmation counts and verification status

4. Dashboard (Leaflet.js):
>Displays defects on a map
>Highlights verified hotspots

📊 Features Implemented

>REST API for image-based road anomaly detection
>Grid-based clustering of nearby defects
>Multi-report verification logic
>Real-time database updates
>Interactive map dashboard
>GitHub-based development tracking

🧪 Demo & Screenshots

🎥 Demo Video:
(Uploaded in repository / hackathon submission)

📸 Screenshots Included:

>Backend API response after image upload
>Supabase defect table updates
>Dashboard map with verified hotspots
>GitHub commit history

⚙️ Tech Stack

>Backend: Python, Flask
>AI Model: YOLOv8 (Ultralytics)
>Database: Supabase (PostgreSQL)
>Frontend: HTML, JavaScript, Leaflet.js
>Version Control: Git & GitHub

🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/Parnika110805/AsphaltV.git
cd AsphaltV

2️⃣ Setup Virtual Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key

4️⃣ Run Backend
python app.py

5️⃣ Test API
curl -F "image=@sample.jpg" -F "lat=12.9716" -F "lon=77.5946" http://127.0.0.1:5000/predict

👥 Team Roles

Team Member 1:
- AI & Backend Development
- AI inference logic
- Spatial consensus algorithm
- Flask API development
- Database integration

Team Member 2:
- Frontend & Visualization
- Dashboard development
- Map-based visualization
- UI logic and data rendering
- Demo and documentation support

🌍 Expected Impact

>Reduces false road defect reports
>Enables data-driven repair prioritization
>Improves road safety
>Supports scalable smart city infrastructure
>Cost-effective and fleet-agnostic deployment

🚧 Limitations & Future Work

>Train a custom road defect dataset for improved accuracy
>Add mobile PWA for live driver input
>Implement role-based authentication
>Integrate predictive maintenance analytics
>Support additional defect types (cracks, faded markings)

📚 References

>Ultralytics YOLOv8: https://github.com/ultralytics/ultralytics
>Supabase Documentation: https://supabase.com/docs
>Leaflet.js Maps: https://leafletjs.com
>OpenStreetMap Data

📌 License

This project is developed for educational and hackathon purposes.
