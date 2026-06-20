from flask import Flask, render_template, request
from ultralytics import YOLO
import easyocr
import cv2
import os

# ==========================
# Flask App
# ==========================

app = Flask(__name__)

# ==========================
# Folders
# ==========================

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "static/results"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# ==========================
# Load Models
# ==========================

model = YOLO("last.pt")

reader = easyocr.Reader(['en'])

# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")

# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded."

    file = request.files["image"]

    if file.filename == "":
        return "Please select an image."

    # Save image
    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(image_path)

    # YOLO Prediction
    results = model.predict(
        source=image_path,
        conf=0.25
    )

    plate_number = "Not Detected"
    vehicle_status = "No Plate Detected"
    confidence = 0

    image = cv2.imread(image_path)

    # Detection found
    if len(results) > 0 and len(results[0].boxes) > 0:

        # Confidence
        confidence = round(
            float(results[0].boxes[0].conf[0]) * 100,
            2
        )

        # Class
        class_id = int(
            results[0].boxes[0].cls[0]
        )

        # OCR
        ocr_results = reader.readtext(image)

        text = []

        for result in ocr_results:
            text.append(result[1])

        if len(text) > 0:
            plate_number = " ".join(text)
        else:
            plate_number = "Number Not Read"

        # Vehicle status
        if class_id == 0:
            vehicle_status = "Licensed Vehicle"
        else:
            vehicle_status = "Not Licensed Vehicle"

    else:
        plate_number = "No Plate Found"
        vehicle_status = "Not Licensed Vehicle"
        confidence = 0

    return render_template(
        "index.html",
        uploaded=True,
        plate=plate_number,
        status=vehicle_status,
        confidence=confidence
    )

# ==========================
# Run App
# ==========================

if __name__ == "__main__":
    app.run(debug=True)