p1 = p2 = 100000
m1 = m2 = p1
r1 = 0.1
r2 = 0.05
n = 0
while m2 <= m1:
    n += 1
    m1 = m1 + p1 * r1 
    m2 = m2 * ( 1 + r2 )
    if m2 > m1:
        print('錢精打的', p1, '元在第', n, '年時有', m1, '元')
        print('郝細算的', p2, '元在第', n, '年時有', m2, '元')