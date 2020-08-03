#include <stdlib.h>
#include <math.h>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

// angle of rotation for the camera direction
float angle = 0.0f;

// actual vector representing the camera's direction
float lx=0.0f,lz=-1.0f;

// XZ position of the camera
float x=0.0f, z=5.0f;

// the key states. These variables will be zero
//when no key is being presses
float deltaAngle = 0.0f;
float deltaMove = 0;
int xOrigin = -1;

void changeSize(int w, int h) {

	// Prevent a divide by zero, when window is too short
	// (you cant make a window of zero width).
	if (h == 0)
		h = 1;

	float ratio =  w * 1.0 / h;

	// Use the Projection Matrix
	glMatrixMode(GL_PROJECTION);

	// Reset Matrix
	glLoadIdentity();

	// Set the viewport to be the entire window
	glViewport(0, 0, w, h);

	// Set the correct perspective.
	gluPerspective(45.0f, ratio, 0.1f, 100.0f);

	// Get Back to the Modelview
	glMatrixMode(GL_MODELVIEW);
}

void drawSnowMan() {

	glColor3f(1.0f, 1.0f, 1.0f);

// Draw Body
	glTranslatef(0.0f ,0.75f, 0.0f);
	glutSolidSphere(0.75f,20,20);

// Draw Head
	glTranslatef(0.0f, 1.0f, 0.0f);
	glutSolidSphere(0.25f,20,20);

// Draw Eyes
	glPushMatrix();
	glColor3f(0.0f,0.0f,0.0f);
	glTranslatef(0.05f, 0.10f, 0.18f);
	glutSolidSphere(0.05f,10,10);
	glTranslatef(-0.1f, 0.0f, 0.0f);
	glutSolidSphere(0.05f,10,10);
	glPopMatrix();

// Draw Nose
	glColor3f(1.0f, 0.5f , 0.5f);
	glRotatef(0.0f,1.0f, 0.0f, 0.0f);
	glutSolidCone(0.08f,0.5f,10,2);
}

void computePos(float deltaMove) {

	x += deltaMove * lx * 0.1f;
	z += deltaMove * lz * 0.1f;
}

void renderScene(void) {

	if (deltaMove)
		computePos(deltaMove);

	// Clear Color and Depth Buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// Reset transformations
	glLoadIdentity();
	// Set the camera
	gluLookAt(	x, 1.0f, z,
			x+lx, 1.0f,  z+lz,
			0.0f, 1.0f,  0.0f);

// Draw ground

	glColor3f(0.9f, 0.9f, 0.9f);
	glBegin(GL_QUADS);
		glVertex3f(-100.0f, 0.0f, -100.0f);
		glVertex3f(-100.0f, 0.0f,  100.0f);
		glVertex3f( 100.0f, 0.0f,  100.0f);
		glVertex3f( 100.0f, 0.0f, -100.0f);
	glEnd();

// Draw 36 SnowMen

	for(int i = -3; i < 3; i++)
		for(int j=-3; j < 3; j++) {
                     glPushMatrix();
                     glTranslatef(i*10.0,0,j * 10.0);
                     drawSnowMan();
                     glPopMatrix();
               }
        glutSwapBuffers();
} 

void processNormalKeys(unsigned char key, int xx, int yy) { 	

        if (key == 27)
              exit(0);
} 

void pressKey(int key, int xx, int yy) {

       switch (key) {
             case GLUT_KEY_UP : deltaMove = 0.5f; break;
             case GLUT_KEY_DOWN : deltaMove = -0.5f; break;
       }
} 

void releaseKey(int key, int x, int y) { 	

        switch (key) {
             case GLUT_KEY_UP :
             case GLUT_KEY_DOWN : deltaMove = 0;break;
        }
} 

void mouseMove(int x, int y) { 	

         // this will only be true when the left button is down
         if (xOrigin >= 0) {

		// update deltaAngle
		deltaAngle = (x - xOrigin) * 0.001f;

		// update camera's direction
		lx = sin(angle + deltaAngle);
		lz = -cos(angle + deltaAngle);
	}
}

void mouseButton(int button, int state, int x, int y) {

	// only start motion if the left button is pressed
	if (button == GLUT_LEFT_BUTTON) {

		// when the button is released
		if (state == GLUT_UP) {
			angle += deltaAngle;
			xOrigin = -1;
		}
		else  {// state = GLUT_DOWN
			xOrigin = x;
		}
	}
}

