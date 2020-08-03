#include <GL/glew.h>
#include <GL/freeglut.h>

int rotateX = 15, rotateY = -15, rotateZ = 0;

float vertexCoords[24] = {
	1, 1, 1, 
	1, 1, -1,
	1, -1, -1,
	1, -1, 1,
	-1, 1, 1,
	-1, 1, -1,
	-1, -1, -1,
	-1, -1, 1 };

float vertexColors[24] = {
	1, 1, 1,
	1, 0, 0,
	1, 1, 0,
	0, 1, 0,
	0, 0, 1,
	1, 0, 1,
	0, 0, 0,
	0, 1, 1 };

int elementArray[24] = { 
	0, 1, 2,
	3, 0, 3,
	7, 4, 0,
	4, 5, 1,
	6, 2, 1,
	5, 6, 5,
	4, 7, 6,
	7, 3, 2 };


void renderFunction(void) {
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();

	glRotatef(rotateZ, 0, 0, 1);
	glRotatef(rotateY, 0, 1, 0);
	glRotatef(rotateX, 1, 0, 0);

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_COLOR_ARRAY);          
	

	glVertexPointer(3, GL_FLOAT, 0, vertexCoords); 
	glColorPointer(3, GL_FLOAT, 0, vertexColors);

	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_INT, elementArray); 
	glutSwapBuffers();
}


void keyPress(int key, int x, int y) {
	if (key == GLUT_KEY_LEFT)
		rotateY -= 15;
	else if (key == GLUT_KEY_RIGHT)
		rotateY += 15;
	else if (key == GLUT_KEY_DOWN)
		rotateX += 15;
	else if (key == GLUT_KEY_UP)
		rotateX -= 15;
	else if (key == GLUT_KEY_PAGE_UP)
		rotateZ += 15;
	else if (key == GLUT_KEY_PAGE_DOWN)
		rotateZ -= 15;
	else if (key == GLUT_KEY_HOME)
		rotateX = rotateY = rotateZ = 0;
	glutPostRedisplay();
}

void initGL() {
	glMatrixMode(GL_PROJECTION);
	glOrtho(-4, 4, -2, 2, -2, 2); 
	glMatrixMode(GL_MODELVIEW);
	glEnable(GL_DEPTH_TEST);
	glClearColor(0.5, 0.5, 0.5, 1);
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH);
	glutInitWindowSize(600, 300);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("P1");
	initGL();
	glutDisplayFunc(renderFunction);
	glutSpecialFunc(keyPress);
	glutMainLoop();
	return 0;
}