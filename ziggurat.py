from tkinter import*
side = int(input())

root = Tk()
root.title('Зиккурат')
root.resizable(False, False)

zic    = []
rg     = range(1, side+1)
last   = side+1
center = (side+1)//2

for y in rg:
    row = []
    for x in rg:
        if x < y:
            if y > last-x:
                row.append(last-y)
            else:
                row.append(x)
        elif y < x:
            if x > last-y:
                row.append(last-x)
            else:
                row.append(y)
        elif y == x:
            if y > center or x > center:
                row.append(last-x)
            else:
                row.append(x)
        
    zic.append(row)

cell_size = 30
colors = ['red'   , 'orange', 'yellow',
          'green' , 'aqua'  , 'blue',
          'purple', 'black' , 'gray',
          'silver', 'white' , 'pink']
for i in range(len(zic)):
    for j in range(len(row)):
        num = zic[j][i]
        b = Button(root, bg = colors[num-1], text = num)
        b.place(width  = cell_size,
                height = cell_size,
                x = j*cell_size,
                y = i*cell_size)

for i in zic:
    print(i)

root.update_idletasks()

width_root  = cell_size*(last-1)
height_root = cell_size*(last-1)
     
w = (root.winfo_screenwidth()  // 2) - (width_root  // 2)
h = (root.winfo_screenheight() // 2) - (height_root // 2)

root.geometry('{}x{}+{}+{}'.format(width_root, height_root, w, h))
root.mainloop()
