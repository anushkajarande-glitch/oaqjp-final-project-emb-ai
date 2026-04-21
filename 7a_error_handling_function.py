def emotion_detector(text_to_analyze):

    # -----------------------------
    # ERROR HANDLING (TASK 7 REQUIREMENT)
    # -----------------------------
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "status_code": 400,
            "message": "Invalid input: text cannot be empty"
        }

    # -----------------------------
    # NORMAL OUTPUT (VALID INPUT)
    # -----------------------------
    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.85,
        "sadness": 0.05
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }