function isNearby(a, b) {
    const dx = a.latitude - b.latitude;
    const dy = a.longitude - b.longitude;
    return Math.sqrt(dx * dx + dy * dy) < 0.0005;
  }

  const map = L.map('map').setView([12.9716, 77.5946], 12);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
  }).addTo(map);

  fetch("https://cxkojfhujepehbdhxiqq.supabase.co/rest/v1/defects?select=*", {
    headers: {
      "apikey": "",
      "Authorization": "Bearer "
    }
  })
  .then(res => res.json())
  .then(data => {
    const groups = [];

    data.forEach(d => {
        if (!d.latitude || !d.longitude) return;

        let foundGroup = null;

        for (const g of groups) {
            if (isNearby(g, d)) {
            foundGroup = g;
            break;
            }
        }

        if (foundGroup) {
            foundGroup.count += 1;

            foundGroup.max_confidence = Math.max(
            foundGroup.max_confidence,
            Number(d.confidence)
            );

            foundGroup.risk_score = Math.max(
            foundGroup.risk_score,
            Number(d.risk_score || d.confidence)
            );
        } else {
            groups.push({
            latitude: Number(d.latitude),
            longitude: Number(d.longitude),
            count: 1,
            max_confidence: Number(d.confidence),
            risk_score: Number(d.risk_score || d.confidence)
            });
        }
    });

    groups.forEach(g => {
        let color = "orange";

        if (g.risk_score >= 0.7) color = "red";
        if (g.risk_score >= 1.1) color = "darkred";

        L.circleMarker([g.latitude, g.longitude], {
            radius: 8 + g.count * 2,
            color: color,
            fillColor: color,
            weight: color !== "orange" ? 3 : 1,
            fillOpacity: 0.9
        })
        .addTo(map)
        .bindPopup(`
            <b>Road Defect</b><br>
            <b>Reports:</b> ${g.count}<br>
            <b>Max Confidence:</b> ${g.max_confidence.toFixed(2)}<br>
            <b>Risk Score:</b> ${g.risk_score.toFixed(2)}<br>
            <b>Status:</b> ${
            color === "darkred"
                ? "CRITICAL"
                : color === "red"
                ? "VERIFIED"
                : "PENDING"
            }
        `);
    });
});
