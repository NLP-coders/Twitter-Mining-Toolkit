from config import Config
from tweepy import TweepError
#import mysql.connector
import argparse

#https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1

parser = argparse.ArgumentParser(description='Parse the  hydrator script')
parser.add_argument("--a")

args = parser.parse_args()
a = args.a
print(a)


#Creat mysql connection 
#db = mysql.connector.connect(host=Config.host , user = Config.user, password = Config.password)