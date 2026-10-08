def calcul():
    try:
        nb1 = float(input("Nombre 1 : "))
        nb2 = float(input("Nombre 2 : "))
    except ValueError:
        print("Veuillez entrer un nombre valide")
        return

    operation = input("Operation (+, -, *, /) : ")
    match operation:
        case "+":
            result = nb1 + nb2
        case "-":
            result = nb1 - nb2
        case "*":
            result = nb1 * nb2
        case "/":
            if nb2 == 0:
                print("Division par 0 impossible")
                return
            result = nb1 / nb2
        case _:
            print("Opération invalide")
            return

    print(f"{nb1:g} {operation} {nb2:g} = {round(result,3):g}")

calcul()
