from PIL import Image, ImageDraw

width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

draw.rectangle([(0, 0), (width, height // 2)], fill='skyblue') # небо

draw.rectangle([(0, height // 2), (width, height)], fill='green') # земля

def draw_cloud(x, y):
    draw.ellipse([(x, y), (x + 50, y + 20)], fill='white')
    draw.ellipse([(x + 20, y - 10), (x + 70, y + 10)], fill='white')
    draw.ellipse([(x + 40, y), (x + 90, y + 20)], fill='white')

draw_cloud(100, 50)
draw_cloud(300, 70)
draw_cloud(500, 60)

def draw_house(x, y):
    draw.rectangle([(x, y), (x + 100, y + 80)], fill='brown') # основание дома
    draw.polygon([(x, y), (x + 100, y), (x + 50, y - 50)], fill='red') # крыша
    draw.rectangle([(x + 30, y + 40), (x + 70, y + 80)], fill='black') # дверь

draw_house(100, 350)

def draw_grass(x, y):
    draw.line([(x, y), (x - 5, y - 15)], fill='darkgreen', width=2)
    draw.line([(x, y), (x + 5, y - 15)], fill='darkgreen', width=2)

for i in range(0, width, 20):
    draw_grass(i, height // 2)

def draw_car(x, y):
    draw.rectangle([(x, y), (x + 80, y + 30)], fill='blue') # нижний прямоугольник
    draw.rectangle([(x + 20, y - 10), (x + 60, y)], fill='blue') # верхний прямоугольник
    draw.ellipse([(x + 10, y + 25), (x + 30, y + 45)], fill='black') # колеса
    draw.ellipse([(x + 50, y + 25), (x + 70, y + 45)], fill='black')

draw_car(600, 400)

def draw_gryadki(x, y):
    draw.rectangle([(x, y), (x + 120, y + 25)], fill='brown')
    draw.rectangle([(x, y + 40), (x + 120, y + 65)], fill='brown')

draw_gryadki(400, 450)

def draw_person(x, y):
    draw.line([(x, y), (x, y + 30)], fill='black', width=2) # тело
    draw.ellipse([(x - 15, y - 30), (x + 15, y)], fill='white', outline='black') # голова
    draw.line([(x - 15, y + 15), (x + 15, y + 15)], fill='black', width=2) # руки
    draw.line([(x, y + 30), (x - 15, y + 45)], fill='black', width=2) # ноги
    draw.line([(x, y + 30), (x + 15, y + 45)], fill='black', width=2)

draw_person(200, 450)

image.show()