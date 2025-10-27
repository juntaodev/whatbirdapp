# 🐦 WhatBirdApp

An intelligent mobile and web platform that identifies birds from recorded sounds using machine learning and signal processing.

---

## 📘 Overview

**WhatBirdApp** lets users record or upload a short bird sound and instantly identify the most likely species.  
It uses **BirdNET**, a pre-trained deep learning model from the Cornell Lab of Ornithology, integrated through a Python backend and a Flutter mobile frontend.

---

## 🚀 Current Status — Phase 0 Complete

- ✅ Local ML environment setup (BirdNET-Analyzer)
- ✅ Successful model download and test inference
- ✅ Project structure created for `backend`, `frontend`, and `ml`
- ✅ `.gitignore` configured to exclude large model data
- ✅ Ready for Phase 1: Backend & ML Integration (FastAPI + BirdNET) 

---

## 🧩 Architecture

```

Frontend (Flutter)
↓
REST API (FastAPI)
↓
ML Model Server (BirdNET)
↓
Database / Storage (PostgreSQL, MinIO, or Firebase)

```

---

## 📁 Repository Structure

```

whatbirdapp/
├── README.md
├── .gitignore
├── backend/
│   
├── frontend/
│  
├── ml/
│  
└── docs/


````

---

🧩 Next Step — Phase 1: Backend & ML Integration

In the next phase:

1.Build a FastAPI backend (/identify endpoint)

2.Connect it to ml/infer.py

3.Serve predictions as JSON

4.Add Docker and CI/CD support

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
