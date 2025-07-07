# Import needed package
import text_analyzer # type: ignore

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets) # type: ignore

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')

