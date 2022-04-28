hydrogen = 1.008
helium = 4.0026
lithium = 6.94
atomic_weight = input("element: ")

if atomic_weight.lower() == 'hydrogen':
    print(hydrogen)
elif atomic_weight.lower() == 'helium':
    print(helium)
elif atomic_weight.lower() == 'lithium':
    print(lithium)
else:
    print("Sorry, I don't recognize that element!")