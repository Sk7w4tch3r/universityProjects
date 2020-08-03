using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class dayNnight : MonoBehaviour
{

    public Transform Sun;
    private Vector3 temp;
    private int count = 0;
   
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (count % 10 == 0)
        {
            Sun.rotation *= Quaternion.Euler(0.3f, 0,0);
        }
        count += 1;
    }
}
