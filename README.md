# graph-maker-ros2
Graph maker for ros2 elements (Nodes and Topics). This project is very simple, it's a library that transforms indices matrix to graphic visualization.
This library produces an rqt-like graph, so _why use it_? It has been very useful for me when rqt is not available in raspberry environments without gui (like ubuntu-core).

You can use a node to pull out the graph produced by the maker and view it on the Web, through a socket, with `rosboard`.
![image](repo_resources/rqt_graph.jpg)

## Directories Layout
```
├── make_graph.py
├── README.md
├── repo_resources
│   └── ...
├── src
│   ├── ENodeType.py
│   └── GraphTree.py
└── test
    └── test_maker.py
```

## Requirements

## Usage
**TODO**

### Input: Indices Matrix
**TODO**

### Output: Image with ros Graph
**TODO**
