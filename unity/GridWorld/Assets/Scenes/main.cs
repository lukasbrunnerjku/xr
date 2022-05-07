using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using NetMQ;
using NetMQ.Sockets;

public class main : MonoBehaviour
{
    public float speed;
    public RequestSocket socket;

    // Start is called before the first frame update
    void Start()
    {
        speed = 10f;
        AsyncIO.ForceDotNet.Force();
        socket = new RequestSocket();
        socket.Connect("tcp://localhost:5555");
    }

    // Update is called once per frame
    void Update()
    {    
        socket.SendFrame("I am a message from the client");
        string msg = socket.ReceiveFrameString();
        print(msg);
        
        float x = Input.GetAxis("Horizontal") * Time.deltaTime * speed;
        float z = Input.GetAxis("Vertical") * Time.deltaTime * speed;
        transform.Translate(x, 0, z);
    }
}
