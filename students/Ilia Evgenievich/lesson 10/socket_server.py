import socketio
import eventlet
#eventlet.monkey_patch()
#mgr = socketio.RedisManager('redis://socketio-redis:6379/0')
sio = socketio.Server(cors_allowed_origins='*',async_mode='eventlet')

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def test_message(sid, data):
    print('message ', data)
    sio.emit('message', {'data': 'pong'}, broadcast=True, include_self=True)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)