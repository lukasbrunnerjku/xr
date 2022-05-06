import zmq
import flatbuffers
import numpy as np

from .rep import Reply
from .req import Request

context = zmq.Context()
socket = context.socket(zmq.REQ)
addr = "tcp://localhost:5555"
socket.connect(addr)

try:
    for i in range(3):
        code = i
        
        builder = flatbuffers.Builder(1024)
        Request.Start(builder)
        Request.AddCode(builder, code)
        req = Request.End(builder)
        builder.Finish(req)
        buf: bytearray = builder.Output()
        socket.send(buf)
        
        msg = socket.recv()
        rep = Reply.Reply.GetRootAs(bytearray(msg), 0)
        pose = rep.PoseAsNumpy()
        print(pose)
              
except Exception as e:
    raise e

finally:
    socket.close()
        