int main(int argc, char **argv) {

	// init GLUT and create window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(320,320);
	glutCreateWindow("Lighthouse3D - GLUT Tutorial");

	// register callbacks
	glutDisplayFunc(renderScene);
	glutReshapeFunc(changeSize);
	glutIdleFunc(renderScene);

	glutIgnoreKeyRepeat(1);
	glutKeyboardFunc(processNormalKeys);
	glutSpecialFunc(pressKey);
	glutSpecialUpFunc(releaseKey);

	// here are the two new functions
	glutMouseFunc(mouseButton);
	glutMotionFunc(mouseMove);

	// OpenGL init
	glEnable(GL_DEPTH_TEST);

	// enter GLUT event processing cycle
	glutMainLoop();

	return 1;
}



// //----------------------------------------------------------------------
// //	Best if viewed with tab stops set every 2 columns.
// //----------------------------------------------------------------------
// //	File: opengl-3D-sample.cpp - Sample 3D OpenGL/GLUT program
// //	Origin: Lighthouse3D (heavily modified by Dave Mount)
// //
// //	This is a sample program that illustrates OpenGL and GLUT. It
// //	renders a picture of 36 snowmen. The camera can be moved by dragging
// //	the mouse. The camera moves forward by hitting the up-arrow key and
// //	back by moving the down-arrow key. Hit ESC, 'q' or 'Q' to exit.
// //
// //	Warning #1: This program uses the function glutSpecialUpFunc, which
// //	may not be available in all GLUT implementations. If your system
// //	does not have it, you can comment this line out, but the up arrow
// //	processing will not be correct.
// //
// //	Warning #2: This is a minimalist program. Very little attention has
// //	been paid to good programming technique.
// //----------------------------------------------------------------------

// #include <stdlib.h> // standard definitions
// #include <math.h> // math definitions
// #include <stdio.h> // standard I/O

// // include files are in a slightly different location for MacOS
// #ifdef __APPLE__
// #include <GLUT/glut.h>
// #else
// #include <GL/glut.h>
// #endif

// // escape key (for exit)
// #define ESC 27

// //----------------------------------------------------------------------
// // Global variables
// //
// // The coordinate system is set up so that the (x,y)-coordinate plane
// // is the ground, and the z-axis is directed upwards. The y-axis points
// // to the north and the x-axis points to the east.
// //
// // The values (x,y) are the current camera position. The values (lx, ly)
// // point in the direction the camera is looking. The variables angle and
// // deltaAngle control the camera's angle. The variable deltaMove
// // indicates the amount of incremental motion for the camera with each
// // redraw cycle. The variables isDragging and xDragStart are used to
// // monitor the mouse when it drags (with the left button down).
// //----------------------------------------------------------------------

// // Camera position
// float x = 0.0, y = -5.0; // initially 5 units south of origin
// float deltaMove = 0.0; // initially camera doesn't move

// // Camera direction
// float lx = 0.0, ly = 1.0; // camera points initially along y-axis
// float angle = 0.0; // angle of rotation for the camera direction
// float deltaAngle = 0.0; // additional angle change when dragging

// // Mouse drag control
// int isDragging = 0; // true when dragging
// int xDragStart = 0; // records the x-coordinate when dragging starts

// //----------------------------------------------------------------------
// // Reshape callback
// //
// // Window size has been set/changed to w by h pixels. Set the camera
// // perspective to 45 degree vertical field of view, a window aspect
// // ratio of w/h, a near clipping plane at depth 1, and a far clipping
// // plane at depth 100. The viewport is the entire window.
// //
// //----------------------------------------------------------------------
// void changeSize(int w, int h) 
// {
// 	float ratio =  ((float) w) / ((float) h); // window aspect ratio
// 	glMatrixMode(GL_PROJECTION); // projection matrix is active
// 	glLoadIdentity(); // reset the projection
// 	gluPerspective(45.0, ratio, 0.1, 100.0); // perspective transformation
// 	glMatrixMode(GL_MODELVIEW); // return to modelview mode
// 	glViewport(0, 0, w, h); // set viewport (drawing area) to entire window
// }

