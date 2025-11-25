# Feedback Sentiment Analysis & Clustering - OLIST Brazilian e-Commerce
👉 [**Download the Power BI Report (.pbix)**](https://drive.google.com/uc?export=download&id=1lzJParmPO_Kn_BspM1aC1FAen83M2BkY)  
*A direct download link — no Google Drive preview.*

## Overview
Analysis of 42,000+ customer reviews from OLIST Brazilian e-Commerce platform to understand sentiment drivers and identify key factors affecting customer satisfaction.

## Key Findings
- **Sentiment Distribution**: 39% positive, 45% neutral, 16% negative (0.30 avg polarity)
- **Primary Pain Point**: Delivery delays dominate negative feedback
- **Satisfaction Drivers**: Fast delivery + high-quality products = strong loyalty & recommendations
- **Geographic Gaps**: São Paulo outperforms other cities; opportunity for regional standardization
  
### Sentiment Distribution
![Sentiment Distribution](images/SentimentDistribution.jpg)

## Project Structure
- Data preprocessing and translation (Portuguese → English)
- Sentiment classification using VADER
- Word frequency clustering analysis
- Power BI visualizations (word clouds, sentiment trends)

## Methodology
1. Loaded 42,000+ reviews from OLIST dataset
2. Translated reviews from Portuguese to English
3. Extracted meaningful words using Python (removed stopwords, filtered 2+ characters)
4. Classified reviews into positive (>0.5), neutral (0-0.5), negative (<0)
5. Analyzed top 100 words per sentiment category
6. Created word cloud visualizations in Power BI

## Technologies Used
- Python (data cleaning, text analysis)
- VADER (sentiment analysis)
- Power BI (visualization)
- Pandas, Re, Collections libraries

## Key Insights
**Why Customers Are Mad:** Delivery delays, missing/defective items, poor quality
![Negative Word Cloud](images/WhyAreCustomersMad.jpg)

**Why Customers Are Happy:** Fast delivery, high-quality products, excellent service
![Positive Word Cloud](images/WhyAreCustomersHappy.jpg)

## Recommendations
- Optimize delivery logistics and set SLAs
- Implement stricter quality control
- Create regional performance benchmarks
- Upgrade to BERT-based sentiment analysis for improved accuracy

## Files
- `sentiment_analysis.py` - Main analysis script
- `sentiment_words.csv` - Exported word frequencies
- `dashboard.pbix` - Power BI visualization
