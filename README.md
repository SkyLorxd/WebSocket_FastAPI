A combination of three serveres

First FastAPI server receives JSON and send it to intermediate websocket server
Intermediate websocket serversends it to final websocket server 
Final websocket server is processing and returns three messages, which after go back final->intermediate->start(FastAPI)
Finally, three messages generated by final websocket server get back to client
