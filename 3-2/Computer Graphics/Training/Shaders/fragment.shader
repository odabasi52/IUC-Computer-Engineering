#version 330 core

out vec4 FragColor;
in vec3 myFragColor;
in vec2 myTextureCoord;

uniform sampler2D texture0;
uniform sampler2D texture1;

uniform vec4 lightColor;
uniform vec3 lightPos;
uniform vec3 camPos;

in vec3 myNormal;
in vec3 myCurPos;

vec4 pointLight()
{
    vec3 lightVector = lightPos - myCurPos;
    float distance = length(lightVector);
    float a = 1.5f;
    float b = 0.3f;
    float intensity = 1.0f / (a* distance * distance + b * distance + 1.0f);

    float ambient = 0.2f;

    vec3 normal = normalize(myNormal);
    vec3 lightDir = normalize(lightVector);

    float diffuse = max(dot(normal, lightDir), 0.0);

    float specularLight = 0.5f;
    vec3 viewDir = normalize(camPos - myCurPos);
    vec3 reflectDir = reflect(-lightDir, normal);
    float specAmount = pow(max(dot(viewDir, reflectDir), 0.0f), 16);
    float specular = specularLight * specAmount;

    return (texture(texture0, myTextureCoord) * (diffuse*intensity + ambient) + texture(texture1, myTextureCoord).r * specular * intensity) * lightColor;
}

vec4 directionalLight()
{
    float ambient = 0.2f;

    vec3 normal = normalize(myNormal);

    // give specific direction
    vec3 lightDir = normalize(vec3(1.0f, 1.0f, 0.0f));

    float diffuse = max(dot(normal, lightDir), 0.0);

    float specularLight = 0.5f;
    vec3 viewDir = normalize(camPos - myCurPos);
    vec3 reflectDir = reflect(-lightDir, normal);
    float specAmount = pow(max(dot(viewDir, reflectDir), 0.0f), 16);
    float specular = specularLight * specAmount;

    return (texture(texture0, myTextureCoord) * (diffuse + ambient) + texture(texture1, myTextureCoord).r * specular) * lightColor;
}

vec4 spotLight()
{
    vec3 lightVector = lightPos - myCurPos;
    float outerCone = 0.90f;
    float innerCone = 0.95f;

    float ambient = 0.2f;

    vec3 normal = normalize(myNormal);
    vec3 lightDir = normalize(lightVector);

    float diffuse = max(dot(normal, lightDir), 0.0);

    float specularLight = 0.5f;
    vec3 viewDir = normalize(camPos - myCurPos);
    vec3 reflectDir = reflect(-lightDir, normal);
    float specAmount = pow(max(dot(viewDir, reflectDir), 0.0f), 16);
    float specular = specularLight * specAmount;

    float angle = dot(vec3(0.0f, -1.0f, 0.0f), -lightDir);
    float intensity = clamp((angle - outerCone) / (innerCone - outerCone), 0.0f, 1.0f);

    return (texture(texture0, myTextureCoord) * (diffuse*intensity + ambient) + texture(texture1, myTextureCoord).r * specular * intensity) * lightColor;
}

void main()
{
    FragColor = pointLight();
}