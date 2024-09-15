""" Module providing flask for emotion detection. """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emo_detector")
def emo_detector():
    """
    Detect the dominant emotion from the provided text.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    dominant_emotion, emotion_result = emotion_detector(text_to_analyse)

    anger_score = emotion_result['anger']
    disgust_score = emotion_result['disgust']
    fear_score = emotion_result['fear']
    joy_score = emotion_result['joy']
    sadness_score = emotion_result['sadness']
    anger_score = emotion_result['disgust']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page for the emotion detection app.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
