using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using NetMQ;
using NetMQ.Sockets;
using FlatBuffers;
using rep;
using req;

public class main : MonoBehaviour
{
    public float speed;
    public RequestSocket socket;

    // Start is called before the first frame update
    void Start()
    {
        speed = 10f;
        // AsyncIO.ForceDotNet.Force();
        socket = new RequestSocket();
        socket.Connect("tcp://localhost:5555");
    }

    // Update is called once per frame
    void Update()
    {    
        // socket.SendFrame("I am a message from the client");
        // string msg = socket.ReceiveFrameString();
        // print(msg);

        int code = 1;

        FlatBufferBuilder builder = new FlatBufferBuilder(1);
        Request.StartRequest(builder);
        Request.AddCode(builder, code);
        var offset = Request.EndRequest(builder);
        Request.FinishRequestBuffer(builder, offset);
        ByteBuffer bb = builder.DataBuffer;
        byte[] msg = bb.ToArray(0, bb.Length);
        socket.SendFrame(msg, msg.Length);

        msg = socket.ReceiveFrameBytes();
        bb = new ByteBuffer(msg);
        Reply rep = Reply.GetRootAsReply(bb);
        float[] pose = rep.GetPoseArray();
        print(string.Join(", ", pose));

        float x = Input.GetAxis("Horizontal") * Time.deltaTime * speed;
        float z = Input.GetAxis("Vertical") * Time.deltaTime * speed;
        transform.Translate(x, 0, z);
    }
}
