#! Question 1 – Web Interaction & REST API Consumption

#& Working with Web & APIs, Automation/Web interaction, requests library, Basics of REST API

'''
Write a Python program that:			
			
1. Uses the requests library to send a GET request to a public REST API (e.g., users or posts API)			
			
2. Sends custom headers with the request			
			
3. Parses the JSON response and extracts specific fields			
			
4. Serializes the extracted data and saves it into a JSON file			
			
5. Handles HTTP errors using proper exception handling.			
'''

import requests

import json

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-App"
}

try:
    response=requests.get(url,headers=headers)
    
    response.raise_for_status()

    users=response.json()

    extracted_data=[]
    
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        })
        
    with open("Assignment/DAY8/users_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)   
        
    print("data saved successfully")

except requests.exceptions.HTTPError as e:
    print("HTTP Error :",e) 

except requests.exceptions.RequestException as e:
    print("HTTP Error : ",e)
    


