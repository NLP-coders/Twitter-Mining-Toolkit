from config import Config
from tweepy import TweepError
import os
import argparse
import numpy as np
from glob import glob
from auth import TwitterAuthKeys as auth 
import tweepy
from util import TweepyHeplers as helpers
import json
from twarc import Twarc

#setup the parser 
parser = argparse.ArgumentParser(description='Parse the  hydrator script')
parser.add_argument("--i", required=True, type=str, help="This is the input direct") #Required
parser.add_argument("--o", type=str,  default="output/" , help="This is the 'out' variable")

#Get the input/output dir 
args = parser.parse_args()
input_dir = args.i
output_dir = args.o

if not os.path.isdir(input_dir):
    print("The given dir  does not exist")
    exit()
if not os.path.isdir(output_dir):
    print("The given out dir does not exist")
    exit()

#Check if we have already retrived some IDs
input_files_paths = np.array(glob(r"{}\*".format(input_dir)))
retrived_ids_file_paths = np.array(glob("{}\*".format(output_dir)))
retrived_ids_file_paths = [os.path.basename(path).split(".")[0] for path in retrived_ids_file_paths]
print("The total number of already retrived ID files= {}".format(len(retrived_ids_file_paths)))

#Information for Twitter API access
consumer_key = auth.consumer_key
consumer_secret = auth.consumer_secret
access_token = auth.access_token
access_token_secret = auth.access_token_secret

twarc_ob = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

for path in input_files_paths:
    
    #prepare the output path
    file_name = os.path.basename(path).split(".")[0]
    
    if file_name in retrived_ids_file_paths:
        print("The file: {} has been already Processed".format(path))
        continue
    
    print("Openeing {} file".format(path))
    #initiat lists/counters
    ids = []
    hydrated_tweets=[]
    count = len(hydrated_tweets) #set up counter
    end_index =len(ids) 
    
    #set the output
    output_path = r"{}\{}.json".format( output_dir, file_name)
    
    with open(path, "r") as ids_file: #open the input file
        ids = ids_file.read().split() #read and store the ids  
        
    print("Total Tweets IDs: {} ".format(len(ids)))

    list_ = twarc_ob.hydrate(iter(ids))
    for tweet in list_:
        hydrated_tweets.append(tweet)  #appent tweet json into a list 
        
    print("Total of {} tweets downloaded, saving as json".format(len(hydrated_tweets)))
    print(hydrated_tweets)


    with open(output_path, 'w', encoding='utf8') as outfile: #open json file
        json.dump(hydrated_tweets, outfile, ensure_ascii=False) # write the data into json file



