#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

// Kamera ayarları
glm::vec3 cameraPos   = glm::vec3(0.0f, 0.0f, 3.0f);  // Kamera başlangıç konumu
glm::vec3 cameraFront = glm::vec3(0.0f, 0.0f, -1.0f); // Kamera yönü
glm::vec3 cameraUp    = glm::vec3(0.0f, 1.0f, 0.0f);  // Yukarı yön vektörü

// Kamera hızı
float cameraSpeed = 0.05f;

void processInput(GLFWwindow* window) {
    // İleri - Geri hareket (Z ve X)
    if (glfwGetKey(window, GLFW_KEY_Z) == GLFW_PRESS)
        cameraPos += cameraSpeed * cameraFront; // İleri git
    if (glfwGetKey(window, GLFW_KEY_X) == GLFW_PRESS)
        cameraPos -= cameraSpeed * cameraFront; // Geri git

    // Sola - Sağa hareket (A ve D)
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        cameraPos -= glm::normalize(glm::cross(cameraFront, cameraUp)) * cameraSpeed; // Sola git
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        cameraPos += glm::normalize(glm::cross(cameraFront, cameraUp)) * cameraSpeed; // Sağa git

    // Yukarı - Aşağı hareket (W ve S)
    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        cameraPos += cameraSpeed * cameraUp; // Yukarı çık
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        cameraPos -= cameraSpeed * cameraUp; // Aşağı in
}

// shader güncellendi (kamera için)
// projection * view * transform * vec4(aPos, 1.0)
const char* vertexShaderSource = R"(
#version 330 core
layout (location = 0) in vec3 aPos;
uniform mat4 transform;
uniform mat4 view; 
uniform mat4 projection; 
void main()
{
    gl_Position = projection * view * transform * vec4(aPos, 1.0);
}
)";

const char* fragmentShaderSource = R"(
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(1.0, 0.5, 0.2, 1.0);
}
)";

int main()
{
    glfwInit();
    GLFWwindow* window = glfwCreateWindow(800, 600, "Transform Triangle", NULL, NULL);
    glfwMakeContextCurrent(window);
    gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);

    /*
    If your display is scaled, the framebuffer size is different from the window size. 
    Get the framebuffer size with glfwGetFramebufferSize and set the viewport based on the framebuffer size
    */
    int fbSizeX, fbSizeY;
    glfwGetFramebufferSize(window, &fbSizeX, &fbSizeY);
    glViewport(0, 0, fbSizeX, fbSizeY);

    unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);
    
    unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);
    
    unsigned int shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    float vertices[] = {
        -0.5f, -0.5f, 0.0f,
         0.5f, -0.5f, 0.0f,
         0.0f,  0.5f, 0.0f
    };
    
    unsigned int VAO, VBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    while (!glfwWindowShouldClose(window))
    {
        processInput(window); // Kullanıcı girişlerini işle

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // Diagonal Matrix with 1 (Birim Matris)
        glm::mat4 myTransform = glm::mat4(1.0f);

        // Specifies the translation vector. In this case, it translates by (0.0, 1.0, 0.0),
        // which means move 1 unit in the positive y-direction.
        myTransform = glm::translate(myTransform, glm::vec3(0.0f, 0.0f, 0.0f));
        myTransform = glm::rotate(myTransform, (float)glfwGetTime(), glm::vec3(0.0f, 0.0f, 1.0f));
        myTransform = glm::scale(myTransform, glm::vec3(1.0f, 1.0f, 1.0f));
        unsigned int transformLoc = glGetUniformLocation(shaderProgram, "transform");        
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, glm::value_ptr(myTransform));


        // Kamera (View Matrix)
        glm::mat4 view = glm::lookAt(cameraPos, cameraPos + cameraFront, cameraUp);
        unsigned int viewLoc = glGetUniformLocation(shaderProgram, "view");
        glUniformMatrix4fv(viewLoc, 1, GL_FALSE, glm::value_ptr(view));

        // Perspektif Projeksiyon Matrisi
        glm::mat4 projection = glm::ortho(-5.0f, 5.0f, -5.0f, 5.0f, 0.1f, 100.0f);
        unsigned int projectionLoc = glGetUniformLocation(shaderProgram, "projection");
        glUniformMatrix4fv(projectionLoc, 1, GL_FALSE, glm::value_ptr(projection));


        glUseProgram(shaderProgram);

        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);

    glfwTerminate();
    return 0;
}
