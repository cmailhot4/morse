from gpiozero import LED
from time import sleep
import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

mot = input("Entrez le texte: ")
liste = []
compteur = 0
nbCharactere = 0

for charactere in mot:
	liste.append(charactere)
	nbCharactere+=1

while compteur < nbCharactere:
	if liste[compteur]=="a":
		a.run()
	elif liste[compteur]=="b":
		b.run()
	elif liste[compteur]=="c":
        	c.run()
	elif liste[compteur]=="d":
        	d.run()
	elif liste[compteur]=="e":
        	e.run()
	elif liste[compteur]=="f":
        	f.run()
	elif liste[compteur]=="g":
		g.run()
	elif liste[compteur]=="h":
		h.run()
	elif liste[compteur]=="i":
		i.run()
	elif liste[compteur]=="j":
		j.run()
	elif liste[compteur]=="k":
		k.run()
	elif liste[compteur]=="l":
		l.run()
	elif liste[compteur]=="m":
		m.run()
	elif liste[compteur]=="n":
		n.run()
	elif liste[compteur]=="o":
		o.run()
	elif liste[compteur]=="p":
		p.run()
	elif liste[compteur]=="q":
		q.run()
	elif liste[compteur]=="r":
		r.run()
	elif liste[compteur]=="s":
		s.run()
	elif liste[compteur]=="t":
		t.run()
	elif liste[compteur]=="u":
		u.run()
	elif liste[compteur]=="v":
		v.run()
	elif liste[compteur]=="w":
		w.run()
	elif liste[compteur]=="x":
		x.run()
	elif liste[compteur]=="y":
		y.run()
	elif liste[compteur]=="z":
		z.run()
	elif liste[compteur]==" ":
		sleep(4)
	compteur+=1
