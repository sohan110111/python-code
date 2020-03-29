import turtle

def square() :
     turtle.forward(100)
     turtle.right(90)
     turtle.forward(100)
     turtle.right(90)
     turtle.forward(100)
     turtle.right(90)
     turtle.forward(100)

elephant_weight = 3000
ant_weight = 0.9
# print(3000 > .9)

if elephant_weight > ant_weight :
   # print("elephant_weight is bigger than ant_weight")
   square()

# boolean check
if True :
     square()


if elephant_weight < ant_weight :
     square()
else :
     turtle.forward(100)


    



