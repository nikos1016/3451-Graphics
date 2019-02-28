#define PROCESSING_COLOR_SHADER

uniform mat4 transform;
uniform mat4 texMatrix;
uniform mat3 normalMatrix;
uniform vec3 lightNormal;

attribute vec4 position;
attribute vec4 color;
attribute vec2 texCoord;
attribute vec3 normal;

varying vec4 vertColor;
varying vec4 vertTexCoord;
varying vec3 vertNormal;
varying vec3 vertLightDirect;

void main() {
  vertNormal = normalize(normalMatrix * normal);
  vertColor = color;
  vec4 vert = position;
  gl_Position = transform * vert;
  vertLightDirect = normalize(-lightNormal);
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);
}
