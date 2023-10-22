# renderer class

import RT_utility as rtu
import numpy as np
from PIL import Image as im

def background_color(rGen_ray):
    unit_direction = rtu.Vec3.unit_vector(rGen_ray.getDirection())
    a = (unit_direction.y() + 1.0)*0.5
    return rtu.Color(1,1,1)*(1.0-a) + rtu.Color(0.5, 0.7, 1.0)*a

class Renderer():

    def __init__(self, cCamera) -> None:

        self.camera = cCamera
        pass

    def render(self):
        for j in range(self.camera.img_height):
            for i in range(self.camera.img_width):

                pixel_color = rtu.Color(0,0,0)
                generated_ray = self.camera.get_center_ray(i, j)
                pixel_color = background_color(generated_ray)

                self.camera.write_to_film(i, j, pixel_color)


    def write_img2png(self, strPng_filename):
        png_film = self.camera.film * 255
        data = im.fromarray(png_film.astype(np.uint8))
        data.save(strPng_filename)

