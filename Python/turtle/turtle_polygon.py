import turtle 
  
t = turtle.Turtle() 
  
n = int(input("Inserisci numero di lati: ")) 
  
l = int(input("Inserisci lunghezza lati: ")) 
  
for _ in range(n): 
    turtle.forward(l) 
    turtle.right(360 / n) 

turtle.done()
