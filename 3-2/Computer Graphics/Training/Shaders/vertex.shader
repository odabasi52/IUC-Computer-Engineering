#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;
layout (location = 2) in vec2 aTex;
layout (location = 3) in vec3 aNormal;

out vec3 myFragColor;
out vec2 myTextureCoord;

out vec3 myNormal;
out vec3 myCurPos;

uniform mat4 camMatrix;
uniform mat4 model;

void main()
{
    myCurPos = vec3(model * vec4(aPos, 1.0));

    gl_Position = camMatrix * vec4(myCurPos, 1.0);
    myFragColor = aColor;
    myTextureCoord = aTex;
    myNormal = aNormal;
}