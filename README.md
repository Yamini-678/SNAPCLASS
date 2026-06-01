# 🎓 Smart Attendance Management System

An AI-powered attendance management system that uses facial recognition, voice verification, and QR code technology to automate student attendance tracking securely and efficiently.

---

## 📖 Overview

The Smart Attendance Management System is an intelligent solution designed to streamline attendance tracking in educational institutions and organizations. The system leverages Artificial Intelligence, Computer Vision, and Voice Biometrics to authenticate users and record attendance accurately.

By combining facial recognition, voice verification, QR code generation, and cloud database integration, the platform minimizes manual effort, reduces proxy attendance, and improves attendance management efficiency.

---

## ✨ Features

* 👤 Face Recognition-based Authentication
* 🎙️ Voice Verification
* 📱 QR Code Generation and Validation
* 📊 Attendance Tracking Dashboard
* 🔐 Secure User Authentication
* ☁️ Supabase Cloud Database Integration
* 📈 Attendance Analytics
* 🌐 Interactive Streamlit Interface
* 📝 Student and Faculty Management

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & Machine Learning

* Face Recognition
* Dlib
* Resemblyzer
* Scikit-Learn

### Data Processing

* NumPy
* Pandas

### Database

* Supabase

### Security

* Bcrypt

### Additional Libraries

* QR Code Generation (Segno)
* Pillow (Image Processing)
* Librosa (Audio Processing)

---

## 📂 Project Structure

```text
Attendance_System/
│
├── components/
│   ├── reusable UI components
│
├── database/
│   ├── database operations
│
├── pipelines/
│   ├── face and voice processing pipelines
│
├── screens/
│   ├── application pages
│
├── ui/
│   ├── interface design
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd Attendance_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🔄 Workflow

1. User Registration

   * Capture facial image
   * Record voice sample
   * Store biometric embeddings securely

2. Authentication

   * Face Recognition
   * Voice Verification
   * Identity Validation

3. Attendance Marking

   * QR Code Scanning
   * Biometric Verification
   * Attendance Recording

4. Dashboard

   * View attendance records
   * Generate reports
   * Analyze attendance statistics

---

## 📸 Screenshots

### Login Screen

![Login](images/login.png)

### Attendance Dashboard

![Dashboard](images/dashboard.png)

---

## 🧠 Key Concepts Used

* Computer Vision
* Face Recognition
* Voice Biometrics
* Machine Learning
* Cloud Database Integration
* QR Code Authentication
* Data Analytics
* User Authentication & Security

---

## 🎯 Applications

* Educational Institutions
* Colleges and Universities
* Corporate Attendance Systems
* Employee Monitoring
* Training Centers
* Smart Classroom Solutions

---

## 📈 Future Enhancements

* Mobile Application
* Multi-Factor Authentication
* Real-Time Notifications
* Attendance Prediction Analytics
* Student Performance Integration
* Cloud Deployment
* Admin Reporting Dashboard

---

## 👩‍💻 Author

### Yamini

Computer Engineering Student | AI & Machine Learning Enthusiast

GitHub: https://github.com/Yamini-678

---

## ⭐ Support

If you found this project useful:

* Star the repository ⭐
* Fork the repository 🍴
* Share feedback 💡

---
