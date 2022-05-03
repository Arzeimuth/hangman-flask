from aiohttp import web
import socketio
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()



# ## creates a new Async Socket IO Server
# sio = socketio.AsyncServer()
# ## Creates a new Aiohttp Web Application
# app = web.Application()
# # Binds our Socket.IO server to our Web App
# ## instance
# sio.attach(app)

# ## we can define aiohttp endpoints just as we normally
# ## would with no change
# async def index(request):
#     with open('index.html') as f:
#         with open('gamefile.json') as game:

#             return web.Response(text=f.read(), content_type='text/html')


# ## If we wanted to create a new websocket endpoint,
# ## use this decorator, passing in the name of the
# ## event we wish to listen out for
# @sio.on('message')
# async def print_message(sid, message):
#     print("Socket ID: " , sid)
#     print(message)
#     ## await a successful emit of our reversed message
#     ## back to the client
#     await sio.emit('message', message)

# ## We bind our aiohttp endpoint to our app
# ## router
# app.router.add_get('/', index)

# ## We kick off our server
# if __name__ == '__main__':
#     web.run_app(app)
