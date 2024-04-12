## CUBE
#vertices = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1,1,0], [1,0,1], [0,1,1], [1,1,1]]
#P = Polyhedron(vertices=vertices)
#viewpoint = [674, 108, -731]
#angle = 30
#Img = P.tikz(viewpoint, angle, scale=2, opacity=0.4, output_type='LatexExpr')
#print(Img)

## SIMPLEX
#vertices = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, 0, 1]]
#P = Polyhedron(vertices=vertices)
#viewpoint = [674, 108, -731]
#angle = 90
#Img = P.tikz(viewpoint, angle, scale=2, opacity=0.4, output_type='LatexExpr')
#print(Img)

## PYRAMID
#vertices = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0,0,1]]
#P = Polyhedron(vertices=vertices)
#viewpoint = [674, 108, -731]
#angle = 90
#Img = P.tikz(viewpoint, angle, scale=2, opacity=0.4, output_type='LatexExpr')
#print(Img)

## BIPYRAMID
#vertices = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0,0,-1], [0,0,1]]
#P = Polyhedron(vertices=vertices)
#viewpoint = [674, 108, -731]
#angle = 90
#Img = P.tikz(viewpoint, angle, scale=2, opacity=0.4, output_type='LatexExpr')
#print(Img)

## PRISM
vertices = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [1,0,2], [-1,0,2], [0,1,2]]
P = Polyhedron(vertices=vertices)
viewpoint = [674, 108, -731]
angle = 120
Img = P.tikz(viewpoint, angle, scale=1.4, opacity=0.4, output_type='LatexExpr')
print(Img)
