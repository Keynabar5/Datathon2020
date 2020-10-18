# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:22:33 2020

@author: keyna
"""

import pandas as pd


def read_data_files(file_prefix, start_file_num, end_file_num):
    '''    
    Parameters
    ----------
    file_prefix : str,
        The pre-fix of the file path. 
    start_file_num : int
        Integer specifying the beginning of desired files, or file name, to read.
    end_file_num : int
        Integer specifying the end of desired files, or file name, to read.

    Returns
    -------
    df : DataFrame
        Data frame containing combined data from specified files.
    '''
    # creates an empty data frame for files' data
    df = pd.DataFrame()  
    
    # iterates over the range of desired file's in order (start to end)
    for i in range(start_file_num, end_file_num +1):
        # string manipulation to acquuire desired file path or name
        file_name = file_prefix + str(i) + '.csv'
        # appends data from specified data file to df data frame
        df = df.append(pd.read_csv(file_name))
        sort = True
        sort = sort
 
    # drop the extra index colum
    #del df['Index']
    # drop the df index and reset the df index
    df = df.reset_index(drop=True)
    # returns final dataframe with data obtained from specified files   
    return df


data = read_data_files("C:\\Users\\keyna\\Downloads\\Data_", 0,0)
user_input = input("Please enter city: " )


for i in range(len(data)):
    if user_input == data['city'][i]:
        print(data.iloc[i])
        
        
p
    
       






