
# Q_02 : Write a python program that takes a list of urls, attempts to download their content, and retries upto 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions


import requests # http requests
from time import sleep # pauses the program for short duration

def urls_download(url_list):
    result = {} # storing the result in a dictionary
    retries =  3 # retries count

# looping through each url in the provided list 
    for url in urls_list: 

        attempts = 0 # setting the initial counter for attempts 

        while attempts < retries:
                 try :  
                    response = requests.get(url) # attempt to download the content of the url 

                    if response.status_code == 200: # checking the response status code (200)
                        result[url] = response.text # storing the content in the dictionary
                        print(f"succesfully download content from {url}")
                        break
                    else:
                        #handling the unsuccesful status code
                        print(f"Failed to download  from {url} with status code {response.status_code}")
                        result[url] = f"Failed"
                        break

                 except requests.exceptions.RequestException as e:   
                    # to handle N/W related errors 
                    print(f"Failed for {url} as error : {e}")
                    attempts = attempts + 1  # prints the error message and increments the attempt

                    sleep(2) # pauses for 2 secs 

                    # when maximum attempts reach
                    if attempts == retries: 
                        result[url ] = f"Failed to retrieve the data as max retries reached {retries} with the error : {e}"
                        print(f"Giving up on {url} after max attempts")
    return result     # returns the dictionary


    #EXAMPLE 
    url_list = ["https://www.htps.com"] 
    result  = urls_download(url_list)
    print(result)
