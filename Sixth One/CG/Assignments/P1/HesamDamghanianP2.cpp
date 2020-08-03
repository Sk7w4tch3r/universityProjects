#include <GL/glut.h>
#include <math.h>

void renderFunction1();
void renderFunction2();
void renderFunction3();
void renderFunction4();
void renderFunction5();

int main(int argc, char** argv) {

	
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGB);

	glutInitWindowPosition(80, 80);
	glutInitWindowSize(400, 300);
	glutCreateWindow("first");
	glutDisplayFunc(renderFunction1);
	glutInitWindowPosition(200, 80);
	glutCreateWindow("second");
	glutDisplayFunc(renderFunction2);
	glutInitWindowPosition(80, 200);
	glutCreateWindow("third");
	glutDisplayFunc(renderFunction3);
	glutInitWindowPosition(400, 80);
	glutCreateWindow("fourth");
	glutDisplayFunc(renderFunction4);
	glutInitWindowPosition(80, 400);
	glutCreateWindow("fifth");
	glutDisplayFunc(renderFunction5);

	glutMainLoop();
}



void renderFunction1() {

	glClear(GL_COLOR_BUFFER_BIT);
	glShadeModel(GL_SMOOTH);

	// triangle with each node having a color in smooth shade mode
	glBegin(GL_POLYGON);
	glColor3f(1, 0, 0); glVertex3f(-0.6f, -0.75f, 0.5f);
	glColor3f(0, 1, 0); glVertex3f(0.6f, -0.75f, 0.0f);
	glColor3f(0, 0, 1); glVertex3f(0.0f, 0.75f, 0.0f);
	glEnd();

	
}

void renderFunction2() {

	glClear(GL_COLOR_BUFFER_BIT);
	
	// red rectangle
	glColor3f(1,0,0);
	glRectf(-0.5,0.5, 0.5, -0.5);

}

void renderFunction3() {

	glClear(GL_COLOR_BUFFER_BIT);
	glShadeModel(GL_FLAT);

	// flat shade mode example
	glBegin(GL_POLYGON);
	glColor3f(1, 0, 0); glVertex3f(-0.3f, -0.75f, 0.5f);
	glColor3f(0, 1, 0); glVertex3f(0.3f, -0.75f, 0.0f);
	glColor3f(0, 0, 1); glVertex3f(0.6f, 0.75f, 0.0f);
	glColor3f(0, 1, 1); glVertex3f(-0.4f, 0.75f, 0.0f);
	glEnd();

}

void renderFunction4() {

	glClear(GL_COLOR_BUFFER_BIT);
	glShadeModel(GL_SMOOTH);

	// hexagon
	glBegin(GL_POLYGON);
	glColor3f(1, 0, 0); glVertex3f(-0.75f, 0.0f, 0.5f);
	glColor3f(0, 1, 0); glVertex3f(-0.25f, 0.75f, 0.0f);
	glColor3f(1, 0, 0); glVertex3f(0.25f, 0.75f, 0.5f);
	glColor3f(0, 1, 0); glVertex3f(0.75f, 0.0f, 0.0f);
	glColor3f(0, 0, 1); glVertex3f(0.25f, -0.75f, 0.0f);
	glColor3f(0, 0, 1); glVertex3f(-0.25f, -0.75f, 0.0f);
	glEnd();

	glFlush();
}

void renderFunction5() {

	glClear(GL_COLOR_BUFFER_BIT);
	

	// ellipse
	float x1, y1, x2, y2;
	float angle;
	double radius = 0.5;

	x1 = 0, y1 = 0;
	
	glColor3f(0, 0, 1);
	glBegin(GL_TRIANGLE_FAN);
	glVertex2f(x1, y1);

	for (angle = 1.0f; angle<361.0f; angle += 0.2)
	{
		x2 = x1 + sin(angle)*radius;
		y2 = y1 + cos(angle)*radius;
		
		glVertex2f(x2, y2);
	}

	glEnd();

	glFlush();
}
