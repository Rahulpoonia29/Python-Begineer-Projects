from PIL import Image, ImageDraw
from numpy import arange

width = 1000
height = 1000
img = Image.new("RGB", (width,height), "white")
draw = ImageDraw.Draw(img)
# Z = complex(0,0)
# c = complex(1,1)
# values = [Z]
c = complex(0,0)
for imaginary in arange(0,2,0.01):
    for rl in arange(0,2,0.01):
        c = complex(rl,imaginary)
        values = [complex(0,0)]
        for i in range(0,200):
            Z_n = (values[i]**2) + c
            if (((Z_n.real)**2)+((Z_n.imag)**2))**(1/2) < 2:
                output = True
                values.append(Z_n)
            else: 
                output = False
                break
        
        if output == True:
            
            # point_drawn = ((values[-1].real*1000)*(width/2),(values[-1].imag*1000)*(height/2))
            point_drawn = ((values[-1].real*1000),(values[-1].imag*1000))
            draw.point(point_drawn,fill="black")
img.save("image.png")            
Image.open("image.png")     
            
            
#     # print(values)

# # mandelbort(0,5)

# def plot(start,end,fuc):
#     img = Image.new("RGB", (500,500), "white")
#     draw = ImageDraw.Draw(img)
#     modified_values =  []
#     for i in fuc:
#         a = (i.real,i.imag)
#         modified_values.append(a)
#     print(modified_values)
#     draw.point(modified_values,"black")
#     img.save("image.png")
    
    
# plot(0,50,mandelbort(0,50))   
    