// //----------------------------------------------------------------------
// // Draw one snowmen (at the origin)
// //
// // A snowman consists of a large body sphere and a smaller head sphere.
// // The head sphere has two black eyes and an orange conical nose. To
// // better create the impression they are sitting on the ground, we draw
// // a fake shadow, consisting of a dark circle under each.
// //
// // We make extensive use of nested transformations. Everything is drawn
// // relative to the origin. The snowman's eyes and nose are positioned
// // relative to a head sphere centered at the origin. Then the head is
// // translated into its final position. The body is drawn and translated
// // into its final position.
// //----------------------------------------------------------------------
// void drawSnowman()
// {
// 	// Draw body (a 20x20 spherical mesh of radius 0.75 at height 0.75)
// 	glColor3f(1.0, 1.0, 1.0); // set drawing color to white
// 	glPushMatrix();
// 		glTranslatef(0.0, 0.0, 0.75);
// 		glutSolidSphere(0.75, 20, 20);
// 	glPopMatrix();

// 	// Draw the head (a sphere of radius 0.25 at height 1.75)
// 	glPushMatrix();
// 		glTranslatef(0.0, 0.0, 1.75); // position head
// 		glutSolidSphere(0.25, 20, 20); // head sphere

// 		// Draw Eyes (two small black spheres)
// 		glColor3f(0.0, 0.0, 0.0); // eyes are black
// 		glPushMatrix();
// 			glTranslatef(0.0, -0.18, 0.10); // lift eyes to final position
// 			glPushMatrix();
// 				glTranslatef(-0.05, 0.0, 0.0);
// 				glutSolidSphere(0.05, 10, 10); // right eye
// 			glPopMatrix();
// 			glPushMatrix();
// 				glTranslatef(+0.05, 0.0, 0.0);
// 				glutSolidSphere(0.05, 10, 10); // left eye
// 			glPopMatrix();
// 		glPopMatrix();

// 		// Draw Nose (the nose is an orange cone)
// 		glColor3f(1.0, 0.5, 0.5); // nose is orange
// 		glPushMatrix();
// 			glRotatef(90.0, 1.0, 0.0, 0.0); // rotate to point along -y
// 			glutSolidCone(0.08, 0.5, 10, 2); // draw cone
// 		glPopMatrix();
// 	glPopMatrix();

// 	// Draw a faux shadow beneath snow man (dark green circle)
// 	glColor3f(0.0, 0.5, 0.0);
// 	glPushMatrix();
// 		glTranslatef(0.2, 0.2, 0.001);	// translate to just above ground
// 		glScalef(1.0, 1.0, 0.0); // scale sphere into a flat pancake
// 		glutSolidSphere(0.75, 20, 20); // shadow same size as body
// 	glPopMatrix();
// }

// //----------------------------------------------------------------------
// // Update with each idle event
// //
// // This incrementally moves the camera and requests that the scene be
// // redrawn.
// //----------------------------------------------------------------------
// void update(void) 
// {
// 	if (deltaMove) { // update camera position
// 		x += deltaMove * lx * 0.1;
// 		y += deltaMove * ly * 0.1;
// 	}
// 	glutPostRedisplay(); // redisplay everything
// }

// //----------------------------------------------------------------------
// // Draw the entire scene
// //
// // We first update the camera location based on its distance from the
// // origin and its direction.
// //----------------------------------------------------------------------
// void renderScene(void) 
// {
// 	int i, j;

// 	// Clear color and depth buffers
// 	glClearColor(0.0, 0.7, 1.0, 1.0); // sky color is light blue
// 	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

// 	// Reset transformations
// 	glLoadIdentity();

// 	// Set the camera centered at (x,y,1) and looking along directional
// 	// vector (lx, ly, 0), with the z-axis pointing up
// 	gluLookAt(
// 			x,      y,      1.0,
// 			x + lx, y + ly, 1.0,
// 			0.0,    0.0,    1.0);

// 	// Draw ground - 200x200 square colored green
// 	glColor3f(0.0, 0.7, 0.0);
// 	glBegin(GL_QUADS);
// 		glVertex3f(-100.0, -100.0, 0.0);
// 		glVertex3f(-100.0,  100.0, 0.0);
// 		glVertex3f( 100.0,  100.0, 0.0);
// 		glVertex3f( 100.0, -100.0, 0.0);
// 	glEnd();

