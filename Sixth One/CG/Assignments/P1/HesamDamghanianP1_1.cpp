#include <GL/glew.h>
#include <GL/freeglut.h>
#include <iostream>
using namespace std;

bool keyboard = true;
float 
rotateH = 0,
rotateV = 0,
xrotated, yrotated, zrotated;

int
CurrentWidth = 800,
CurrentHeight = 600;

void keyPress(int key, int x, int y);
void ResizeFunction(int, int);
void RenderFunction(void);
void animation(void);

int main(int argc, char* argv[])
{
	glutInit(&argc, argv);
	glutInitWindowSize(CurrentWidth, CurrentHeight);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutCreateWindow("P1");
	glutSpecialFunc(keyPress);
	glutReshapeFunc(ResizeFunction);
	glutDisplayFunc(RenderFunction);
	glutIdleFunc(animation);
	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
	glutMainLoop();
	exit(EXIT_SUCCESS);
}


void ResizeFunction(int Width, int Height)
{
	CurrentWidth = Width;
	CurrentHeight = Height;
	glViewport(0, 0, CurrentWidth, CurrentHeight);
}


void RenderFunction(void)
{
	glMatrixMode(GL_MODELVIEW);
	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
		
	if (keyboard){
		glRotatef(rotateH, 0.0f, 0.5f, 0.0f);
		glRotatef(rotateV, 0.0f, 0.0f, 0.5f);
	}
	else
	{
		glRotatef(xrotated, 1.0f, 0.0f, 0.0f);
		glRotatef(yrotated, 0.0f, 1.0f, 0.0f);
		glRotatef(zrotated, 0.0f, 0.0f, 1.0f);
	}

	

	glBegin(GL_QUADS);
	
	// top
	glColor3f(0.0f, 0.1f, 0.2f);
	glVertex3f(0.5, 0.5, -0.5);
	glColor3f(0.9f, 0.8f, 0.7f);
	glVertex3f(-0.5, 0.5, -0.5);
	glColor3f(0.8f, 0.7f, 0.6f);
	glVertex3f(-0.5, 0.5, 0.5);	
	glColor3f(0.7f, 0.6f, 0.5f);
	glVertex3f(0.5, 0.5, 0.5);

	//right
	glColor3f(0.5f, 0.6f, 0.7f);
	glVertex3f(0.5, 0.5, -0.5);
	glColor3f(0.9f, 0.8f, 0.7f);
	glVertex3f(0.5, 0.5, 0.5);
	glColor3f(0.8f, 0.7f, 0.6f);
	glVertex3f(0.5, -0.5, 0.5);
	glColor3f(0.7f, 0.6f, 0.5f);
	glVertex3f(0.5, -0.5, -0.5);

	//left
	glColor3f(0.4f, 0.5f, 0.6f);
	glVertex3f(-0.5, 0.5, 0.5);
	glColor3f(0.9f, 0.8f, 0.7f);
	glVertex3f(-0.5, 0.5, -0.5);
	glColor3f(0.8f, 0.7f, 0.6f);
	glVertex3f(-0.5, -0.5, -0.5);
	glColor3f(0.7f, 0.6f, 0.5f);
	glVertex3f(-0.5, -0.5, 0.5);

	//front
	glColor3f(0.3f, 0.4f, 0.5f);
	glVertex3f(0.5, 0.5, 0.5);
	glColor3f(0.9f, 0.8f, 0.7f);
	glVertex3f(-0.5, 0.5, 0.5);
	glColor3f(0.8f, 0.7f, 0.6f);
	glVertex3f(-0.5, -0.5, 0.5);
	glColor3f(0.7f, 0.6f, 0.5f);
	glVertex3f(0.5, -0.5, 0.5);

	//back
	glColor3f(0.2f, 0.3f, 0.4f);
	glVertex3f(0.5, -0.5, -0.5);
	glColor3f(0.9f, 0.8f, 0.7f);
	glVertex3f(-0.5, -0.5, -0.5);
	glColor3f(0.8f, 0.7f, 0.6f);
	glVertex3f(-0.5, 0.5, -0.5);
	glColor3f(0.7f, 0.6f, 0.5f);
	glVertex3f(0.5, 0.5, -0.5);

	//bottom
	glColor3f(0.1f, 0.2f, 0.3f);
	glVertex3f(0.5, -0.5, 0.5);
	glColor3f(0.9f, 0.8f, 0.7f);
	glVertex3f(-0.5, -0.5, 0.5);
	glColor3f(0.8f, 0.7f, 0.6f);
	glVertex3f(-0.5, -0.5, -0.5);
	glColor3f(0.7f, 0.6f, 0.5f);
	glVertex3f(0.5, -0.5, -0.5);


	glEnd();

	glFlush();
	glutSwapBuffers();
	glutPostRedisplay();
}

void keyPress(int key, int x, int y){
	
	if (key == 27)
		exit(0);
	if (key == GLUT_KEY_RIGHT)
		rotateH += 1;
	if (key == GLUT_KEY_LEFT)
		rotateH -= 1;
	if (key == GLUT_KEY_UP)
		rotateV += 1;
	if (key == GLUT_KEY_DOWN)
		rotateV -= 1;

	glutPostRedisplay();
		
}

void animation(void)
{

	yrotated += 0.01;
	xrotated += 0.02;
	RenderFunction();
}
