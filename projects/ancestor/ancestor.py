from collections import deque
def earliest_ancestor(ancestors, starting_node):

#first create a graph  for relationships
    relationships = {}
    for relations in ancestors:
        parents = relations[0]
        children = relations[1]
        if children not in relationships:
            relationships[children] = set()
        relationships[children].add(parents)
    early_ancestor = - 1

#Breadth-First

    queue = deque()
    queue.append(starting_node)
    while len(queue) > 0:
        current_vertex = queue.popleft()
        if current_vertex in relationships:
            parent_lowest_id =None
            for parent in relationships[current_vertex]:
                if parent_lowest_id is None:
                    parent_lowest_id = parent
                elif parent < parent_lowest_id:
                    parent_lowest_id = parent
                queue.append(parent)
            if parent_lowest_id is not None:
                early_ancestor = parent_lowest_id
    return early_ancestor




