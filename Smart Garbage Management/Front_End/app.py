from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# In-memory storage (for hackathon demo)
reports = []

# ------------------ PRIORITY LOGIC ------------------
def get_priority(text):
    text = text.lower()
    if "large" in text or "overflow" in text or "dump" in text:
        return "High"
    elif "medium" in text:
        return "Medium"
    return "Low"

# ------------------ ROUTES ------------------

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Submit report
@app.route("/report", methods=["POST"])
def report():
    data = request.json

    new_report = {
        "image": data.get("image", ""),
        "location": data.get("location", ""),
        "priority": get_priority(data.get("image", "")),
        "status": "Pending",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    reports.append(new_report)

    return jsonify({
        "message": "Report submitted successfully",
        "data": new_report
    })

# Get all reports
@app.route("/reports", methods=["GET"])
def get_reports():
    return jsonify(reports)

# Update status (mark as completed)
@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    if index < 0 or index >= len(reports):
        return jsonify({"error": "Invalid report index"}), 400

    reports[index]["status"] = "Completed"
    return jsonify({
        "message": "Report updated",
        "data": reports[index]
    })

# Delete report (optional but useful)
@app.route("/delete/<int:index>", methods=["DELETE"])
def delete(index):
    if index < 0 or index >= len(reports):
        return jsonify({"error": "Invalid report index"}), 400

    deleted = reports.pop(index)
    return jsonify({
        "message": "Report deleted",
        "data": deleted
    })

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
