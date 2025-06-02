# Simple swarm agent communication simulation
def agent_communication():
    agents = ["Agent A", "Agent B", "Agent C"]
    message = "Target located!"

    for agent in agents:
        print(f"{agent} received message: '{message}' and is taking action.")

if __name__ == "__main__":
    agent_communication()