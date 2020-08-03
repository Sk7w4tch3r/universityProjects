using System;
using System.Collections;
using System.Diagnostics;
using System.Threading;
using UnityEngine;
using Random = UnityEngine.Random;
using Debug = UnityEngine.Debug;
using System.Collections.Specialized;

public class MoveBlockRight : MonoBehaviour
{
    public AudioSource crash;
    public Rigidbody rb;
    public Transform objectPosition;
    public float speed = -800f;
    public Vector3 temp1;
    public Vector3 start_temp;
    int randomStep = 30;
    public float[] rightCarX = { 3, 8, 3, 8, 3, 8, 8, 3 };
    private float level = 0.0f;
    private int log1;
    public float z_start;

    void Start()
    {
        start_temp = objectPosition.position;
        z_start = start_temp.z;
    }
    // Update is called once per frame
    void Update()
    {
        level += 0.01f;
        if (level % 10 > 0 && level % 10 < 0.01)
        {
            speed -= 100.0f;
        }
        rb.velocity = new Vector3(0f, 0f, speed * Time.deltaTime);
        temp1 = objectPosition.position;

        //float z1_disp = Random.Range(30, 40);
        if (temp1.z < -275)
        {
            if (temp1.x > 0)
            {
                temp1.x = rightCarX[Random.Range(0, 7)];
                Debug.Log("right lane");
            }
            int randomZ = Random.Range(20, 200);
            //temp1.z = 200 + (Mathf.Floor(randomZ / randomStep)) * randomStep;
            Debug.Log(temp1.z);
            temp1.z = z_start;
            objectPosition.position = temp1;
        }

    }

    void OnCollisionEnter(Collision CollisionInfo)
    {
        crash = GetComponent<AudioSource>();
        if (CollisionInfo.collider.tag == "CarGame")
        {
            crash.Play();
        }

        else if (CollisionInfo.collider.tag == "Obstacle")
        {
            if (temp1.x > 0)
            {
                temp1.x = rightCarX[Random.Range(0, 8)];
            }
            //int randomZ = Random.Range(20, 200);
            //temp1.z = 200 + (Mathf.Floor(randomZ / randomStep)) * randomStep;

            temp1.z = z_start;
            objectPosition.position = temp1;
        }
    }

}
