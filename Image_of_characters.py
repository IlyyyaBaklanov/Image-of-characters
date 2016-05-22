from PIL import Image, ImageDraw

path = input('Путь до изображения:')
simvols_a = input('Символ заменяющий чёрный цвет:')
simvols_b = input('Символ заменяющий белый цвет:')
simvols_c = input('Символ заменяющий серый цвет:')
out_path = input('Путь сохранения изображения:')
image = Image.open(path) 
draw = ImageDraw.Draw(image) 
width = image.size[0] 
height = image.size[1] 	
pix = image.load()

factor = int(input('factor:'))
for j in range(height):
	for i in range(width):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = a + b + c
		if (S > (((255 + factor) // 2) * 3)):
			a, b, c = 255, 255, 255
		else:
			a, b, c = 0, 0, 0

		draw.point((i, j), (a, b, c)) 

image.save(out_path, "JPEG")
del draw

step = int(input('Шаг пикселей:'))
softnes = int(input('Мягкость:'))
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
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                color = 255
            else:
                color = 0

            color_sum += color

            r += 1
 
            if r == step:
                c_1 += 1
                r = 0
     
        if color_sum//(step**2) > (255/2+softnes):
            row_app = simvols_b
        elif color_sum//(step**2) < (255/2-softnes):
            row_app = simvols_a
        else:
            row_app = simvols_c 
        
        row += row_app
        if i == width//step-1:
            print(row)
