from sys import stdout
from time import sleep

def cnt():
    for count in range(0, 10):
        print(count + 1)
        stdout.flush()
        sleep(0.5)

#websocketd unavailable in arch linux repository, use github version
# import asyncio
# import websockets
# import sys
# import time

# Host = "0.0.0.0"
# SocketPort = 8080

# async def websocketserver(websocket,path):

#     Rxdata = await websocket.recv()
#     print(f" Received data : {Rxdata}")
#     await websocket.send("200")
    

#     start_server = websockets.serve(websocketserver, Host, SocketPort)

#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()



if __name__ == "__main__":
    cnt()

