space = "<{:>49}"
title = "<{:>25} {:>23}"
optionA = "<{:^8}Option a {:>32}"
optionB = "<{:^8}Option b {:>32}"
optionC = "<{:^8}Option c {:>32}"

print("^"*50)
print(space.format(">"))
print(space.format(">"))
print(space.format(">"))
print(title.format("Title",">"))
print(space.format(">"))
print(space.format(">"))
print(optionA.format("A",">"))
print(optionB.format("B",">"))
print(optionC.format("C",">"))
print(space.format(">"))
print(space.format(">"))
print("v"*50)