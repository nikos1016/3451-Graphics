#define PROCESSING_TEXTURE_SHADER
#define PROCESSING_TEXLIGHT_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;
varying vec3 vertNormal;
varying vec3 vertLightDirect;

void main() {
  //vec4 diffuse_color = texture2D(texture, vertTexCoord.xy) * vertColor;
  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  gl_FragColor = vec4(diffuse_color.rgb, 1.0);
}
