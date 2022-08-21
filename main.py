import pydot
import missinaries_cannibals as State
    
class Node:
    def __init__(self, value,parent):
        self.value = value
        self.parent = parent
    
    def children_generate(self,li):
        children = []  
        if self.value.is_boat_left:
            for choice in self.value.choices:
                children.append(Node(self.value.move_left_2_right(*choice,li), self))
        else:
            for choice in self.value.choices:
                children.append(Node(self.value.move_right_2_left(*choice,li), self))
        return children

def generate(node_to_expand,li):
    nodes = node_to_expand.children_generate(li)
    print('Parent', node_to_expand.value)

    for node in nodes:
        if node.value.status == 'valid':
            li.append(node.value)
        
    for node in nodes:
        print(node.value)
        
        my_node=pydot.Node(str(node.value)+str(node.parent.value),label=str(node.value))
        my_node.add_style('filled')
        my_node.set_fillcolor(generate_color(node))
        graph.add_node(my_node)
        if node.parent.parent:
            my_edge = pydot.Edge(str(node.parent.value)+str(node.parent.parent.value), str(node.value)+str(node.parent.value), color='deepskyblue', \
                label = str((abs(node.parent.value.right_missinaries-node.value.right_missinaries), abs(node.parent.value.right_cannibals - node.value.right_cannibals))))
            graph.add_edge(my_edge)
        elif node.parent:
            my_edge = pydot.Edge('root', str(node.value)+str(node.parent.value), color='deepskyblue', \
                label = str((abs(node.parent.value.right_missinaries-node.value.right_missinaries), abs(node.parent.value.right_cannibals - node.value.right_cannibals))))
            graph.add_edge(my_edge)


    for node in nodes:
        if node.value.status == 'valid':
            generate(node, li)



def generate_color(node):
    if node.value.status == 'valid':
        return 'lightgreen'
    elif node.value.status == 'dead':
        return 'lightcoral'
    elif node.value.status == 'already':
        return 'lightyellow'
    else:
        return 'green'

   
def draw_legend(graph):
    graphname = pydot.Cluster(graph_name="name", label="Name", fontsize="20", color="red",\
                                fontcolor="blue", style="filled", fillcolor="white")
    legend1 = pydot.Node('Bishal Joshi', shape="plaintext", fontsize ='30')
    graphname.add_node(legend1)
    graph.add_subgraph(graphname)

    graphlegend = pydot.Cluster(graph_name="legend", label="Legend", fontsize="20", color="black",\
                                fontcolor="blue", style="filled", fillcolor="white")

    legend1 = pydot.Node('Processed node', shape="plaintext")
    graphlegend.add_node(legend1)
    legend2 = pydot.Node("Killed Node", shape="plaintext")
    graphlegend.add_node(legend2)
    legend3 = pydot.Node('Already processed node', shape="plaintext")
    graphlegend.add_node(legend3)
    legend4 = pydot.Node('Goal Node', shape="plaintext")
    graphlegend.add_node(legend4)
    legend5=pydot.Node('Node x,y,z=> x,y = No. of missionaries and cannibals at right shore\n'
                       '               If z=1 -> boat at left shore\n'
                       '               If z=0-> boat at right shore\n'
                       'Edge x,y=> Move x missionaries and y cannibals to opposite shore' , shape="plaintext",fontsize="15")
    graphlegend.add_node(legend5)

    node1 = pydot.Node("1", style="filled", fillcolor="lightgreen", label="")
    graphlegend.add_node(node1)
    node2 = pydot.Node("2", style="filled", fillcolor="lightcoral", label="")
    graphlegend.add_node(node2)
    node3 = pydot.Node("3", style="filled", fillcolor="lightyellow", label="")
    graphlegend.add_node(node3)
    node4 = pydot.Node("4", style="filled", fillcolor="green", label="")
    graphlegend.add_node(node4)

    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(legend1, legend2, style="invis"))
    graph.add_edge(pydot.Edge(legend2, legend3, style="invis"))
    graph.add_edge(pydot.Edge(legend3, legend4, style="invis"))
    graph.add_edge(pydot.Edge(legend4, legend5, style="invis"))
    graph.add_edge(pydot.Edge(node1, node2, style="invis"))
    graph.add_edge(pydot.Edge(node2, node3, style="invis"))
    graph.add_edge(pydot.Edge(node3, node4, style="invis"))

    

if __name__ == "__main__":

    right_missinaries = 3
    right_cannibals = 3
    is_boat_left = False
    a = State.Missinaries_cannibals( right_missinaries, right_cannibals, is_boat_left, 'valid')
    li = [a]
    start_node = Node(a, None)
    graph = pydot.Dot('my_graph', graph_type='digraph', bgcolor='white')
    my_node=pydot.Node('root',label=str(start_node.value))
    my_node.add_style('filled')
    my_node.set_fillcolor('aqua')
    graph.add_node(my_node)
    generate(start_node, li)
    draw_legend(graph)
    graph.write_png('output2.png')