# NS 1st Types of Lists Notes 
#list 
alienstage = ["Luka", "Mizi", "Sua", "Till", "Hyuna", "Ivan"]

print(alienstage[3])
alienstage[-1] = "EMO"

print(alienstage)

# tuples
fruit = ("apple", "orange", "peach", "kiwi", "raspberry")
home = (0,0)
x,y = home

#fruit[3] = pineapple
print(x)

# set
colors = {"Yellow", "Pink", "Purple", "Gray", "Brown", "Black"}
colors.add("Blue")
colors.remove("Purple")
print(colors)

for i in colors:
    if i == "Orange":
        print("fruit")
    print(i)