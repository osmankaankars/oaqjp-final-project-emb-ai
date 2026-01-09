"""Flask web server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

APP = Flask(__name__)


@APP.route("/", methods=["GET"])
def index():
    """Render the main page of the web application."""
    return render_template("index.html")


@APP.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_endpoint():
    """Analyze the given text and return a formatted emotion detection response.

    The input text is taken from:
    - GET:  query parameter 'textToAnalyze'
    - POST: form field 'textToAnalyze'

    Returns:
        str: A formatted response string, or an error message for invalid input.
    """
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:
        text_to_analyze = request.form.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


def main():
    """Start the Flask development server."""
    APP.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
