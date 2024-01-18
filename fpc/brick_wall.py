#!/usr/bin/env python3

""" =Initialize=all=values======================== """
k = 4
colors = ["orange", "VioletRed", "blue", "Green", "cyan"]
""" ============================================== """


def create_header():
	print("""\\begin{figure}[!ht]\\centering
	\\begin{tikzpicture}[node distance={9mm}, main/.style = {draw, circle}]""")

def create_footer():
	print("""	\\end{tikzpicture}
	\\caption{Example of a \\textbf{brick wall} graph.}
	\\label{brick-wall}
\\end{figure}""")

def create_graph(k):
	""" Create a graph in tikzpicture. """
	print("\\node[main] (0) {$s_{1}$};")
	for i in range(2*k - 2): # Create first bricks.
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
	for i in range(2*k-1): # Create middle bricks.
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
	last=(2*k)*10 + 1 # Create last bricks.
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

def straight_path(x, k, s):
	""" Straight path from x to bottom. """
	for i in range(s):
		print()
		print(f"\t({x + i * 10}) edge ({x + (i + 1) * 10})", end="")

def rec_path(x, k, s):
	""" Recusrive path zig-zag. """
	if x // 10 == 2*k:
		return
	print()
	if x % 10 == 2 * k - 1:
		for i in range(s + 1):
			print(f"\t({x - i}) edge ({x - i -1})")
		print(f"\t({x - s - 1}) edge ({x - s - 1 + 10})", end="")
		straight_path(x - s - 1 + 10, k, s);
	else:
		print(f"\t({x}) edge ({x + 1})")
		print(f"\t({x + 1}) edge ({x + 11})", end="")
		rec_path(x+11, k, s)

def create_path(x, k, s, color):
	""" Create a path from x. """
	print(f"\\path[color={color}, thick] ({x}) edge ({x+10})")
	print(f"\t({x+10}) edge ({x+11})")
	print(f"\t({x+11}) edge ({x+21})", end="")
	rec_path(x+21, k, s)
	print(";")

def create_flow(k):
	""" Create all paths with. """
	for i in range(k):
		create_path(2*i, k, 2*i-1, colors[i])

""" Create only a graph. """
#create_header()
#create_graph(k)
#create_footer()

""" Create also one path. """
#create_header()
#create_graph(k)
#create_path(0, k, 0, "blue")
#create_footer()

""" Create the flow. """
create_header()
create_graph(k)
create_flow(k)
create_footer()

