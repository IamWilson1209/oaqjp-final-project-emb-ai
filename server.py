from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotionDetector():

    text_to_analyse = request.args.get('textToAnalyze')
    
    dominant_emotion, emotion_result = emotion_detector(text_to_analyse)
    
    print("dominant_emotion: ", dominant_emotion, "emotion_result: ", emotion_result)

    anger_score = emotion_result['anger']
    disgust_score = emotion_result['disgust']
    fear_score = emotion_result['fear']
    joy_score = emotion_result['joy']
    sadness_score = emotion_result['sadness']
    anger_score = emotion_result['disgust']

    if dominant_emotion is None:
        return "Invalid input! Try again!!"
    else:
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, response)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
