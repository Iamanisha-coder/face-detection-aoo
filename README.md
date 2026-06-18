# 🤖 Real-Time Face Detection App

A lightweight, real-time face detection application built using Python, OpenCV, and Google MediaPipe. It tracks faces instantly using your device's webcam with high accuracy and minimal lag.

## 🚀 Features
* **Real-time Tracking:** Captures video directly via your webcam.
* **High Performance:** Uses MediaPipe's machine learning models for smooth processing.
* **Clean Codebase:** Structured modularly with a separate detector class and entry application.

## 📦 Repository Structure
```text
face-detection-aoo/
│
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignored files (like virtual environments)
└── src/
    ├── __init__.py          # Marks directory as a package
    ├── detector.py          # Core FaceDetector logic
    └── app.py               # Main file to run the app
