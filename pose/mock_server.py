import zmq
import flatbuffers
import numpy as np

from .rep import Reply
from .req import Request

context = zmq.Context()
socket = context.socket(zmq.REP)
addr = "tcp://127.0.0.1:5555"
socket.bind(addr)

try:
    while True:
        # msg = socket.recv()
        # req = Request.Request.GetRootAs(bytearray(msg), 0)
        # print(req.Code())
        
        # pose = np.random.randn(6)
        
        # builder = flatbuffers.Builder(1024)
        # pose = builder.CreateNumpyVector(pose)
        # Reply.Start(builder)
        # Reply.AddPose(builder, pose)
        # rep = Reply.End(builder)
        # builder.Finish(rep)
        # buf: bytearray = builder.Output()
        # socket.send(buf)
        
        msg = socket.recv()
        print(msg)
        socket.send(b'I am a message from the server')
              
except Exception as e:
    raise e

finally:
    socket.close()
        