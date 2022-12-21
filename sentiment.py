import requests
import json

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# VADER = Valence Aware Dictionary for Sentiment Reasoning

analyzer = SentimentIntensityAnalyzer()

# Fetching news from newsapi using my api key
r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=daf58c9e5adb4e259f2bbee82fde445c")

# print(r.content)
data = json.loads(r.content)
# print(data)
# print(data["articles"][0]["title"])

negative = []
neutral = []
positive = []

# Calculating the Sentiment Scores
for i in range(len(data["articles"])):

    title = data['articles'][i]['title']
    description = data['articles'][i]['description']

    if(title == None or description == None):
        continue
    
    title_analyzed = analyzer.polarity_scores(title)
    description_analyzed = analyzer.polarity_scores(description)
    
    negative.append(((title_analyzed["neg"]) + (description_analyzed["neg"])) / 2)
    neutral.append(((title_analyzed["neu"]) + (description_analyzed["neu"])) / 2)
    positive.append(((title_analyzed["pos"]) + (description_analyzed["pos"])) / 2)


# Printing
for i in range(len(negative)):
    
    title = data['articles'][i]['title']

    print("News",i + 1,":")
    print("Topic :",title)
    print("Negative Score :",negative[i])
    print("Neutral Score :",neutral[i])
    print("Positive Score :",positive[i])
    print("\n\n")
