#version 330 core

out vec4 FragColor;
in vec3 myFragColor;
void main()
{
    FragColor = vec4(myFragColor, 1.0f);
}