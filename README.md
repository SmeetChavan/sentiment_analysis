# Sentiment analysis of news articles using VaderSentiment
Task for joining the Data Scientist Internship with Indegenous

Requirements :
1) Install vaderSentiment , command : pip install vaderSentiment
2) Install requests , command : pip install requests
3) (Optional) Install json , command : pip install json  (Usually Pre-installed with Python)

Fetching latest news from newsapi using my API KEY. Converting it to json format and calculating the Polarity scores of its title and description.
The average of these scores are our final scores.

Here I'm using a Built-in library of Python 'vaderSentiment' (VADER = Valence Aware Dictionary for Sentiment Reasoning)
which can calculate the negative, neutral and positive scores for a given text.

I have printed the Negative, Neutral and Positive scores with each news, but we can also guess the exact sentiment(negative or neutral or positive) using some if else conditions. For example, if(negative[i] > positive[i]): print("Negative").
