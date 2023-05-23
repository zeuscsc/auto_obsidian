Fibonacci Heaps
### Introduction to Fibonacci Heaps
Fibonacci heaps are an advanced data structure used in computer science to improve the running time of certain algorithms, such as Dijkstra's algorithm for finding shortest paths. They are based on binary heaps, but with a looser structure that allows for faster insert and decrease key operations. [![[/snapshots/6JxvKfSV9Ns/00-00-30.png]]](<https://youtu.be/6JxvKfSV9Ns?t=28s>)

### Data Structure and Priority Queue [![[/snapshots/6JxvKfSV9Ns/00-04-22.png]]](<https://youtu.be/6JxvKfSV9Ns?t=260s>)
Fibonacci heaps are implemented as a collection of trees called the root list, with each tree satisfying the heap property—every value is at least as small as its children. The smallest value in the heap is always at a root node, and a pointer to that node is maintained for constant-time access to the minimum element. 

### Insert Operation
The insert operation for a Fibonacci heap is simple: create a new tree with a single node and add it to the root list. Update the minimum pointer if necessary. This operation runs in constant time due to its simplicity. [![[/snapshots/6JxvKfSV9Ns/00-07-15.png]]](<https://youtu.be/6JxvKfSV9Ns?t=433s>)

### Extract Minimum Operation
The extract minimum operation requires finding and deleting the root node with the minimum value, reinserting its children into the root list, merging trees with the same degree, and updating the minimum pointer. Amortization analysis allows for a running time proportional to the maximum node degree, which is logarithmic in the size of the heap. [![[/snapshots/6JxvKfSV9Ns/00-18-18.png]]](<https://youtu.be/6JxvKfSV9Ns?t=1095s>)

### Decrease Key Operation
The decrease key operation involves cutting a node with a decreased key value out of the tree and inserting it into the root list, and fixing the heap property if necessary. It also allows for cutting out at most one child per node to ensure node degrees grow logarithmically. [![[/snapshots/6JxvKfSV9Ns/00-17-48.png]]](<https://youtu.be/6JxvKfSV9Ns?t=1066s>)

### Final Analysis
Fibonacci heaps have constant time operations except for extract minimum; however, they are not commonly used in practice due to their complexity. Despite this, they demonstrate an interesting exploration of advanced concepts in computer science and data structure optimization. 

Source: [(167) Fibonacci Heaps or "How to invent an extremely clever data structure" - YouTube](https://www.youtube.com/watch?v=6JxvKfSV9Ns)
