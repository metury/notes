# Define the vertices of the tetrahedron
vertices = [[2, 0, 0], [-2, 0, 0], [0, 2, 0], [0, -2, 0], [0, 0, -2], [0, 0, 2], [1,1,1], [1,1,-1], [1,-1,1], [-1,1,1], [1,-1,-1], [-1,-1,1], [-1,1,-1], [-1,-1,-1],]
P = Polyhedron(vertices=vertices)

# Obtain the viewpoint values (e.g., [674, 108, -731] and angle=112)
viewpoint = [674, 108, -731]
angle = 180

# Generate the TikZ code
Img = P.tikz(viewpoint, angle, opacity=0.4, output_type='LatexExpr')
print(Img)  # Print the TikZ code to the console
