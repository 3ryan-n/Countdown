import tweepy
 
# Fill the X's with the credentials obtained by 
# following the above mentioned procedure.
consumer_key = "v5xJUW8r0183ot6AoG278yJ6G" 
consumer_secret = "Yzc6oibCV4h8E8l8rQm41L5yaaCYPjSWnelrSfaf1gk5sEH792"
access_key = "1384162986542043138-8Q2aABCghwa1MSvtqlshoMtFrHu0QC"
access_secret = "iTtjbVVtKrR3XlbZ82fXifosPVKNSEsWiCjGBb5aP6TSc"
 
# Function to extract tweets
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # extracting 250 tweets
        number_of_tweets=250
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        temp=[] 
 
        # create an array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for t in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            temp.append(t) 
 
        # Printing the tweets
        print(temp)
 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("twitter-handle") 