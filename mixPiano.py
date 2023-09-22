#####################################################################################################################
#  Author:  Guillermo Escobar <
#  Date:    2023-09-20
#  Purpose: This script merges two CSV files into a new CSV file 
#####################################################################################################################

import requests
import csv
# API parameters
aid = "o1sRRZSLlw"
api_token = "xeYjNEhmutkgkqCZyhBn6DErVntAKDx30FqFOS6D"
# looking for the list of users in piano
userList = requests.get("https://sandbox.piano.io/api/v3/publisher/user/list?aid="+aid+"&api_token="+api_token)
response = userList.json()
# read fileA.csv
# File A: user_id,email

def getUserID_Piano(email):
    for user in response["users"]:
        if user["email"] == email:
            return user["uid"]
    return None

with open('fileA.csv', 'r') as archivo_csv:
    # create a CSV reader object
    lectorA_csv = csv.reader(archivo_csv)
    # iterate through the rows in the CSV file and append them to a list.
    listFileA = []
    for filaA in lectorA_csv:
        listFileA.append(filaA)
    listFileA = listFileA[1:]

# read fileB.csv
# File B: user_id,first_name,last_name
with open('fileB.csv', 'r') as archivo_csv:
    # create a CSV reader object
    lectorB_csv = csv.reader(archivo_csv)
    # iterate through the rows in the CSV file
    listFileB = []
    for filaB in lectorB_csv:
        listFileB.append(filaB)

    listFileB = listFileB[1:]

# prepare the output file
    fieldnames = ['user_id', 'email','first_name', 'last_name']

    with open("mergedFile_PY.csv", 'w', newline = "") as csvfile:
        out = csv.writer(csvfile)
        # out.writeheader()
        out.writerow(fieldnames)
        user = {}
        for elementA in listFileA:
            UserIdPiano = getUserID_Piano(elementA[1]) 
            if UserIdPiano is not None:
               user['user_id'] = UserIdPiano
            else:
                user['user_id'] = elementA[0]

            user['email'] = elementA[1]
            for elementB in listFileB:
                if elementA[0] == elementB[0]:
                    user['first_name'] = elementB[1]
                    user['last_name'] = elementB[2]
            out.writerow(user.values())
        print("")
        print("*************************************************")
        print("*   END OF RUN: output ---> mergedFile_PY.csv   *")
        print("*************************************************")
        print("")