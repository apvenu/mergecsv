#import modules
import os
import glob
import pandas as pd
#list all csv files only

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
print("Current working directory: {0}".format(os.getcwd()))
# Change the current working directory
os.chdir('mbb/')
csv_files = glob.glob('*.{}'.format('csv'))
csv_files

df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
df_concat
df_concat.to_csv('C:/Users/mbb/Combined_files.csv')