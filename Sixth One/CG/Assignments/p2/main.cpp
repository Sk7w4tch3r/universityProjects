#include <GL/glut.h>
#include <stdlib.h> 
#include <iostream>
#include <math.h>

using namespace std;

const GLfloat light_ambient[]  = { 0.0f, 0.0f, 0.0f, 1.0f };
const GLfloat light_diffuse[]  = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_specular[] = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_position[] = { 2.0f, 5.0f, 5.0f, 0.0f }; 
 
const GLfloat mat_ambient[]    = { 0.0f, 1.0f, 0.3f, 1.0f };
const GLfloat mat_diffuse[]    = { 0.8f, 0.8f, 0.8f, 1.0f };
const GLfloat mat_specular[]   = { 0.5f, 1.0f, 1.0f, 1.0f };
const GLfloat high_shininess[] = { 80.0f }; 

float posX = 0.0;
float posY = 0.0;
float posZ = -8.0;
float posXMoon = 0.0;
float posYMoon = 0.0;
float posZMoon = 0.0;
float EarthT   = 0.0;
float MoonT   = 0.0;
float angle = 0.0f;

float a = 3.5;
float b = 0.5;


static void resize(int width, int height){
    const float ar = (float) width / (float) height; 
 
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0); 
 
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity() ;
} 


static void display(void){ 

 	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    
    glPushMatrix(); // sun
        glColor3d(1,1,0); 
		glTranslated(0,0,-10);
		glRotated(angle, 1.0f, 1.0f, 1.0f);
        glutSolidSphere(0.9,15,15);
    glPopMatrix(); 

	glPushMatrix(); // earth
		glColor3d(0,0,1); 
        glTranslated(posX, posY, posZ);
		glRotated(angle, 1.0f, 1.0f, 1.0f);
        glutSolidSphere(0.2,30,30);
    glPopMatrix(); 

    glPushMatrix(); // moon
		glColor3d(1,1,1); 
        glTranslated(posX+posXMoon, posY+posYMoon, posZMoon);
        glutSolidSphere(0.1,50,50);
    glPopMatrix(); 

	angle+=0.5f;

    glutSwapBuffers();
} 
 

void timer(int someshit){
	EarthT += 0.05;
    MoonT += 0.1;
	posX = a * cos(EarthT);
    posZ = -10 + 2 * sin(EarthT);
    posXMoon = 0.5 * cos(MoonT);
    posYMoon = 0.5 * sin(MoonT);
	posZMoon = posZ + 0.5 * sin(MoonT);
	glutPostRedisplay();
	glutTimerFunc(50, timer, 1);
}
 

int main(int argc, char *argv[]){
    glutInit(&argc, argv);
    glutInitWindowSize(1080,720);
    glutInitWindowPosition(10,10);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH); 
 
    glutCreateWindow("Sun and Earth and moon and some code :)"); 
 
    glutReshapeFunc(resize);
    glutDisplayFunc(display); 
 
    glClearColor(0,0,0,1);
    glEnable(GL_CULL_FACE);
    // glCullFace(GL_BACK); 
 
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS); 
 
    glEnable(GL_LIGHT0);
    glEnable(GL_NORMALIZE);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING); 
 
    glLightfv(GL_LIGHT0, GL_AMBIENT,  light_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  light_diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position); 
 
    glMaterialfv(GL_FRONT, GL_AMBIENT,   mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE,   mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess); 
 
	glutTimerFunc(50, timer, 1);
	glutIdleFunc(display);
    glutMainLoop(); 
 
    return EXIT_SUCCESS;
}
