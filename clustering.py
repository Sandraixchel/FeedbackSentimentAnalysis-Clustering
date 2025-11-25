import pandas as pd
import re
from collections import Counter


dataset = pd.read_csv(
    r'C:\Users\Sandra\OneDrive - Generation\PowerBI Group 1 project - Documents\Clustering\onlist_order_reviews_dataset_polarity_EN.csv',
    encoding='latin-1')

# Function to extract words
def extract_words(text):
    if pd.isna(text) or text.strip() == '':
        return []
    
    # Convert to lowercase and extract words (2+ characters)
    words = re.findall(r'\b[a-z]{2,}\b', text.lower())
    
    # Remove common stopwords
    stopwords = ['the', 'and', 'was', 'is', 'it', 'to', 'of', 'a', 'in', 
                 'for', 'not', 'on', 'with', 'as', 'at', 'by', 'an', 'be',
                 'this', 'that', 'from', 'or', 'had', 'but', 'are', 'have',
                 'has', 'were', 'been', 'their', 'said', 'they', 'would',
                 'will', 'what', 'there', 'can', 'all', 'your', 'when',
                 'which', 'she', 'her', 'him', 'his', 'could', 'our', 'my']
    
    words = [w for w in words if w not in stopwords]
    return words

positive_reviews = dataset[dataset['polarity_scores_EN'] > 0.5]['English_title_comment'].dropna()
negative_reviews = dataset[dataset['polarity_scores_EN'] < 0]['English_title_comment'].dropna()
neutral_reviews = dataset[(dataset['polarity_scores_EN'] >= 0) & 
                          (dataset['polarity_scores_EN'] <= 0.5)]['English_title_comment'].dropna()

print(f"Positive reviews (>0.5): {len(positive_reviews)}")
print(f"Neutral reviews (0 to 0.5): {len(neutral_reviews)}")
print(f"Negative reviews (<0): {len(negative_reviews)}")

# Extract all words from positive reviews
all_positive_words = []
for review in positive_reviews:
    all_positive_words.extend(extract_words(review))

# Extract all words from negative reviews
all_negative_words = []
for review in negative_reviews:
    all_negative_words.extend(extract_words(review))

# Extract all words from neutral reviews (optional)
all_neutral_words = []
for review in neutral_reviews:
    all_neutral_words.extend(extract_words(review))

# Count word frequencies
positive_word_counts = Counter(all_positive_words).most_common(100)
negative_word_counts = Counter(all_negative_words).most_common(100)
neutral_word_counts = Counter(all_neutral_words).most_common(100)

# Create dataframes
positive_words_df = pd.DataFrame(positive_word_counts, columns=['Word', 'Frequency'])
positive_words_df['Sentiment'] = 'Positive'

negative_words_df = pd.DataFrame(negative_word_counts, columns=['Word', 'Frequency'])
negative_words_df['Sentiment'] = 'Negative'

neutral_words_df = pd.DataFrame(neutral_word_counts, columns=['Word', 'Frequency'])
neutral_words_df['Sentiment'] = 'Neutral'

# Combine all three
words_df = pd.concat([positive_words_df, negative_words_df, neutral_words_df], ignore_index=True)

# Save to CSV 
words_df.to_csv(
    r'C:\Users\Sandra\OneDrive - Generation\PowerBI Group 1 project - Documents\Feedback Sentiment Analysis\sentiment_words.csv',
    index=False
)

# print("\nWord frequency data saved!")
# print("\nTop 10 Positive Words (polarity > 0.5):")
# print(positive_words_df.head(10))
# print("\nTop 10 Negative Words (polarity < 0):")
# print(negative_words_df.head(10))
# print("\nTop 10 Neutral Words (polarity 0 to 0.5):")
# print(neutral_words_df.head(10))