def sort_input(mat):
    # este codigo va a ordenar una matriz
    mat.sort()
    print mat


def random_sort(n):
    import random
    mat = []
    for i in range(1, n):
        mat.append(random.randrange(1, 100,1))

    print mat



