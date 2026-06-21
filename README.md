# 🚗 Automatic Number Plate Recognition (ANPR)

An AI-powered Automatic Number Plate Recognition (ANPR) web application built using **YOLOv8**, **Flask**, **OpenCV**, and **EasyOCR**. The application detects vehicle license plates from uploaded images and extracts the license number using Optical Character Recognition (OCR).

---

## 📌 Features

- 🚘 Detects vehicle license plates using YOLOv8
- 🔍 Extracts license plate text using EasyOCR
- 🌐 User-friendly Flask web interface
- 📤 Upload vehicle images
- 📸 Displays uploaded image with detected plate
- ⚡ Fast and accurate detection
- 🎨 Modern responsive UI with animations

---

## 🛠️ Technologies Used

- Python
- Flask
- YOLOv8 (Ultralytics)
- OpenCV
- EasyOCR
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
ANPR/
│
├── static/
│   ├── uploads/
│   ├── css/
│   ├── js/
│
├── templates/
│   └── index.html
│
├── best.pt
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/gootyruchitha/anpr-.git
```

### 2. Move into the project folder

```bash
cd anpr-
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📸 How It Works

1. Upload a vehicle image.
2. YOLOv8 detects the license plate.
3. The detected plate is cropped.
4. EasyOCR extracts the license number.
5. The result is displayed on the webpage.

---

## 🎯 Applications

- Smart Parking Systems
- Toll Collection
- Traffic Monitoring
- Vehicle Access Control
- Security Surveillance
- Law Enforcement

---

## 🚀 Future Enhancements

- Real-time webcam detection
- Live CCTV integration
- Multiple plate detection
- Vehicle type classification
- Database integration
- Automatic logging system
- Mobile application

---

## 📷 Sample Output

(Add screenshots of your application here)

Example:

```
Original Image
↓

License Plate Detected
↓

Recognized Number:
AP39AB1234
```

---

## 👩‍💻 Author

**Ruchitha**

GitHub:
https://github.com/gootyruchitha

---

## 📄 License

This project is created for educational and learning purposes.
