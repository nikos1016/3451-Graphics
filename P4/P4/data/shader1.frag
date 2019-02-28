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
  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  //gl_FragColor = vec4(diffuse_color.rgb, 1.0);
  float centerGrey = (diffuse_color.r)*0.2989+(diffuse_color.g)*0.5870+(diffuse_color.b)*0.1140;
  float diffuse = clamp(dot (vertNormal, vertLightDirect),0.0,1.0);

  // then look at surrounding pixel
  vec2 leftPos = vec2(vertTexCoord.x-.01,vertTexCoord.y);
  vec2 rightPos = vec2(vertTexCoord.x+.01,vertTexCoord.y);
  vec2 upPos = vec2(vertTexCoord.x, vertTexCoord.y+.01);
  vec2 downPos = vec2(vertTexCoord.x, vertTexCoord.y-.01);

  vec4 left = texture2D(texture, leftPos.xy);
  vec4 up = texture2D(texture, upPos.xy);
  vec4 right = texture2D(texture, rightPos.xy);
  vec4 down = texture2D(texture, downPos.xy);

  float leftGrey = 	(left.r) *0.2989+(left.g) *0.5870+(left.b)	*0.1140;
  float upGrey = 	(up.r)	 *0.2989+(up.g)	  *0.5870+(up.b)	*0.1140;
  float rightGrey = (right.r)*0.2989+(right.g)*0.5870+(right.b)	*0.1140;
  float downGrey = 	(down.r) *0.2989+(down.g) *0.5870+(down.b)	*0.1140;

  float edgeDetec = (leftGrey+upGrey+rightGrey+downGrey)-(4*centerGrey);

  vec4 edgeColor = vec4(edgeDetec,edgeDetec,edgeDetec,1);

  gl_FragColor = vec4(diffuse * edgeColor.rgb*3, 1.0);
}
