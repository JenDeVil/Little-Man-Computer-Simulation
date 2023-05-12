import os
from LittleManComputer import LittleManComputer
from time import sleep


def selectProgram(direc):
    programs = []
    for file in os.scandir(direc):
        filename, fileext = os.path.splitext(file)
        if file.is_file() and fileext == ".lmc":
            programs.append(filename.split("\\")[-1])

    os.system("cls")
    print("Please select a program to run")
    for i in range(len(programs)):
        print(str(i + 1) + ". " + programs[i])

    return direc + "/" + programs[int(input(">| ")) - 1] + ".lmc"


def getStepType():
    options = ["Step-by-step", "Micro step-by-step", "Auto step", "Auto micro-step", "Auto step fast",
               "Auto micro-step fast"]

    os.system("cls")
    print("Welcome to Ms. Universe's Little Woman Computer Simulation\n"
          "How do you want the simulation to run?")
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])
    
    return options[int(input(">| ")) - 1]


def main():
    lmc = LittleManComputer()

    # Select a program from the Program directory
    lmc.decode_from_file(selectProgram("Programs"))

    # Get the user to choose a step type
    inp = getStepType()

    # Ask for a wait time if they chose a step type that requires one
    wait = None
    if inp in ["Auto step", "Auto micro-step"]:
        wait = float(input("Enter wait time between steps (seconds) "))

    # Draw the first frame of the memory before the cycle starts
    ext = False
    os.system("cls")
    lmc.draw_frame()

    # Perform the cycle until it exits
    while not ext:
        if inp == "Micro step-by-step":
            ext = lmc.excecute(True)

        elif inp == "Step-by-step":
            input("Press ENTER to step")
            ext = lmc.excecute()
            lmc.draw_frame()

        elif inp == "Auto step":
            ext = lmc.excecute()
            lmc.draw_frame()
            sleep(wait)

        elif inp == "Auto micro-step":
            ext = lmc.excecute(True, wait)

        elif inp == "Auto step fast":
            ext = lmc.excecute()
            lmc.draw_frame()

        elif inp == "Auto micro-step fast":
            ext = lmc.excecute(True, 0)
            lmc.draw_frame()

        else:
            print(inp + " is not supported yet")
            break
    print("Program successfully halted")


if __name__ == "__main__":
    main()
