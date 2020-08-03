using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Threading;
using UnityEngine;

public class rightController : MonoBehaviour
{
    public Transform carPosition;
    public Rigidbody rb;
    private float speed = 2000f;
    public Vector3 leftPos = new Vector3(3f, 0.5f, -9f);
    public Vector3 rightPos = new Vector3(8f, 0.5f, -9f);
    public bool toggle = false;
    public AudioSource horn_right;
    
    // Update is called once per frame
    void Update()
    {
        if (Input.GetButtonDown("right"))
        {
            horn_right = GetComponent<AudioSource>();
            toggle = !toggle;
            if (toggle == true)
            {
                horn_right.Play();
                rb.velocity = new Vector3(speed * Time.deltaTime,0,0);
            }
            else
            {
                horn_right.Play();
                rb.velocity = new Vector3(-speed * Time.deltaTime, 0, 0);
            }

            //rb.MovePosition((Vector3)carPosition.position + (leftPos * speed * Time.deltaTime));
        }
    }
    void OnCollisionEnter(Collision CollisionInfo)
    {
        if (CollisionInfo.collider.tag == "Obstacle")
        {
            
            Debug.Log(CollisionInfo.collider.name);
            FindObjectOfType<GameManagerRight>().GameOver();
        }
    }
}
