import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(554, 554, "Cuadrícula Manual (554x554)", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(0.05, 0.05, 0.05, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        glLineWidth(1.0)
        glBegin(GL_LINES)

        # ==========================================
        # 1. LÍNEAS VERTICALES (De abajo hacia arriba)
        # ==========================================
        glColor3f(0.3, 0.3, 0.3)  # Gris para las líneas secundarias

        glVertex2f(-1.0, -1.0); glVertex2f(-1.0,  1.0) # Borde izquierdo
        glVertex2f(-0.8, -1.0); glVertex2f(-0.8,  1.0)
        glVertex2f(-0.6, -1.0); glVertex2f(-0.6,  1.0)
        glVertex2f(-0.4, -1.0); glVertex2f(-0.4,  1.0)
        glVertex2f(-0.2, -1.0); glVertex2f(-0.2,  1.0)

        # EJE Y CENTRAL (Rojo)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f( 0.0, -1.0); glVertex2f( 0.0,  1.0) # Centro vertical
        glColor3f(0.3, 0.3, 0.3)

        glVertex2f( 0.2, -1.0); glVertex2f( 0.2,  1.0)
        glVertex2f( 0.4, -1.0); glVertex2f( 0.4,  1.0)
        glVertex2f( 0.6, -1.0); glVertex2f( 0.6,  1.0)
        glVertex2f( 0.8, -1.0); glVertex2f( 0.8,  1.0)
        glVertex2f( 1.0, -1.0); glVertex2f( 1.0,  1.0) # Borde derecho

        # ==========================================
        # 2. LÍNEAS HORIZONTALES (De izquierda a derecha)
        # ==========================================
        glVertex2f(-1.0, -1.0); glVertex2f( 1.0, -1.0) # Borde inferior
        glVertex2f(-1.0, -0.8); glVertex2f( 1.0, -0.8)
        glVertex2f(-1.0, -0.6); glVertex2f( 1.0, -0.6)
        glVertex2f(-1.0, -0.4); glVertex2f( 1.0, -0.4)
        glVertex2f(-1.0, -0.2); glVertex2f( 1.0, -0.2)

        # EJE X CENTRAL (Rojo)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-1.0,  0.0); glVertex2f( 1.0,  0.0) # Centro horizontal
        glColor3f(0.3, 0.3, 0.3)

        glVertex2f(-1.0,  0.2); glVertex2f( 1.0,  0.2)
        glVertex2f(-1.0,  0.4); glVertex2f( 1.0,  0.4)
        glVertex2f(-1.0,  0.6); glVertex2f( 1.0,  0.6)
        glVertex2f(-1.0,  0.8); glVertex2f( 1.0,  0.8)
        glVertex2f(-1.0,  1.0); glVertex2f( 1.0,  1.0) # Borde superior

        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
# Fondo del modelo

#modelo del perosnaje