using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ExitInGame : MonoBehaviour
{
    public void QuitInGame()
    {
        Debug.Log("Quit Game");
        Application.Quit();
    }
}
