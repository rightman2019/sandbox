def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def answer(ns: list) -> str:

    pns = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    answer : str = ""

    for i in range(len(ns)):

        for j in range(len(pns)):

            if ns[i] % pns[j] == 0:
                answer += answerlist(pns[j]) + ", "

    return answer + "Have a Good Time!"

def answerlist(prime: int) -> str:

    match prime:
        case 2:
            return "Fuck off"
        case 3:
            return "Fuck you"
        case 5:
            return "Son of a bitch"
        case 7:
            return "Asshole"
        case 11:
            return "Dumbass"
        case 13:
            return "Bastard"
        case 17:
            return "Bullshit"
        case 19:
            return "Shithead"
        case 23:
            return "Dickhead"
        case 29:
            return "Jackass"
        case 31:
            return "Douchebag"
        case 37:
            return "Piece of shit"
        case 41:
            return "Get lost"
        case 43:
            return "Piss off"
        case 47:
            return "Screw you"
        case 53:
            return "Damn you"
        case 59:
            return "Go to hell"
        case 61:
            return "Shut the fuck up"
        case 67:
            return "What the fuck?"
        case 71:
            return "Fuck this shit"
        case 73:
            return "Fuck that"
        case 79:
            return "Eat shit"
        case 83:
            return "Kiss my ass"
        case 89:
            return "Up yours"
        case 97:
            return "Go fuck yourself"
        case _:
            return "Hello world"
