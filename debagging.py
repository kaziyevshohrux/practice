"""
1_) python packages & core Package
2_) Package manager & External Package
3_) debugging
"""
 
#print('=========== python packages and cor packages')

""" puyhpon Packages/modules: Core , File , and External"""

# core packeges    https://docs.python.org/3/library

# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(6)
# t.circle(100)
# turtle.done()


print('==----------==')

my_file = open("material/massage.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()



# with context manager hisoblanadi 

with open("material/massage.txt", "r") as your_file:
    your_file = your_file.read()
    print(your_file)
print('done')


print('=====external packages=======')

# core packages pytondi ozi bilan keladi 

# external packages ladi install qilishimiz kerak boladi 

# external   ->    https://pypi.org/ 


from PIL import Image

with Image.open("material/egpt.jpg") as img_obj:
   resize_img= img_obj.resize((200,200))
   resize_img.show()
   resize_img.save("material/sample.jpg")