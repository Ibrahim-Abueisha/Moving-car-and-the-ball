from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0.6, 0.6, 0.5, 1)
    glClear(GL_COLOR_BUFFER_BIT)

def Draw_view():

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)     #TheRoad
    glColor3f(0.2, 0.3, 0.4)
    glVertex(300, -1, -6)
    glVertex(300, -1, 6)
    glVertex(-30, -1, 6)
    glVertex(-30, -1, -6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(2.5, -1, -0.3)
    glVertex(2.5, -1, 0.3)
    glVertex(-2.5, -1, 0.3)
    glVertex(-2.5, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(5, -1, -0.3)
    glVertex(5, -1, 0.3)
    glVertex(10, -1, 0.3)
    glVertex(10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-5, -1, -0.3)
    glVertex(-5, -1, 0.3)
    glVertex(-10, -1, 0.3)
    glVertex(-10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(15, -1, -0.3)
    glVertex(15, -1, 0.3)
    glVertex(25, -1, 0.3)
    glVertex(25, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)  #The tree
    glColor3f(0.3,0.1,0)
    glVertex(15, -1, -6)
    glVertex(14.2, -1, -6)
    glVertex(14.2, 1.5, -6)
    glVertex(15, 1.5, -6)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.7, 0)
    glVertex(16, 1.5, -6)
    glVertex(13.2, 1.5, -6)
    glVertex(14.6, 3.5, -6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.1, 0)
    glVertex(-7, -1, -6)
    glVertex(-6.2, -1, -6)
    glVertex(-6.2, 1.5, -6)
    glVertex(-7, 1.5, -6)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.7, 0)
    glVertex(-8, 1.5, -6)
    glVertex(-5.2, 1.5, -6)
    glVertex(-6.6, 3.5, -6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.1, 0)
    glVertex(1, -1, -6)
    glVertex(1.8, -1, -6)
    glVertex(1.8, 1.5, -6)
    glVertex(1, 1.5, -6)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.7, 0)
    glVertex(0, 1.5, -6)
    glVertex(2.8, 1.5, -6)
    glVertex(1.4, 3.5, -6)
    glEnd()

angle = 0
x = 0
forward = True
car_z = 0

def arrowkeys(key, x, y):
    global car_z
    if key == GLUT_KEY_LEFT:
        car_z += 1
    elif key == GLUT_KEY_RIGHT:
        car_z -= 1
    display()

def display():
    global car_z
    global angle
    global x
    global forward

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Draw_view()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5 + x, -2.5 * 0.25, - 2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-2.5 + x, -2.5 * 0.25, - 2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x,0,0 + car_z)
    glColor3f(1,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1, 1, 0)
    glTranslate(0 + x, 1.25, 0 + car_z)
    glScale(0.5, 0.2, 0.45)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1, 0, 0)
    glTranslate(0 + x, 1.25, 0 + car_z)
    glScale(0.5, 0.2, 0.45)
    glutWireCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5 + x, -2.5 * 0.25, 2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-2.5+x, -2.5 * 0.25, 2.5 * 0.5 + car_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 0.1)
    glutSolidTorus(0.2, 0.55, 20, 15)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1, 1, 0)
    glTranslate(2.5+x, 0, 0.6 + car_z)
    glutWireSphere(0.3, 10, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1, 1, 0)
    glTranslate(2.5 + x, 0, - 0.6 + car_z)
    glutWireSphere(0.3, 10, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0, 0.9, 0)
    glTranslate(2.5 - x, 0, - 0.6 )
    glutSolidSphere(1, 100, 100)

    if forward:
        x += 0.025
        angle -= 0.1
        if x > 20:
                forward = False
    else:
        x -= 0.025
        angle += 0.1
        if x < -8:
            forward = True

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700,700)
glutCreateWindow(b"Moving car and the ball")
glutDisplayFunc(display)
glutIdleFunc(display)
glutSpecialFunc(arrowkeys)
myInit()
glutMainLoop()