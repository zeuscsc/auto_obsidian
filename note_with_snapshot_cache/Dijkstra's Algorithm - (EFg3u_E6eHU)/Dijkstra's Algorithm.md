## Dijkstra's Algorithm
### Dijkstra's Algorithm Introduction

Dijkstra's algorithm is a graph theory solution for finding the shortest path between two vertices in a weighted graph. It is commonly used to determine the quickest route from one location to another, based on factors such as distance or time. [![[/snapshots/EFg3u_E6eHU/00-00-03.png]]](<https://youtu.be/EFg3u_E6eHU?t=0s>)

### Dijkstra's Algorithm Process

1. Initialize all vertex distances to infinity, except the source vertex which has a distance of zero. [![[/snapshots/EFg3u_E6eHU/00-07-53.png]]](<https://youtu.be/EFg3u_E6eHU?t=470s>)
2. Mark all vertices as unexplored. [![[/snapshots/EFg3u_E6eHU/00-07-59.png]]](<https://youtu.be/EFg3u_E6eHU?t=476s>)
3. Repeat the following two steps: [![[/snapshots/EFg3u_E6eHU/00-03-16.png]]](<https://youtu.be/EFg3u_E6eHU?t=195s>)
   - Update the distance estimates for unexplored neighboring vertices. [![[/snapshots/EFg3u_E6eHU/00-07-48.png]]](<https://youtu.be/EFg3u_E6eHU?t=465s>)
   - Choose the unexplored vertex with the smallest distance to explore next. 
4. Continue the repetition until the destination vertex is explored. [![[/snapshots/EFg3u_E6eHU/00-02-35.png]]](<https://youtu.be/EFg3u_E6eHU?t=152s>)
5. Find the shortest path by tracing back the previous vertices from the destination vertex. [![[/snapshots/EFg3u_E6eHU/00-01-12.png]]](<https://youtu.be/EFg3u_E6eHU?t=69s>)

### Important Notes

- The algorithm's output includes both the shortest distance and the path itself. [![[/snapshots/EFg3u_E6eHU/00-06-19.png]]](<https://youtu.be/EFg3u_E6eHU?t=376s>)
- Only works correctly with non-negative edge weights. [![[/snapshots/EFg3u_E6eHU/00-07-12.png]]](<https://youtu.be/EFg3u_E6eHU?t=429s>)
- Utilize a priority queue to efficiently choose the next unexplored vertex. 
- To reconstruct the path, track the previous vertex visited for each updated distance estimate. [![[/snapshots/EFg3u_E6eHU/00-06-39.png]]](<https://youtu.be/EFg3u_E6eHU?t=396s>)

Source: [(156) How Dijkstra's Algorithm Works - YouTube](https://www.youtube.com/watch?v=EFg3u_E6eHU)
