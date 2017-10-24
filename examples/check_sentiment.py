from client import TwitterSent
import secret_keys as sk

import sys
sys.path.insert(0, '/Users/xanthate/twittersent/twittersent')


print("Enter the list of keywords separated by commas: ")

user_input_as_string = input()
user_input_as_list = user_input_as_string.split(',') #splits the input string on commas

user_input_as_list = [a for a in user_input_as_list]

print("Enter the total number of tweets on which the analysis is to be done: ")
input_total_number_of_tweets = int(input())

T = TwitterSent()
value = TwitterSent.calculate_sentiment(T, user_input_as_list, input_total_number_of_tweets)
TwitterSent.barplot(T, value)
