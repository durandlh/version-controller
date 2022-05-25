import json 

with open('hello.json') as json_file:
    data = json.load(json_file)
    print (data['setup'])
    if data['setup'] == "https://github.com":
        print ("url is good")
    
    if data['version'] == '1':
        print("Version is 1")
