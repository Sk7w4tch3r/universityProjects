using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;
public class GameManagerRight : MonoBehaviour
{
    public GameObject GameOverUI;
    public bool GameHasEnded = false;
    public void GameOver()
    {
        if (GameHasEnded == false)
        {
            GameHasEnded = true;
            Debug.Log("Game Over Right Car");
            GameOverUI = GameObject.Find("GameOverPanel");
            StartCoroutine(wait());
        }
    }
    IEnumerator wait()
    {
        //yield on a new YieldInstruction that waits for 7 seconds.
        yield return new WaitForSeconds(6);
        Restart();
    }
    void Restart()
    {
        // SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }

}