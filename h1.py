from sketchpy import canvas as sp #pip install sketchpy
path = "Enter photo path with / for example- C:/Users/krish/Downloads/h4.jpg"
screen = sp.sketch_from_image(path)
screen.draw()