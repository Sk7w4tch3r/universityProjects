#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>

static int shoulderR = -30, elbowR = 0;
static int shoulderL = 0, elbowL = 0;

void display(void);
void reshape(int w, int h);
void keyboard(unsigned char key, int x, int y);
void timer(int t);

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
   glutInitWindowSize (500, 500); 
   glutCreateWindow (argv[0]);
   glutFullScreen();
   
   glClearColor (0.0, 0.0, 0.0, 0.0);
   glShadeModel (GL_FLAT);
   
   glutTimerFunc(50, timer, 1);
   glutDisplayFunc(display); 
   glutReshapeFunc(reshape);
   glutKeyboardFunc(keyboard);
   glutMainLoop();
   return 0;
}

int tmp = 1;
int s   = 3;
int e   = 5;
void timer(int t){
   
   if (shoulderR > 30 || shoulderR < -30 ){
      tmp *= -1;
   }

   shoulderR += tmp*s;
   elbowR    += tmp*e;
   glutPostRedisplay();
   glutTimerFunc(80, timer, 1);
}

void display(void)
{
   glClear (GL_COLOR_BUFFER_BIT);

   // Right Arm
   glPushMatrix();
   glColor3f(0, 0.5, 0);
   glTranslatef (0.75, 0.75, 0.0);
   glRotatef ((GLfloat) shoulderR, 0.0, 0.0, 1.0);
   glTranslatef (0.65, 0.0, 0.0);
   glPushMatrix();
   glScalef (1.25, 0.4, 0.1);
   glutSolidCube (1.0);
   glPopMatrix();
   glTranslatef (0.65, 0.0, 0.0);
   glRotatef ((GLfloat) elbowR, 0.0, 0.0, 1.0);
   glTranslatef (0.5, 0.0, 0.0);
   glPushMatrix();
   glScalef (1, 0.4, 0.1);
   glutSolidCube (1.0);
   glPopMatrix();
   glPopMatrix();

   // Left Arm
   glPushMatrix();
   glColor3f(0, 0.5, 0);
   glTranslatef (-0.75, 0.75, 0.0);
   glRotatef ((GLfloat) shoulderR, 0.0, 0.0, 1.0);
   glTranslatef (-0.65, 0.0, 0.0);
   glPushMatrix();
   glScalef (1.25, 0.4, 0.1);
   glutSolidCube (1.0);
   glPopMatrix();
   glTranslatef (-0.65, 0.0, 0.0);
   glRotatef ((GLfloat) elbowR, 0.0, 0.0, 1.0);
   glTranslatef (-0.5, 0.0, 0.0);
   glPushMatrix();
   glScalef (1, 0.4, 0.1);
   glutSolidCube (1.0);
   glPopMatrix();
   glPopMatrix();

   // Head
   glPushMatrix();
   glTranslatef (0, 1.65, 0.0);
   glColor3f(0.5, 0.5, 0.5);
   glutSolidSphere(0.5, 50, 50);
   glPopMatrix();

   // Body
   glPushMatrix();
   glColor3f(0.5, 0.5, 0);
   glScalef (1.5, 2, 0.5);
   glutSolidCube (1.0);
   glPopMatrix();


   // Legs
   glPushMatrix();
   glColor3f(0,0,1);
   glTranslatef(0, -2, 0);
   glPushMatrix();
   glTranslatef(0.5, 0, 0);
   glScalef (0.5, 2, 0.5);
   glutSolidCube (1.0);
   glPopMatrix();
   glPushMatrix();
   glTranslatef(0, 1, 0);
   glScalef (1.5, 0.3, 0.5);
   glutSolidCube (1.0);
   glPopMatrix();
   glPushMatrix();
   glTranslatef(-0.5, 0, 0);
   glScalef (0.5, 2, 0.5);
   glutSolidCube (1.0);
   glPopMatrix();
   glPopMatrix();


   glutSwapBuffers();
}

void reshape (int w, int h)
{
   glViewport (0, 0, (GLsizei) w, (GLsizei) h); 
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   gluPerspective(65.0, (GLfloat) w/(GLfloat) h, 1.0, 20.0);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   glTranslatef (0.0, 0.0, -5.0);
}

void keyboard (unsigned char key, int x, int y)
{
   switch (key) {
      case 27: // Escape key
         exit (0);
         break;      
   }
}
