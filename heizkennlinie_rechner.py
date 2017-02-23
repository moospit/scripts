#/usr/bin/python3


def vorlauf(soll=20, aussen=19, neigung=.6, niveau=0):
    return .55 * neigung * ((soll)**(aussen / (320 - aussen * 4))) * ((-aussen + 20) * 2) + soll + niveau

def main():
    soll = 20
    neigung = .6
    niveau = 3
    print("  +- {} | /\\ {}".format(niveau, neigung))
    print("Aussen | Vorlauf")
    for aussen in range(20,-20,-1):
        print("{:>6} | {:<6}".format(aussen, round(vorlauf(soll, aussen, neigung, niveau), 1)))


if __name__ == "__main__":
    main()
