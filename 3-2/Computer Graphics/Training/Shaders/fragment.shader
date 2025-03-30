#version 330 core

out vec4 FragColor;
in vec3 myFragColor;
in vec2 myTextureCoord;
uniform sampler2D texture0;
void main()
{
    FragColor = texture(texture0, myTextureCoord);
}