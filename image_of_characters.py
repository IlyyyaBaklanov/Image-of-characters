from PIL import Image, ImageDraw

path = input('Путь до изображения:')
simvols_a = input('Символ заменяющий чёрный цвет:')
simvols_b = input('Символ заменяющий белый цвет:')
shades = int(input('Количество оттенков'))
simvols_c = [input('Символы оттенков серого светлые --> темные') for i in range(shades-2)]
out_path = input('Путь сохранения изображения:')
image = Image.open(path) 
draw = ImageDraw.Draw(image) 
width = image.size[0] 
height = image.size[1] 	
pix = image.load()

for j in range(height):
	for i in range(width):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = (a + b + c)//3
		draw.point((i, j), (S, S, S)) 

image.save(out_path, "JPEG")
del draw
step = int(input('Шаг пикселей:'))
for j in range(height//step):
    row = ''
    for i in range(width//step):
        c_1 = 0
        r = 0
        color_sum = 0 
        for k in range(step*step):
            a = pix[r+i*step, c_1+j*step][0]
            b = pix[r+i*step, c_1+j*step][1]
            c = pix[r+i*step, c_1+j*step][2]
            S = (a + b + c)//3

            color_sum += S

            r += 1
 
            if r == step:
                c_1 += 1
                r = 0
     
        if color_sum//(step**2) > ((255/shades)*(shades-1)):
            row_app = simvols_b
        elif color_sum//(step**2) < (255/shades):
            row_app = simvols_a
        else:
            count = 2
            for n in range(shades-2):
                if color_sum//(step**2) > ((255/shades)*(shades-count)):
                    row_app = simvols_c[count-2]
                    break
                else:
                   count += 1 
        
        row += row_app
        if i == width//step-1:
            print(row)
        
    
