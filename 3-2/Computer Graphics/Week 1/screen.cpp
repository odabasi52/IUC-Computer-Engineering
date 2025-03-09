#include <GLFW/glfw3.h>
#include <iostream>
/* g++ screen.cpp -o screen -lglfw -lGL */


int main()
{
    bool init = glfwInit();
    if (!init)
    {
        std::cerr << "GLFW Initialization failed!" << std::endl;
        return -1;
    }

    //width, height, title, monitor, share
    GLFWwindow *window = glfwCreateWindow(800, 600, "OpenGL Window", NULL, NULL);
    if (!window)
    {
        std::cerr << "Window creation failed!" << std::endl;
        glfwTerminate();
        return -1;
    }

    // Makes the created window's OpenGL context current.
    glfwMakeContextCurrent(window);

    // Sets the background color of the window
    // r, g, b, opacity
    glClearColor(0.0f, 0.0f, 1.0f, 1.0f);

    // Loop until the user closes the window
    while (!glfwWindowShouldClose(window))
    {
        // Clears the color buffer (framebuffer) before rendering the next frame.
        glClear(GL_COLOR_BUFFER_BIT);
        
        // Swap the front and back buffers, displaying the new frame on the screen
        glfwSwapBuffers(window);

        // Processes input and window events (like closing, resizing, or keyboard input)
        glfwPollEvents();
    }

    // Destroys the created window and frees resources
    glfwDestroyWindow(window);

    // Terminates GLFW, cleaning up any allocated resources
    glfwTerminate();
    return 0;
}