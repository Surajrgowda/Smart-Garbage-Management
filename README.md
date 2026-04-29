<img width="1905" height="895" alt="Screenshot 2026-04-29 153926" src="https://github.com/user-attachments/assets/d2132428-66ce-4b49-9b13-f4f0bc95d011" /># Smart-Garbage-Management

The Smart Garbage Reporting System is a web-based application designed to improve waste management in urban areas. It allows users to report garbage issues by uploading images and sharing their live location.

The system provides a centralized platform where administrators can monitor complaints, track their status, and assign work to field workers. It also includes features like real-time notifications, live location tracking, and AI-based garbage classification (demo) to enhance efficiency and response time.

This solution helps bridge the gap between citizens and municipal authorities, contributing to cleaner and smarter cities.
[3:40 pm, 29/04/2026] Visnu SNPSU: ✨ Feature Scope
👤 User Features
Submit garbage reports with image
Capture live GPS location
Provide description of issue
🛠️ Admin Features
Dashboard with report statistics
View all reports with images
Update report status (Pending / In Progress / Completed)
View real-time garbage locations on map
Receive notifications for new reports
👷 Worker Features
View assigned tasks
Accept and complete jobs
Track work progress
🧠 Smart Features
AI-based garbage detection (demo)
Real-time alerts for new reports
Map-based visualization of complaints
🛠️ Tech Stack
Frontend
HTML
CSS (Tailwind CSS)
JavaScript
Backend
Python
Flask
Libraries / Tools
Leaflet.js (maps & location tracking)
Font Awesome (icons)
Storage
Local file storage (images)
In-memory data (temporary database)
mart Garbage Reporting System
📌 Overview

The Smart Garbage Reporting System is a web-based application that helps users report garbage issues in their locality using images and live location.

It provides a centralized platform for administrators to monitor complaints, track their status, and ensure timely resolution. The system improves communication between citizens and authorities, making cities cleaner and smarter.

🚀 Features
👤 User
Upload garbage images (camera or gallery)
Capture live GPS location
Submit complaints easily
🛠️ Admin
Dashboard with real-time statistics
View all reports with images
Update report status (Pending / In Progress / Completed)
View garbage locations on map
Receive real-time notifications
👷 Worker
View assigned tasks
Accept and complete jobs
Track work progress
🧠 Smart Features
AI-based garbage detection (demo)
Live map visualization
Real-time alerts for new reports
🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript, Tailwind CSS
Backend: Python (Flask)
Maps: Leaflet.js
Storage: Local storage (images + in-memory data)
📂 Project Structure
smart-garbage-reporting/
│
├── app.py
├── static/
│   └── uploads/
├── templates/
│   ├── index.html
│   ├── admin.html
│   ├── worker.html
│   ├── admin_login.html
│   └── worker_login.html
⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/smart-garbage-reporting.git
cd smart-garbage-reporting
2. Install dependencies
pip install flask
3. Create required folder
static/uploads
4. Run the project
python app.py
5. Open in browser
http://127.0.0.1:5000/
🔑 Login Credentials

Admin

Username: admin
Password: 1234

Worker

Username: worker
Password: 1234

📸 Screenshots
<img width="1912" height="909" alt="Screenshot 2026-04-29 153515" src="https://github.com/user-attachments/assets/45c1b6fc-3c78-43a2-a7f6-d8997900f4e1" />
<img width="1894" height="786" alt="Screenshot 2026-04-29 153533" src="https://github.com/user-attachments/assets/b146541a-a33f-4b20-923b-76dafb67d902" />
<img width="1893" height="857" alt="Screenshot 2026-04-29 153548" src="https://github.com/user-attachments/assets/6a2bcdd8-28ff-4ddd-beff-ca8c9cf8a57a" />
<img width="1893" height="896" alt="Screenshot 2026-04-29 153700" src="https://github.com/user-attachments/assets/8f3f4252-7e3b-46fd-b635-e18b72ecfa69" />
<img width="1905" height="895" alt="Screenshot 2026-04-29 153926" src="https://github.com/user-attachments/assets/487ad33f-aca5-4b0f-b28d-d3fffd956c1a" />







🌐 Live Demo
https://smartgarbage-reportingsystem.netlify.app/


🔮 Future Scope
Real AI/ML model for waste detection
Mobile application (Android/iOS)
Cloud database integration
Push notifications
Route optimization for garbage collection
🌍 Impact
Improves cleanliness in cities
Reduces response time for complaints
Enhances communication between citizens and authorities
Supports smart city initiatives
