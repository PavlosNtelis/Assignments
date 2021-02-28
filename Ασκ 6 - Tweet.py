import tweepy

twitter_keys = {
        "consumer_key":        "",
        "consumer_secret":     "",
        "access_token_key":    "",
        "access_token_secret": ""
}

auth = tweepy.OAuthHandler(twitter_keys["consumer_key"], twitter_keys["consumer_secret"])
auth.set_access_token(twitter_keys["access_token_key"], twitter_keys["access_token_secret"])
api = tweepy.API(auth)

print("Enter the user's twitter handle(without @):")
userid = input()
tmp=[]
tweets = api.user_timeline(screen_name=userid, count = 10)     
csv_tweets = [tweet.text for tweet in tweets]
for i in csv_tweets:    
    tmp.append(i) 

all = tmp[9].split() #δημιουργω το array για να δουλεψει το αλλ += μετα
for i in range(9):
    all += tmp[i].split()

sorted = sorted(all, key = len)
print("The five shortest words are:")
for i in range(5):
    print(sorted[i])

print("The five longest words are:")
for i in range(1,6):
    print(sorted[-i])