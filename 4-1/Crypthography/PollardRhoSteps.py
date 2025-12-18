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
                return ((Z*Z) % p, (2*u)%(p-1), (2*v)%(p-1))
        elif mod == 1:
                return ((Z*B) % p, u%(p-1), (v+1)%(p-1))
        elif mod == 2:
                return ((Z*a) % p, (u+1) % (p-1), v % (p-1))

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
