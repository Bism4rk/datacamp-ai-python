# Import needed package
import text_analyzer # type: ignore

datacamp_tweets = [
    "I love learning Python!",
    "Python is great for data science.",
    "DataCamp offers fantastic Python courses.",
    "I enjoy coding in Python every day.",
    "#Python is my favorite programming language.",
]

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)
