<p align='center'>
     <img height="100" src="image.png" </img> 
     
</p>

# Interview Assessment
<br>

### Author:  Guillermo Escobar

- Date: `September 2023`
- Python 3.11.5
- script name: mixPiano.py 
- input: fileA.csv, fileB.csv, Piano API data 
- output: mergedFile_PY.csv 
- modules: requests, csv

### Purpose:

This script merges two CSV files into a new CSV file.
The client has provided 2 csv files with user data that they would like to import to the system. However some user IDs are incorrect because these users already exist in the system under different user_id values. Generate a merged file in the format: user_id,email,first_name,last_name
But make sure that for the incorrect records, user_id is taken from the system, rather than from the list provided from the client.

### Run:
```
python /file path/mixPiano.py
```