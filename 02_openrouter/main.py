# simple agent project with two agents communicating

class Agent:
    def __init__(self, name):
        self.name = name

# Method to send a hello message to another agent
    def send_hello(self, other_agent):
        print(f"{self.name} says: Hello {other_agent.name}!")
        other_agent.reply_hello(self)

# Method to reply to a hello message
    def reply_hello(self, sender_agent):
        print(f"{self.name} replies: Hello to you too, {sender_agent.name}!")

# Main code
if __name__ == "__main__":
    agent1 = Agent("Agent_1")   # Create an instance of Agent_1
    agent2 = Agent("Agent_2")   # Create an instance of Agent_2

    agent1.send_hello(agent2)  # Agent_1 sends a hello message to Agent_2