// 	// Draw 36 snow men
// 	for(i = -3; i < 3; i++)
// 		for(j = -3; j < 3; j++) {
// 			glPushMatrix();
// 				glTranslatef(i*7.5, j*7.5, 0);
// 				drawSnowman();
// 			glPopMatrix();
// 		}

// 	glutSwapBuffers(); // Make it all visible
// } 

// //----------------------------------------------------------------------
// // User-input callbacks
// //
// // processNormalKeys: ESC, q, and Q cause program to exit
// // pressSpecialKey: Up arrow = forward motion, down arrow = backwards
// // releaseSpecialKey: Set incremental motion to zero
// //----------------------------------------------------------------------
// void processNormalKeys(unsigned char key, int xx, int yy)
// {
// 	if (key == ESC || key == 'q' || key == 'Q') exit(0);
// } 

// void pressSpecialKey(int key, int xx, int yy)
// {
// 	switch (key) {
// 		case GLUT_KEY_UP : deltaMove = 1.0; break;
// 		case GLUT_KEY_DOWN : deltaMove = -1.0; break;
// 	}
// } 

// void releaseSpecialKey(int key, int x, int y) 
// {
// 	switch (key) {
// 		case GLUT_KEY_UP : deltaMove = 0.0; break;
// 		case GLUT_KEY_DOWN : deltaMove = 0.0; break;
// 	}
// } 

// //----------------------------------------------------------------------
// // Process mouse drag events
// // 
// // This is called when dragging motion occurs. The variable
// // angle stores the camera angle at the instance when dragging
// // started, and deltaAngle is a additional angle based on the
// // mouse movement since dragging started.
// //----------------------------------------------------------------------
// void mouseMove(int x, int y) 
// { 	
// 	if (isDragging) { // only when dragging
// 		// update the change in angle
// 		deltaAngle = (x - xDragStart) * 0.005;

// 		// camera's direction is set to angle + deltaAngle
// 		lx = -sin(angle + deltaAngle);
// 		ly = cos(angle + deltaAngle);
// 	}
// }

// void mouseButton(int button, int state, int x, int y) 
// {
// 	if (button == GLUT_LEFT_BUTTON) {
// 		if (state == GLUT_DOWN) { // left mouse button pressed
// 			isDragging = 1; // start dragging
// 			xDragStart = x; // save x where button first pressed
// 		}
// 		else  { /* (state = GLUT_UP) */
// 			angle += deltaAngle; // update camera turning angle
// 			isDragging = 0; // no longer dragging
// 		}
// 	}
// }

// //----------------------------------------------------------------------
// // Main program  - standard GLUT initializations and callbacks
// //----------------------------------------------------------------------
// int main(int argc, char **argv) 
// {
// 	printf("\n\
// -----------------------------------------------------------------------\n\
//   OpenGL Sample Program:\n\
//   - Drag mouse left-right to rotate camera\n\
//   - Hold up-arrow/down-arrow to move camera forward/backward\n\
//   - q or ESC to quit\n\
// -----------------------------------------------------------------------\n");

// 	// general initializations
// 	glutInit(&argc, argv);
// 	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
// 	glutInitWindowPosition(100, 100);
// 	glutInitWindowSize(800, 400);
// 	glutCreateWindow("OpenGL/GLUT Sampe Program");

// 	// register callbacks
// 	glutReshapeFunc(changeSize); // window reshape callback
// 	glutDisplayFunc(renderScene); // (re)display callback
// 	glutIdleFunc(update); // incremental update 
// 	glutIgnoreKeyRepeat(1); // ignore key repeat when holding key down
// 	glutMouseFunc(mouseButton); // process mouse button push/release
// 	glutMotionFunc(mouseMove); // process mouse dragging motion
// 	glutKeyboardFunc(processNormalKeys); // process standard key clicks
// 	glutSpecialFunc(pressSpecialKey); // process special key pressed
// 						// Warning: Nonstandard function! Delete if desired.
// 	glutSpecialUpFunc(releaseSpecialKey); // process special key release

// 	// OpenGL init
// 	glEnable(GL_DEPTH_TEST);

// 	// enter GLUT event processing cycle
// 	glutMainLoop();

// 	return 0; // this is just to keep the compiler happy
// }



































// // #include <GL/glut.h>
// // #include <math.h>

