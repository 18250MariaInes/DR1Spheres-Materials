"""
Maria Ines Vasquez Figueroa
18250
Gráficas
DR1 Spheres & Textures
Main
"""

from gl import Raytracer, color
from obj import Obj, Texture
from sphere import Sphere, Material


"""brick = Material(diffuse = color(0.8, 0.25, 0.25 ))
stone = Material(diffuse = color(0.4, 0.4, 0.4 ))
grass = Material(diffuse = color(0.5, 1, 0))"""
coal = Material(diffuse = color(0, 0, 0))
snow = Material(diffuse = color(1, 1, 1))
carrot=Material(diffuse = color(1, 0.65, 0))
eyes=Material(diffuse = color(0.90, 0.90, 0.90))


width = 500
height = 800
r = Raytracer(width,height)
#dibujo de muñeco de nieve
#cuerpo
r.scene.append( Sphere((0, 0.7,  -5), 0.5, snow) )
r.scene.append( Sphere((0, 0, -5), 0.6, snow) )
r.scene.append( Sphere((0, -1, -5), 0.9, snow) )

#botones
r.scene.append( Sphere((0, 0,  -4), 0.1, coal) )
r.scene.append( Sphere((0, -0.4, -4), 0.1, coal) )
r.scene.append( Sphere((0, -0.8, -4), 0.1, coal) )

#nariz
r.scene.append( Sphere((0, 0.6,  -4), 0.1, carrot) )

#sonrisa
r.scene.append( Sphere((-0.08, 0.4,  -4), 0.05, coal) )
r.scene.append( Sphere((0.08, 0.4,  -4), 0.05, coal) )
r.scene.append( Sphere((-0.20, 0.47,  -4), 0.05, coal) )
r.scene.append( Sphere((0.20, 0.47,  -4), 0.05, coal) )

#ojos
r.scene.append( Sphere((-0.09, 0.8,  -4), 0.08, eyes) )
r.scene.append( Sphere((0.09, 0.8,  -4), 0.08, eyes) )
r.scene.append( Sphere((-0.09, 0.7,  -3.5), 0.03, coal) )
r.scene.append( Sphere((0.09, 0.7,  -3.5), 0.03, coal) )

r.rtRender()

r.glFinish('output.bmp')





