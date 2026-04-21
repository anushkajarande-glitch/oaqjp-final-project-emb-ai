from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_api():

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input! Please enter text."

    result = emotion_detector(text_to_analyze)

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)