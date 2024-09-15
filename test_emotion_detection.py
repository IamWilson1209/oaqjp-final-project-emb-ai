from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        # Test case for joy sentiment
        result_1, emotion_result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1, 'joy')
        
        # Test case for anger sentiment
        result_2, emotion_result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2, 'anger')
        
        # Test case for disgust sentiment
        result_3, emotion_result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3, 'disgust')

        # Test case for sadness sentiment
        result_4, emotion_result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4, 'sadness')

        # Test case for fear sentiment
        result_5, emotion_result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5, 'fear')
        
unittest.main()