__author__ = 'HP'
# Este es el juego, empezamos con un n>1, y el objetivo es encontrar el numero de pasos que se necesita para que n llegue a 1
def collantz(n):
    contador = 0
    if n != 1:
        while n > 1:
            if n % 2 == 0:
                print "paso numero ", contador
                print "n=", n
                n = n/2
                n = int(n)
                contador = contador + 1

            else:
                print "paso numero ", contador
                print "n=", n
                n = n*3 + 1
                n = int(n)
                contador = contador + 1
            if contador > 1500:
                print "mala suerte, duro mucho pensando"
                break
            if n == 1:
                print "Felicitaciones, tomo", contador, "pasos llegar a 1"

    else:

        print "Di un numer mayor que 1, porfavor"
        return
collantz(1
