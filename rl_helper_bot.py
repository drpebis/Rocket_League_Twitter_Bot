#if you like this, please check this guy's git: https://github.com/ykdojo/twitterbotsample
#This is built off of his tutorial he posted on his youtube channel
import tweepy
import time
import random

print('Starting bot...', flush=True)

#You'll need a twitter dev account to generate this specific info
CONSUMER_KEY = 'YOUR KEY'
CONSUMER_SECRET = 'YOUR SECRET'
ACCESS_KEY = 'YOUR KEY'
ACCESS_SECRET = 'YOUR SECRET'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


#this function is where the action happens, it searches for a specific
#hashtag, then responds based off of a random number that corresponds
#to an index of a list for a specific response.
def reply_to_tweets():
    print('Searching for #rlhelper', flush=True)

    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#rlhelper' in mention.full_text.lower():
            print('Found #rlhelper', flush=True)
            print('Responding...', flush=True)
            value = random.randint(0,23)
            #api.update_status('@' + mention.user.screen_name +
                    #well memed!', mention.id)
            api.update_status('@' + mention.user.screen_name + ' ' +
                    list1[value], mention.id)
while True:
    reply_to_tweets()
    time.sleep(15)

    list1 = ['Don\'t worry, at least you weren\'t driving the scarab', 'All your opponents will now have camera shake turned on'
    , 'Play a game with a yellow scarab, I promise you you\'ll have a great time', 'next time play with a USB steering wheel'
    , 'May your next opponents miss their full boost...' , 'Throw on a pair of Cristianos, you\'ll feel ten times better'
    , 'You know, you\'re guaranteed to win your next match if you thown on the most rediculous topper you have', 'Perfect time to try a new car and see how it feels'
    , 'No other player in that match has a pet better than yours' , 'Make a wacky concept car! It\'s always fun to see how creative you can be'
    , 'Take a quick break, grab your favorite drink, and I bet you\'ll have a fantastic match' , 'I always play better with some of my favorite music, ever tried that?'
    , 'Go give that new decal a try!' , 'Why not thow on some new color combinations, change things up?'
    , 'Practicing in free play always helps me out' , 'I like to use free play to calm down a bit'
    , 'In these situations I like to practice dribbling in free play' , 'Try speeding around in free play at max speed, it\'s always really relaxing to me'
    , 'Yeah, but did any of the other players have such an amazing smile like you :)' , 'You\'ll win the next match, I believe in you!'
    , 'The sun is shining, the birds are chirping, we can still train!' , 'Forget that match, this next one you\'ll have will be fantastic'
    , 'Why worry about the last match when your next one is going to be awesome!' , 'Knock Knock, Who\'s there? Grand Champion. Grand Champion what season? Grand Champion Season 3...'
    , 'You never have to stop playing the Octane' , 'I bless you with full boost and a heart full of dreams']


    






