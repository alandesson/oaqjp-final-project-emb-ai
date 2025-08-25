"""Modulo responsavel por levantar aplicação flask e seus endpoints"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask class.
app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Renderiza pagina html na raiz da url
    """
    return render_template('index.html')

# Defining route


@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint para analise de sentimentos
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if not response['dominant_emotion']:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is 'anger': {response['anger']},"
        f"'disgust': {response['disgust']}, 'fear': {response['fear']},"
        f" 'joy': {response['joy']} and 'sadness': {response['sadness']}."
        f"The dominant emotion is {response['dominant_emotion']}")


if __name__ == "__main__":
    # app.run() starts the Flask development server.
    app.run(host="0.0.0.0", port=5000)
