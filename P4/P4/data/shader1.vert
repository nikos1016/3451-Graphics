#define PROCESSING_TEXTURE_SHADER
#define PROCESSING_TEXLIGHT_SHADER

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
varying vec4 vertTexCoordR;
varying vec4 vertTexCoordL;
varying vec3 vertNormal;
varying vec3 vertLightDirect;

void main() {
  vertColor = color;
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);
  vertNormal = normalize(normalMatrix * normal);
  vec4 vert = position;
  gl_Position = transform * vert;
  vertLightDirect = normalize(-lightNormal);
}
