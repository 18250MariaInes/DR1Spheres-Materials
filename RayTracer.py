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
import random

brick = Material(diffuse = color(0.8, 0.25, 0.25 ))
stone = Material(diffuse = color(0.4, 0.4, 0.4 ))
grass = Material(diffuse = color(0.5, 1, 0))


width = 500
height = 300
r = Raytracer(width,height)

r.scene.append( Sphere((0, 0,  -7), 1, brick) )
r.scene.append( Sphere((1, 1, -10), 1, stone) )
r.scene.append( Sphere((-1.5, -1.5, -13), 1, grass) )
 
r.rtRender()

r.glFinish('output.bmp')





