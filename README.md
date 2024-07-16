# Test of websocket connections to FastAPI server #

# files:
+ clien.py - clien based on aiohttp lib
+ main.py - primary websocket
+ intermediate.py - transition websocket
+ final.py - FastAPI server (responses with 3 text messages)
+ final_json.py - FastAPI server (responses with JSON)

# client.py 
Sends a JSON in format:
```{
    "name": "Pavel",
    "surname": "Dolgy",
    "age": 18
    }
```
After recieves back messages of any type

# main.py
Receives a JSON and sends it forward. After waites for a response message.

# intermediate.py
A transition websocket that recieves anything and sends it forward

# final.py
A FastAPI server that receives JSON file. After it handels file and sends back 3 text messages

# final_json.py 
A FastAPI echo serevr that receives a JSON file. After sends it back without any changes 

# used libs:
+ websockets - lib to create a simple websocket client/server
+ aiohttp - lib to create websocket-connections via client session
+ websocket-client - creates a simple websocket client (lib that wasn't used at final version, but might be usefull)
