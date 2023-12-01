#!/usr/bin/env python3

k = 4

print("\\node[main] (0) {$s_{1}$};")

for i in range(2*k - 2):
	if i % 2 == 1:
		print(f"\\node[main] ({i+1}) [right of={i}]", end =" ")
		print("{$s_{" ,end ="")
		print((i // 2) + 2, end="")
		print("}$};")
	else:
		print(f"\\node[main] ({i+1}) [right of={i}]", end =" ")
		print("{};")
	print(f"\\draw ({i}) -- ({i+1});")

odd = False

for i in range(2*k-1):
	print(f"\\node[main] ({(i+1)*10}) [below of={i*10}]", end =" ")
	print("{};")
	if not odd:
		print(f"\\draw ({(i+1)*10}) -- ({i*10});")
	for j in range(2*k - 1):
		print(f"\\node[main] ({(i+1)*10 + j + 1}) [right of={(i+1)*10 + j}]", end =" ")
		print("{};")
		print(f"\\draw ({(i+1)*10 + j + 1}) -- ({(i+1)*10 + j});")
		if j != 2*k - 2 or odd:
			print(f"\\draw ({(i+1)*10 + j + 1}) -- ({i*10 + j + 1});")
	odd = not odd

last=(2*k)*10 + 1

print(f"\\node[main] ({last}) [below of={last - 10}]", end=" ")
print("{$t_{", end="")
print(k, end="")
print("}$};")

for i in range(2*k - 2):
	if i % 2 == 1:
		print(f"\\node[main] ({last+i+1}) [right of={last+i}]", end =" ")
		print("{$t_{" ,end ="")
		print(k - (i // 2) - 1, end="")
		print("}$};")
	else:
		print(f"\\node[main] ({last+i+1}) [right of={last+i}]", end =" ")
		print("{};")
	print(f"\\draw ({last+i+1}) -- ({last+i});")
	print(f"\\draw ({last+i}) -- ({last - 10 + i});")

print(f"\\draw ({last+(2*k - 2)-10}) -- ({last+(2*k - 2)});")


print("\path[color=cyan] (0) edge (10)", end="")
add=0
for i in range(2*k):
	print()
	if i != 2*k - 1:
		print(f"\t({(i+1)*10 + add}) edge ({(i+1)*10 + 1 + add})")
	print(f"\t({i*10 + add}) edge ({(i+1)*10 + add})", end="")
	add += 1
print(";")
