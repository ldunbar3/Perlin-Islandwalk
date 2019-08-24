noise_scale = 0.005
Xlength = 800
Ylength = 800


def setup():
    size(Xlength, Ylength)
    background(52, 164, 206)
    
    for x in range(Xlength):
        for y in range(Ylength):
            n = noise(x * noise_scale, y * noise_scale)
            if n > .5:
                stroke(204, 192, 155)
            if n > .70:
                stroke(96, 117, 94)
            if n > .85:
                stroke(150, 150, 150)
            

                
            if n > .5:
                point(x, y)
                
