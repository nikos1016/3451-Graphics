#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

varying vec4 vertColor;
varying vec4 vertTexCoord;
varying vec3 vertNormal;
varying vec3 vertLightDirect;

void main() {
  //gl_FragColor = vec4(0.2, 0.4, 1.0, vertTexCoord.x);
	vec4 diffuse_color = vec4 (0.0, 1.0, 1.0, 1.0);
 	float diffuse = clamp(dot (vertNormal, vertLightDirect),0.0,1.0);
	for(int i=0; i<3; i++){
 		for(int j=0; j<3; j++){
 			// now the current point is (i/4, j/4)
 			float xPos = float(1.0/6.0) + float(1.0/3.0)*i;
 			float yPos = float(1.0/6.0) + float(1.0/3.0)*j;
 			float distance = sqrt(((xPos-float(vertTexCoord.x))*(xPos-float(vertTexCoord.x)))+((yPos-float(vertTexCoord.y))*(yPos-float(vertTexCoord.y))));
 			if(distance<0.1111){
 				gl_FragColor = vec4(diffuse * diffuse_color.rgb, 0.0);
 				return;
 			}
 			else{
 				gl_FragColor = vec4(diffuse * diffuse_color.rgb, 0.8);
 			}
 		}
 	}

}
