import colorgram,random, turtle as tt
rgb_colors=[]
tt.colormode(255)

colors =colorgram.extract("D:/100 Days Of Python/DAY 18/hirst_image.jpeg",30)
for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
filtered_colors = [(205, 161, 83), (56, 88, 129), (144, 91, 42), (220, 207, 109), (137, 27, 48), 
                   (135, 175, 200), (155, 48, 85), (45, 55, 103), (131, 188, 145), 
                   (82, 20, 41), (190, 139, 161), (36, 43, 68), (184, 94, 107), (88, 122, 177), 
                   (59, 39, 32), (88, 156, 96), (80, 152, 164), (193, 82, 73), (161, 202, 217), 
                   (78, 75, 44), (44, 75, 72), (56, 126, 118), (218, 175, 189), (46, 74, 76), 
                   (161, 208, 157)]
tim = tt.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(101):
    tim.pendown()
    tim.dot(20,random.choice(filtered_colors))
    tim.penup()
    tim.forward(50)
    
    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
sc= tt.Screen()
sc.exitonclick()