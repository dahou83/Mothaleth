from numpy import *
# bouth ways corect .
'''motheleth = array ([
             [4 , 9 , 2] ,
            [3 , 5 , 7] ,
              [8 , 1 , 6]
             ])'''
motheleth = matrix(' 4 9 2 ; 3 5 7 ; 8 1 6 ')
print (motheleth)
i = int(input("inter the number "))
k =   i - 12
if k % 3 == 0 :
    o = k / 3
    a = motheleth [2,1] = o
    b = motheleth [0,2] = a+1
    c = motheleth [1,0] = b+1
    d = motheleth [0,0] = c+1
    e = motheleth [1,1] = d+1
    f = motheleth [2,2] = e+1
    g = motheleth [1,2] = f+1
    h = motheleth [2,0] = g+1
    j = motheleth [0,1] = h+1
    print(motheleth)
elif k % 3 ==1 :
    o = k // 3
    r1 = k % 3
    a = motheleth[2, 1] = o
    b = motheleth[0, 2] = a + 1
    c = motheleth[1, 0] = b + 1
    d = motheleth[0, 0] = c + 1
    e = motheleth[1, 1] = d + 1
    f = motheleth[2, 2] = e + 1
    g = motheleth[1, 2] = f + 1 + r1
    h = motheleth[2, 0] = g + 1
    j = motheleth[0, 1] = h + 1
    print(motheleth )
    print ("jaber 1")
elif k % 3 == 2 :
    o = k // 3
    r2 = k % 3
    a = motheleth[2, 1] = o
    b = motheleth[0, 2] = a + 1
    c = motheleth[1, 0] = b + 1
    d = motheleth[0, 0] = c + 1 + r2
    e = motheleth[1, 1] = d + 1
    f = motheleth[2, 2] = e + 1
    g = motheleth[1, 2] = f + 1
    h = motheleth[2, 0] = g + 1
    j = motheleth[0, 1] = h + 1
    print (motheleth )
    print (" jaber 2")
