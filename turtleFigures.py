import turtle
import math

# 0.TREE
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2,pen)
     pen.right(90)
     tree(n-1, l/2,pen)
     pen.left(45)
     pen.backward(l)

# END TREE

# 1.DANDELION
def dandelion(n, l, pen):
    if n == 0 or l < 2:
        return
    #endif
    pen.forward(l)
    pen.left(90)
    dandelion(n-1, l/2, pen)
    pen.right(60)
    dandelion(n-1, l/2, pen)
    pen.right(60)
    dandelion(n-1, l/2, pen)
    pen.right(60)
    dandelion(n-1, l/2, pen)
    pen.left(90)
    pen.backward(l)
# END DANDELION

# 2.FERN
def fern(n,l,pen):
     if n == 0 or l < 2:
          return
     #endif
     pen.forward(0.3*l)
     pen.left(45)
     fern(n-1, 0.4*l, pen)
     pen.right(45)
     pen.forward(0.7*l)
     pen.right(30)
     fern(n-1, 0.5*l, pen)
     pen.left(30)
     pen.forward(l)
     pen.right(15)
     fern(n-1, 0.7*l, pen)
     pen.left(15)
     pen.backward(2*l)
# END FERN

# 3.KOCH
def koch(n,l,pen):
     if n == 0 or l <2:
          pen.forward(l)
          return
     #endif
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
     pen.right(120)
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
# END KOCH

# 4.FLAKE
def flake(n,l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.right(120)
     #endfor
# END FLAKE

# 5.ANTI-FLAKE
def antiflake(n,l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.left(120)
     #endfor
# END ANTI-FLAKE

# 6.SIERPINSKY GASKET
def sperpinskyGasket(n, l, pen):
     # draw a triangle
     if n==0 or l<2 :
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          return
     # for each triangle
     for i in range(3):
          sperpinskyGasket(n-1, l/2, pen)
          pen.forward(l)
          pen.left(120)
#end triangleGasket

#squre gasket
def squreGasket(n, l, pen):
     #draw a square
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          return

     #for each square
     for i in range(4):
          squreGasket(n-1, l/3, pen)
          pen.forward(l)
          pen.left(90)
#end squreGasket

# CIRCLE GASKET
def circleGasket(n, l, pen):
     if n == 0 or l < 2:
          return
     # end if
     pen.circle(l)
     for i in range(4):
          circleGasket(n-1, l/2, pen)
          pen.down()
          pen.circle(l)
          pen.up()
          pen.forward(l)
          pen.left(90)
          pen.forward(l)
     #end for
     
#end circleGasket

def new1(n, l, pen):
     if n==0 or l<2 :
          return
     #endif

     for i in range(4):
          new1(n-1, l/2, pen)

          
          
          pen.forward(l)
          pen.left(90)
     
          pen.forward(l)
          pen.right(90)
     
          pen.forward(l)
          pen.left(90)

#end circleGasket

# MIX GASKET
def mixGasket(n, l, pen):
     if n == 0 or l < 2:
          return
     # end if
     pen.circle(l)
     for i in range(4):
          mixGasket(n-1, l/2, pen)
          pen.circle(l)
          pen.forward(l)
          pen.left(90)
          pen.forward(l)
     #end for
     
#end mixGasket


