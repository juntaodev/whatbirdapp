# 🐦 WhatBirdApp

An intelligent mobile and web platform that identifies birds from recorded sounds using machine learning and signal processing.

---

## 📘 Overview

**WhatBirdApp** enables users to record or upload a short bird sound clip, and the system identifies the most likely bird species.  
The app combines audio feature extraction (Mel spectrograms), a trained bird song classifier (BirdNET / custom CNN), and a simple, user-friendly mobile interface.

---

## 🚀 Features

- 🎤 Record or upload bird sounds directly from the app  
- 🧠 Identify bird species using pre-trained ML models  
- 🌍 Offline or online inference support  
- 📊 Display confidence scores and additional info (habitat, song pattern, map)  
- 🧩 Modular architecture (frontend + backend + ML)  

---

## 🧩 Architecture

```

Frontend (Flutter)
↓
REST API (FastAPI)
↓
ML Model Server (BirdNET or Custom CNN)
↓
Database / Storage (PostgreSQL, MinIO, or Firebase)

```

---

## 📁 Repository Structure

```

whatbirdapp/
├── README.md
├── .gitignore
├── requirements.txt
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── models/
├── frontend/
│   ├── lib/
│   ├── assets/
│   └── test/
├── ml/
│   ├── models/
│   ├── training/
│   └── utils/
└── docs/
├── roadmap.md
└── architecture-diagram.png

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/juntaoliudev/whatbirdapp.git
cd whatbirdapp
````

### 2️⃣ Set Up Python Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3️⃣ Set Up Flutter Frontend

```bash
cd frontend
flutter pub get
flutter run
```

---

## 🧠 Model Integration

The system supports either:

* **BirdNET Model** (pre-trained) — for baseline performance
* **Custom CNN Model** — trained using spectrograms from open datasets

Model files go under `ml/models/` and are auto-loaded at backend startup.

---

## 🧪 Development Workflow

| Branch      | Purpose                      |
| ----------- | ---------------------------- |
| `main`      | Stable production-ready code |
| `dev`       | Active development           |
| `feature/*` | Feature branches             |

```bash
git checkout -b feature/audio-upload
git add .
git commit -m "feat: add audio upload endpoint"
git push origin feature/audio-upload
```

---

## ✅ Phase 0 Deliverables

* Git repo initialized and connected to GitHub
* Backend and frontend skeletons created
* Initial `README.md` and `.gitignore` added
* Basic CI checks (optional GitHub Actions) configured

---

## 📜 License

MIT License © 2025 Juntao Liu

---

## 👥 Contributors

* **Juntao Liu** — Lead Developer
* [Optional teammates or collaborators]

---

## 📚 Resources

* [BirdNET Research Paper (Cornell Lab of Ornithology)](https://birdnet.cornell.edu/)
* [TensorFlow Audio Classification Tutorial](https://www.tensorflow.org/tutorials/audio/simple_audio)
* [Flutter + FastAPI Integration Guide](https://fastapi.tiangolo.com/tutorial/)

```
