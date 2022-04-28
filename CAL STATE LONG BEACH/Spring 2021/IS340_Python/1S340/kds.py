hydrogen = 1.008
helium = 4.0026
lithium = 6.94
atomic_weight = input("Enter element name: ").lower()

if atomic_weight == 'hydrogen':
    print(hydrogen)
elif atomic_weight == 'helium':
    print(helium)
elif atomic_weight == 'lithium':
    print(lithium)
else:
    print("Sorry, I don't recognize that element!")
