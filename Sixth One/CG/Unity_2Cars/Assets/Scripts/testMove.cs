using System;
using System.Collections;
using System.Diagnostics;
using System.Threading;
using UnityEngine;
using Random = System.Random;
using Debug = UnityEngine.Debug;
using System.Collections.Specialized;

public class testMove : MonoBehaviour
{
    public Rigidbody rb;
    public Transform objectPosition;
    public float speed = -800f;
    Vector3 temp;
    public float[] leftCarX = { -3, -3, -8, -8, -3, -8, -3, -8 };
    public float[] rightCarX = { 3, 3, 8, 8, 3, 8, 3, 8 };
    Random r = new Random();
    private float level = 0.0f;
    private int log;
    // Update is called once per frame

    void Update()
    {
        level += 0.01f;
        if (level % 10 > 0 && level % 10 < 0.01)
        {
            speed -= 50.0f;
        }

        rb.velocity = new Vector3(0f, 0f, speed * Time.deltaTime);
        temp = objectPosition.position;
        if (temp.z < -30)
        {
            if (temp.x < 0)
            {
                log = r.Next(leftCarX.Length);
                temp.x = leftCarX[log];
                Debug.Log(log);
                Debug.Log(temp.x);
            }
            else if (temp.x > 0)
            {
                temp.x = rightCarX[r.Next(rightCarX.Length)];
            }
            temp.z = r.Next(100, 120);
            objectPosition.position = temp;
        }
    }
    
    
    
}
