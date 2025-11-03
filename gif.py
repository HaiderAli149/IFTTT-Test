import imageio.v3 as iio 

filenames = ['testflash1.png', 'testflash2.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('flash.gif', images, duration = 500, loop =0)

