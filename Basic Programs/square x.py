from PIL import Image,ImageDraw

width = 1000
height = 1000
img = Image.new("RGB",(width,height),(100,100,100))
draw = ImageDraw.Draw(img)

x,y = 0,0
# fuc = x**2
points = []
for x in range(-200,200):
    y = (3**x)
    points.append(x+500)
    points.append(y)

draw.line(points,fill="red",width=1,joint="curve")
flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
flipped_img.save("image_sq.png")
Image.open("image_sq.png",)
# print(points)