from env import Env
from MapLoader import ChallengeDesigner
from gui import GUI
from ai import Agent


def ask_user():
    # mapLoadType=input("load or create? (l/c) ")
    # if mapLoadType=="c": return "create", int(input("height? "))+2, int(input("width? "))+2
    # if mapLoadType=="l": return "load"
    return "create", 12, 22


if __name__ == "__main__":
    initial_Map = ChallengeDesigner()
    sim = Env(initial_Map.run(*ask_user()))
    agent = Agent(sim.send_map)
    gui = GUI(cubeSize=20, delay=10, state=sim.state)

    while not (sim.goal_test()):
        gui.redrawPage(sim.state)

        action = agent.act()
        while sim.state.validate_action(action) is False:
            if len(action)==3: action = agent.act()

        sim.take_action(action)
        print("successful action")

    print("победа!!!")
