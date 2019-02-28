#define PROCESSING_TEXTURE_SHADER
#define PROCESSING_TEXLIGHT_SHADER

uniform mat4 transform;
uniform mat4 texMatrix;
uniform mat3 normalMatrix;
uniform vec3 lightNormal;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;
varying vec4 vertTexCoordR;
varying vec4 vertTexCoordL;
varying vec3 vertNormal;
varying vec3 vertLightDirect;

uniform sampler2D texture;

void main() {
  vertColor = color;
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);
  vertNormal = normalize(normalMatrix * normal);
  vec4 pos = position;
  vec4 textColor = texture2D(texture, vertTexCoord.xy);
  float greyColor = (textColor.r)*0.2989+(textColor.g)*0.5870+(textColor.b)*0.1140;
  pos+=vec4(vertNormal*greyColor*200,0.0);
  gl_Position = transform * pos;
  vertLightDirect = normalize(-lightNormal);
}
