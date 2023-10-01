name = input("Enter name: ")

match name:
    case "Ahmad" | "Alam" | "Khan":
        print("Mardan")
    case "Ali":
        print("Dargai")
    case "Wali":
        print("Dir")
    case _:
        print("Who")
