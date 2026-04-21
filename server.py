from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector Running"

@app.route("/emotionDetector")
def detect():

    text = request.args.get("text")

    if text is None or text.strip() == "":
        return "Invalid input! Please enter text."

    return emotion_detector(text)

if __name__ == "__main__":
    app.run(debug=True)