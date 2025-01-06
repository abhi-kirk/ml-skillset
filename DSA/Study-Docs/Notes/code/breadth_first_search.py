from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def get_seller(my_graph):
    search_queue = deque()
    search_queue += my_graph['you']
    people_searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person) and person not in people_searched:
            return person
        else:
            people_searched.append(person)
            search_queue += my_graph[person]
    return "None"

def person_is_seller(name):
    return name[-1] == 'm'

print(get_seller(graph))