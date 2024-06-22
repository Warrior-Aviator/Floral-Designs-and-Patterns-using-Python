import time
from turtle import *
from random import *
dis    = 100      ; dismod = (2/3,3/4,3/5,7/8)       ; c = 2      ; d = 5
ang    = 45       ; a = 20   ; b = 30  ; minpix = 5  ; siz = 10   ; wmod = 2/5
w = Screen()      ; w.bgcolor("white") ; w.tracer(0) ; w.setup(800, 200000, 600, 0)
t = Turtle()      ; t.color  ("black") ; t.lt(90)    ; t.speed(0) ; t.shape("triangle")
t.pu()            ; t.bk(305)          ; t.pd()      ; t.ht()     ; t.shapesize(4)
def tree(x,y,s)   :
    zzz = s*wmod  ; zz = randint(a,b)  ; z  = choice(dismod)*x  
    t.width(s)    ; t.fd(x) ; t.lt(y)
    if z > minpix : tree(z,zz,zzz) #LEFT   BRANCHING
    t.rt(2*y) 
    if z > minpix : tree(z,zz,zzz) #RIGHT  BRANCHING
    t.lt(y)
    if z > minpix : tree(z*1.01,zz,zzz) #CENTER BRANCHING
    t.bk(x)       ;     w.update()

while True :
    ang = randint(20,45) ; dis = randint(90,105)
    t.stamp() ; tree(dis,ang,siz) ; t.clear() ; time.sleep(4)
    



