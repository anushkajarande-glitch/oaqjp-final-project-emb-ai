from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_api():
    text_to_analyze = request.args.get("textToAnalyze")

    # 🔴 TASK 7 REQUIREMENT: blank input handling
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({
            "status_code": 400,
            "message": "Invalid input! Text cannot be empty."
        })

    result = emotion_detector(text_to_analyze)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)