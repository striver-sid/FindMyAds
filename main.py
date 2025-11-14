from typing import Union
from fastapi import FastAPI,WebSocket
app=FastAPI()

@app.get("/")
def printsomething():
    print("Server is on")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept() # Accept client connection
    while True:
        data = await websocket.receive_text() # Receive message
        print("Client says:", data)
        await websocket.send_text(f"You wrote: {data}") # Send response