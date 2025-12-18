"""
B = a^x (mod p)
"""
a = 89 
B = 618
p = 809

i = 1
def steps(Z, u, v):
        mod = Z % 3
        if mod == 0:
                return ((Z*Z) % 809, (2*u)%808, (2*v)%808)
        elif mod == 1:
                return ((Z*B) % 809, u%808, (v+1)%808)
        elif mod == 2:
                return ((Z*a) % 809, (u+1) % 808, v % 808)

Zt = 1
ut = 0
vt = 0
Zh = 1
uh = 0
vh = 0

Zt, ut, vt = steps(Zt, ut, vt)

Zh1, uh1, vh1 = steps(Zh, uh, vh)
Zh, uh, vh = steps(Zh1, uh1, vh1)

print(f"{i}.\n\tHare:\n\t\tZ={Zh1},u={uh1},v={vh1}\n\t\tZ={Zh},u={uh},v={vh}\n\tTortoise:\n\t\tZ={Zt},u={ut},v={vt}")
i+=1
while(Zh != Zt):
        Zt, ut, vt = steps(Zt, ut, vt)

        Zh1, uh1, vh1 = steps(Zh, uh, vh)
        Zh, uh, vh = steps(Zh1, uh1, vh1)



        print(f"{i}.\n\tHare:\n\t\tZ={Zh1},u={uh1},v={vh1}\n\t\tZ={Zh},u={uh},v={vh}\n\tTortoise:\n\t\tZ={Zt},u={ut},v={vt}")
        i += 1
