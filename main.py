from LittleManComputer import LittleManComputer
from time import sleep


def main():
    lmc = LittleManComputer()

    lmc.write(0, 510)
    lmc.write(1, 313)
    lmc.write(2, 513)
    lmc.write(3, 922)
    lmc.write(4, 111)
    lmc.write(5, 313)
    lmc.write(6, 212)
    lmc.write(7, 709)
    lmc.write(8, 602)
    lmc.write(9, 000)
    lmc.write(10, 32)
    lmc.write(11, 1)
    lmc.write(12, 127)

    ext = False
    lmc.display()
    while not ext:
        # input("Press ENTER to step")
        sleep(0.1)
        ext = lmc.excecute()
        lmc.display()


if __name__ == "__main__":
    main()
