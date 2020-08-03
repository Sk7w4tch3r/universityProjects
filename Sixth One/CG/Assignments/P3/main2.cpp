#include <GL/glut.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>

const GLfloat light_ambient[] = {0.0f, 0.0f, 0.0f, 1.0f};
const GLfloat light_diffuse[] = {1.0f, 1.0f, 1.0f, 1.0f};
const GLfloat light_specular[] = {1.0f, 1.0f, 1.0f, 1.0f};
const GLfloat light_position[] = {2.0f, 5.0f, 5.0f, 0.0f};

const GLfloat mat_ambient[] = {0.0f, 1.0f, 0.3f, 1.0f};
const GLfloat mat_diffuse[] = {0.8f, 0.8f, 0.8f, 1.0f};
const GLfloat mat_specular[] = {0.5f, 1.0f, 1.0f, 1.0f};
const GLfloat high_shininess[] = {80.0f};

float earthX    = 0.0;
float earthY    = 0.0;
float earthZ    = -8.0;
float moonX     = 0.0;
float moonY     = 0.0;
float moonZ     = 0.0;

float marsX = 0.0;
float marsY = 0.0;
float marsZ = 0.0;
float camx  = 0.0;
float camy  = -5.0;
float camz  = 10.0;

float marsT     = 0.0;
float earthT    = 0.0;
float moonT     = 0.0;
float angle     = 0.0f;
float earthA    = 3.5;
float earthB    = 0.5;
float marsA     = 2.5;
float marsB     = 0.7;

static void display(void);
void NormalKeyHandler(unsigned char key, int x, int y);
void SpecialKeyHandler(int key, int x, int y);
void MouseHandler(int button, int state, int x, int y);
void timer(int someshit);
void resize(int width, int height);

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitWindowSize(1080, 720);
    glutInitWindowPosition(10, 10);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

    glutCreateWindow("Solar System 	ヽ( •_)ᕗ");
    glutFullScreen();

    glutReshapeFunc(resize);
    glutDisplayFunc(display);

    glClearColor(0, 0, 0, 1);
    glEnable(GL_CULL_FACE);
    glCullFace(GL_BACK);

    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    glEnable(GL_LIGHT0);
    glEnable(GL_NORMALIZE);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);

    glutTimerFunc(50, timer, 1);
    glutMouseFunc(MouseHandler);
    glutSpecialFunc(SpecialKeyHandler);
    glutKeyboardFunc(NormalKeyHandler);
    glutIdleFunc(display);

    glutMainLoop();

    return EXIT_SUCCESS;
}

static void display(void)
{

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glPushMatrix(); // sun
    glColor3d(1, 1, 0);
    glTranslated(0, 0, -10);
    glRotated(angle, 1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.9, 15, 15);
    glPopMatrix();

    glPushMatrix(); // earth
    glColor3d(0, 0, 1);
    glTranslated(earthX, earthY, earthZ);
    glRotated(angle, 1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.2, 30, 30);
    glPopMatrix();

    glPushMatrix(); // moon
    glColor3d(0.95, 0.94, 0.78);
    glTranslated(earthX + moonX, earthY + moonY, moonZ);
    glutSolidSphere(0.1, 50, 50);
    glPopMatrix();

    glPushMatrix(); // mars
    glColor3d(0.73, 0.16, 0.22);
    glTranslated(marsX, marsY, marsZ);
    glRotated(angle, 1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.21, 30, 30);
    glPopMatrix();

    angle += 0.5f;

    glutSwapBuffers();
}

void SpecialKeyHandler(int key, int x, int y){
    if (key == GLUT_KEY_UP){
        camy -= 1;
    }
    else if (key == GLUT_KEY_DOWN){
        camy += 1;
    }
    else if (key == GLUT_KEY_LEFT){
        camx -= 1;
    }
    else if (key == GLUT_KEY_RIGHT){
        camx += 1;
    }
}

void NormalKeyHandler(unsigned char key, int x, int y){
    switch (key) {
      case 27: // Escape key
         exit (0);
         break;      
    }
}

void MouseHandler(int button, int state, int x, int y){
    if ((button == 3) || (button == 4))
    {
        if (button == 3 && state == GLUT_UP){
            camz -= 1;
        }else if (button == 4 && state == GLUT_UP){
            camz += 1;
        }
    }
}

void resize(int width, int height){
    const float ar = (float)width / (float)height;

    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void timer(int someshit){

    marsT   += 0.08;
    earthT  += 0.05;
    moonT   += 0.1;
    earthX  = earthA * cos(earthT);
    earthZ  = -10 + 2 * sin(earthT);
    moonX   = 0.5 * cos(moonT);
    moonY   = 0.5 * sin(moonT);
    moonZ   = earthZ + 0.5 * sin(moonT);
    marsX   = marsA * cos(marsT);
    marsZ   = -10 + 2 * sin(marsT);
    glLoadIdentity();
    gluLookAt(camx, camy, camz, 0.0, 0.0, -10.0, 0.0, 1.0, 0.0);
    glutPostRedisplay();
    glutTimerFunc(50, timer, 1);
}