from math import hypot

square = [(1,1), (1,2), (2,2), (2,1)] # Polygon = List[Point]

def distance(p_1, p_2):
    return hypot(p_1[0]-p_2[0], p_1[1]-p_2[1])

def perimeter(polygon):
    pairs = zip(polygon, polygon[1:] + polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)


#%%
print (square)
print(square[0])
print(square[1])

#%%
print(distance(square[0],square[3]))

#%%
pairs = zip(square, square[1:] + square[:1])
print(pairs)
type(pairs) # es un obj zip
print (square[1:])
print (square[:1])

print(square[1:] + square[:1])

# con esto pasa el primero a la ultima posicion.
# print(square[1:] + square[:1])
# [(1, 2), (2, 2), (2, 1), (1, 1)]
# entonces es un zip de:
# [(1,1), (1,2), (2,2), (2,1)] y [(1, 2), (2, 2), (2, 1), (1, 1)]

for num1,num2 in pairs:
    print (num1,num2)

#%%
perimeter(square)
