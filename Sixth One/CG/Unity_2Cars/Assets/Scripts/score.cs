using System.Globalization;
using UnityEngine;
using UnityEngine.UI;

public class score : MonoBehaviour
{
    public Text scoreText;
    private float scoreVal = 0f;
    private bool stillAlive;

    void Start()
    {
        stillAlive = true;
        scoreVal = 0f;
    }

    // Update is called once per frame
    void Update()
    {
        if (stillAlive)
        {
            scoreVal += 0.005f;
        }
        scoreText.text = "Score: " + ((int)scoreVal).ToString();
    }
}
