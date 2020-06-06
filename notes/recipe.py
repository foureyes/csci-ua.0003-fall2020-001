'''
double ingredients and write to file

alot_of_food.txt
'''
fr = open('food.txt', 'r')
fw = open('alot_of_food.txt', 'w')

# loop and extract parts
for line in fr:
    parts = [ele.strip() for ele in line.split(':')]
    qty, name = parts
    qty = int(qty)
    fw.write(f'{qty * 2} {name}\n')

fr.close()
fw.close()
