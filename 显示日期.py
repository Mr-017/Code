# 实践：显示时间
import turtle, time

def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
    
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
            turtle.pencolor("purple")
            turtle.left(180)
            turtle.fd(750)
            turtle.right(90)
            turtle.fd(100)
            turtle.write('选择了就要坚持,坚持了就要坚持到底\n因为年轻，所以选择了奋斗，你要记住，你是一个奋斗的青年', font=("Bradley Hand ITC", 20, "bold"))
        else:
            drawDigit(eval(i))
            
def main():
    turtle.setup(1000, 400, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
#    drawDate('2018-10=10+')
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()
