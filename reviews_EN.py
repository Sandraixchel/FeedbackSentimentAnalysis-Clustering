import pandas as pd
import numpy as np
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

dataset = pd.read_csv(r'C:\Users\Sandra\OneDrive - Generation\PowerBI Group 1 project - Documents\Feedback Sentiment Analysis\olist_order_reviews_dataset_translated.csv',encoding="latin1")

sia=SentimentIntensityAnalyzer()

dataset['polarity_scores_EN'] =dataset['English_title_comment'].apply(lambda x: sia.polarity_scores(x)['compound'])

print(dataset)