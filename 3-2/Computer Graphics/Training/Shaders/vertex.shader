#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec3 aColor;
layout (location = 3) in vec2 aTex;


out vec3 myCurPos;
out vec3 myNormal;

out vec3 myFragColor;
out vec2 myTextureCoord;



uniform mat4 camMatrix;
uniform mat4 model;

void main()
{
    myCurPos = vec3(model * vec4(aPos, 1.0));

    myNormal = aNormal;
    myFragColor = aColor;
    myTextureCoord = aTex;
    

    gl_Position = camMatrix * vec4(myCurPos, 1.0);
}