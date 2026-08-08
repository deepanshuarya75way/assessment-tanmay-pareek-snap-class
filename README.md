# Snap_Class – AI-Powered Smart Attendance System

Snap_Class is an AI-powered classroom attendance system that automates student identification and attendance using **face recognition and voice recognition**. It provides separate workflows for teachers and students, supports QR-code based enrollment, and uses Supabase for authentication, student data, embeddings, and attendance management.

The application is built with **Python and Streamlit** and combines computer vision, machine learning, audio processing, and cloud database technologies into a single classroom attendance platform.

## 🚀 Features

* 🤖 **Face Recognition Attendance** – Identifies students using facial embeddings and machine learning.
* 🎙️ **Voice Recognition** – Supports student identification using voice embeddings.
* 👨‍🏫 **Teacher Dashboard** – Provides teacher-specific classroom and attendance workflows.
* 👨‍🎓 **Student Dashboard** – Provides student-specific enrollment and attendance functionality.
* 📱 **QR-Code Enrollment** – Allows students to join/enroll in a classroom using a QR code.
* 🔐 **Authentication** – Secure user authentication with password hashing.
* ☁️ **Supabase Integration** – Stores student information, embeddings, authentication data, and attendance records.
* ⚡ **Streamlit Interface** – Provides an interactive web-based application.
* 🔄 **Automated Attendance** – Reduces manual attendance work by automatically identifying students.

## 🧠 AI & ML Pipeline

### Face Recognition

Snap_Class uses a face-recognition pipeline to identify registered students.

The pipeline:

1. Captures the student's face.
2. Detects and processes the face image.
3. Generates a **128-dimensional facial embedding**.
4. Uses a **Linear SVM classifier** to identify the student.
5. Records the student's attendance after successful identification.

### Voice Recognition

The project also includes a voice-based identification pipeline.

The pipeline:

1. Captures or loads the student's voice.
2. Preprocesses the audio using **Librosa**.
3. Generates speaker embeddings using **Resemblyzer**.
4. Compares the voice representation with registered student embeddings.
5. Identifies the corresponding student.

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │    Web Interface     │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
          ┌──────▼──────┐             ┌──────▼──────┐
          │   Teacher   │             │   Student   │
          │   Workflow  │             │   Workflow  │
          └──────┬──────┘             └──────┬──────┘
                 │                           │
                 └─────────────┬─────────────┘
                               │
                  ┌────────────▼────────────┐
                  │      AI Pipelines       │
                  ├─────────────────────────┤
                  │ Face Recognition        │
                  │ Voice Recognition       │
                  └────────────┬────────────┘
                               │
                    ┌──────────▼──────────┐
                    │      Supabase       │
                    │ Database & Auth     │
                    └─────────────────────┘
```

## 🛠️ Tech Stack

### Programming & Application

* Python
* Streamlit
* NumPy
* Pandas

### Machine Learning & Computer Vision

* Scikit-learn
* Linear SVM
* Dlib
* Face Recognition
* Pillow

### Audio Processing

* Librosa
* Resemblyzer

### Database & Security

* Supabase
* Bcrypt

### Utilities

* Segno
* QR Code

## 📁 Project Structure

```text
snap-class/
│
├── .streamlit/
│   └── secrets.toml
│
├── src/
│   ├── components/
│   ├── pipelines/
│   ├── screen/
│   └── ...
│
├── app.py
├── APP1.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Tanmaypareek11/snap-class.git
cd snap-class
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Configuration

Snap_Class uses Supabase for backend services.

Create:

```text
.streamlit/secrets.toml
```

and configure your Supabase credentials:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

> **Important:** Never commit real Supabase credentials or other secrets to GitHub.

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will start locally and provide the Streamlit interface in your browser.

## 🔄 Application Workflow

### Teacher

```text
Teacher Login
     ↓
Create / Manage Classroom
     ↓
Generate Join Code / QR Code
     ↓
Students Enroll
     ↓
Attendance Identification
     ↓
Attendance Records
```

### Student

```text
Student Login
     ↓
Join Classroom
     ↓
QR-Code / Join Code
     ↓
Face / Voice Enrollment
     ↓
AI Identification
     ↓
Attendance Recorded
```

## 🎯 Use Cases

Snap_Class can be used for:

* College and university classrooms
* School attendance systems
* Training institutes
* Coaching centers
* Automated classroom management
* AI-based identity verification experiments

## 🔒 Security Considerations

The application uses authentication and password hashing for user management. Supabase is used for storing application data and authentication-related information.

For production deployment:

* Keep API keys and credentials in environment variables or secret managers.
* Never commit `.streamlit/secrets.toml` containing real credentials.
* Apply appropriate access controls to stored biometric embeddings.
* Obtain user consent before collecting or processing biometric data.
* Follow applicable privacy and data-protection requirements.

## 🚀 Future Improvements

* Improve recognition accuracy under different lighting conditions.
* Add liveness detection to reduce spoofing attacks.
* Add real-time camera-based attendance.
* Improve voice recognition in noisy environments.
* Add attendance analytics and visualization.
* Add CSV/PDF attendance report generation.
* Add support for larger classrooms and multiple sessions.
* Deploy the application with production-grade infrastructure.

## 👨‍💻 Author

**Tanmay Pareek**

GitHub: [Tanmaypareek11](https://github.com/Tanmaypareek11)

Project: [Snap_Class](https://github.com/Tanmaypareek11/snap-class)

---

⭐ If you find this project useful, consider giving the repository a star!
