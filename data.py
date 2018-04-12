from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y')
pyDatalog.create_terms('plasticContainer,paperContainer,glassContainer,mixedContainer')  # types of containers
pyDatalog.create_terms('plastic,glass,paper')  # material by which we segregate

pyDatalog.create_terms('trash')  # type of item
pyDatalog.create_terms('color,elastic,fragile,white')  # properties

# conditions
glass(X) <= (trash[X]==1) & (color[X]==0) & (fragile[X]>0.5)
plastic(X) <= (trash[X]==1) & (color[X]==1) & (elastic[X]>0.8)
paper(X) <= (trash[X]==1) & (white[X]>0.5)

# segregation
glassContainer(X) <= glass(X)
plasticContainer(X) <= plastic(X)
paperContainer(X) <= paper(X)

# example trash
# glass
trash['trash1'] = 1
color['trash1'] = 0
fragile['trash1'] = 0.8

trash['trash2'] = 1
color['trash2'] = 0
fragile['trash2'] = 0.9

trash['trash3'] = 1
color['trash3'] = 0
fragile['trash3'] = 0.7

# plastic
trash['trash4'] = 1
color['trash4'] = 1
elastic['trash4'] = 1

# paper
trash['trash5']=1
white['trash5']=0.8

# prints all trash in glass container
print(glassContainer(X))

# prints all trash that are paper
print(paper(X))
