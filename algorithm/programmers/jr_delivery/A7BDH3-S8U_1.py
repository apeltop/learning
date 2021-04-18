from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self.name)

    def __init__(self, name: str, skills: List, load: int):
        self.name = name
        self.skills = skills
        self.load = load


class Ticket(object):
    def __init__(self, id: str, restrictions: List):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return sorted([agent for agent in agents], key=lambda x: (len(x.skills), x.load))

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if not agents:
            raise NoAgentFoundException

        return agents[0]


class LeastLoadedAgent(FinderPolicy):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return sorted(agents, key=lambda x: x.load)

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return super().find(ticket, self._filter_loaded_agents(agents))


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return super().find(ticket, [agent for agent in self._filter_loaded_agents(agents) if all(elem in agent.skills for elem in ticket.restrictions)])


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English", "Fr"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=1)
agent3 = Agent(name="C", skills=[], load=0)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, [agent1, agent2, agent3]))
# returns the Agent with name "B" because of their currently lower load.
print(least_loaded_policy.find(ticket, [agent1, agent2]))


least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
b = least_flexible_policy.find(ticket, [agent1, agent2])
print(b)
