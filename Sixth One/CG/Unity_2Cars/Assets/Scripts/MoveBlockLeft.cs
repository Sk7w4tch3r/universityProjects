using System;
using System.Collections;
using System.Diagnostics;
using System.Threading;
using UnityEngine;
using Random = UnityEngine.Random;
using Debug = UnityEngine.Debug;
using System.Collections.Specialized;

public class MoveBlockLeft : MonoBehaviour
{
    public AudioSource crash;
    public Rigidbody rb;
    public Transform objectPosition;
    public float speed = -800f;
    public Vector3 temp;
    public Vector3 start_temp;
    int randomStep = 30;
    public float[] leftCarX = { -3, -8, -3, -3, -8, -3, -8, -8 };
    private float level = 0.0f;
    private int log;
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
        temp = objectPosition.position;


        //float z_disp = Random.Range(35, 50);
        if (temp.z < -275)
        {
            if (temp.x < 0)
            {
                temp.x = leftCarX[Random.Range(0, 8)];
                Debug.Log("left lane");
            }
            int randomZ = Random.Range(20, 210);
            //temp.z = 200 + (Mathf.Floor(randomZ / randomStep)) * randomStep;
            Debug.Log(temp.z);
            temp.z = z_start;
            objectPosition.position = temp;
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
            if (temp.x < 0)
            {
                temp.x = leftCarX[Random.Range(0, 8)];
                Debug.Log("left lane");
            }
            int randomZ = Random.Range(20, 210);
            //temp.z = 200 + (Mathf.Floor(randomZ / randomStep)) * randomStep;

            temp.z = z_start;
            objectPosition.position = temp;
        }
    }
}