// // void init(void)
// // {
// //     glClearColor(0.0, 0.0, 0.0, 0.0);
// //     glMatrixMode(GL_PROJECTION);
// //     gluOrtho2D(0.0, 400.0, 0.0, 300.0);
// // }



// // void myWireSphere(GLfloat radius, int slices, int stacks)
// // {
// //     glPushMatrix();
// //     glRotatef(-90.0, 1.0, 0.0, 0.0);
// //     glutWireSphere(radius, slices, stacks);
// //     glPopMatrix();
// // }

// // static int year = 0, day = 0;
// // void display()
// // {
// //     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
// //     glPushMatrix();

// //     glColor3f(1.0, 1.0, 0.0); //ກຳນົດສີດວງຕາເວັນ myWireSphere(1.0, 100, 100); //ກຳນົດຂະໜາດ,ເສັ້ນແວງ,ເສັ້ນຂະໜານຂອງຕະເວັນ

// //     glRotatef((GLfloat)year, 0.0, 1.0, 0.0); //ກຳນົດການໝູນຮອບ glTranslatef (2.0, 0.0, 0.0); //ກຳນົດໄລຍະຫ່າງການໜູນຂອງດາວອ້ອມດວງຕາເວັນ glRotatef((GLfloat)day, 0.0, 1.0, 0.0); //ການໜູນອ້ອມຕົວມັນເອງຂອງດາວ glColor3f(1.9, 0.5, 0.0); myWireSphere(0.4, 15, 15); //ກຳນົດຂະໜາດ,ເສັ້ນແວງ,ເສັ້ນຂະໜານຂອງດາວເຄາະ

// //     glRotatef((GLfloat)year, 0.0, 1.0, 0.0);
// //     glTranslatef(4.0, 0.0, 0.0);
// //     glRotatef((GLfloat)day, 0.0, 1.0, 0.0);
// //     glColor3f(2.0, 0.0, 1.0);
// //     myWireSphere(0.4, 15, 15);

// //     glRotatef((GLfloat)year, 0.0, 1.0, 0.0);
// //     glTranslatef(6.0, 0.0, 0.0);
// //     glRotatef((GLfloat)day, 0.0, 1.0, 0.0);
// //     glColor3f(0.0, 1.0, 1.0);
// //     myWireSphere(0.4, 15, 15);

// //     glRotatef((GLfloat)year, 0.0, 1.0, 0.0);
// //     glTranslatef(5.0, 0.0, 0.0);
// //     glRotatef((GLfloat)day, 0.0, 1.0, 0.0);
// //     glColor3f(0.0, 0.5, 1.9);
// //     myWireSphere(0.4, 15, 15);

// //     glColor3f(1, 1, 1);
// //     glBegin(GL_LINES);
// //     glVertex3f(0, -0.3, 0);
// //     glVertex3f(0, 0.3, 0);
// //     glEnd();

// //     glPopMatrix();
// //     glFlush();
// //     glutSwapBuffers();
// // }

// // static GLfloat u = 0.0;
// // static GLfloat du = 0.1;

// // void timer(int v)
// // {
// //     u += du;
// //     day = (day + 1) % 360;
// //     year = (year + 2) % 360;
// //     glLoadIdentity();
// //     gluLookAt(20*cos(u / 8.0) + 12, 5*sin(u / 8.0) + 1, 10 * cos(u / 8.0) + 2, 0, 0, 0, 0, 1, 0);
// //     glutPostRedisplay();
// //     glutTimerFunc(1000 / 30, timer, v);
// // }

// // void reshape(GLint w, GLint h)
// // {
// //     glViewport(0, 0, w, h);
// //     glMatrixMode(GL_PROJECTION);
// //     glLoadIdentity();
// //     gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 1.0, 40.0);
// //     glMatrixMode(GL_MODELVIEW);
// // }

// // int main(int argc, char **argv)
// // {
// //     glutInit(&argc, argv);
// //     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
// //     glutInitWindowSize(800, 600);
// //     glutCreateWindow("CS8 Group");
// //     init();
// //     glutDisplayFunc(display);
// //     glutReshapeFunc(reshape);
// //     glutTimerFunc(100, timer, 0);
// //     glEnable(GL_DEPTH_TEST);
// //     glutMainLoop();
// // }
