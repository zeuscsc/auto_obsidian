Distributed System Patterns
### Top 7 Distributed System Patterns [![[/snapshots/nH4qjmP2KEE/00-00-06.png]]](<https://youtu.be/nH4qjmP2KEE?t=0s>)

#### 1. Ambassador
The Ambassador pattern acts as a go-between for your application and the services it communicates with, offloading tasks like logging, monitoring, or handling retries. Example: Kubernetes uses Envoy as an ambassador. [![[/snapshots/nH4qjmP2KEE/00-00-45.png]]](<https://youtu.be/nH4qjmP2KEE?t=42s>)

#### 2. Circuit Breaker
The Circuit Breaker pattern prevents cascading failures in distributed systems by stopping requests to an unavailable service. Example: Netflix's Hystric library. [![[/snapshots/nH4qjmP2KEE/00-01-10.png]]](<https://youtu.be/nH4qjmP2KEE?t=68s>)

#### 3. CQRS (Command Query Responsibility Segregation) [![[/snapshots/nH4qjmP2KEE/00-01-41.png]]](<https://youtu.be/nH4qjmP2KEE?t=98s>)
CQRS separates command (write) operations from query (read) operations, allowing for independent scaling and optimization. Example: E-commerce platforms. [![[/snapshots/nH4qjmP2KEE/00-02-11.png]]](<https://youtu.be/nH4qjmP2KEE?t=129s>)

#### 4. Event Sourcing
Event Sourcing stores events representing changes, providing a complete history of the system for better auditing and debugging. Example: Git version control. [![[/snapshots/nH4qjmP2KEE/00-02-48.png]]](<https://youtu.be/nH4qjmP2KEE?t=165s>)

#### 5. Leader Election
The Leader Election pattern ensures that only one node is responsible for a specific task or resource. Example: Zookeeper and etcd for distributed configurations. [![[/snapshots/nH4qjmP2KEE/00-03-11.png]]](<https://youtu.be/nH4qjmP2KEE?t=188s>)

#### 6. PubSub (Publisher Subscriber)
The PubSub pattern allows for better scalability and modularity by emitting events without knowledge of their recipients. Example: Google Cloud PubSub. [![[/snapshots/nH4qjmP2KEE/00-04-07.png]]](<https://youtu.be/nH4qjmP2KEE?t=245s>)

#### 7. Sharding
Sharding is a technique for distributing data across multiple nodes in a system, improving performance and scalability. Example: MongoDB and Cassandra for efficient data handling. [![[/snapshots/nH4qjmP2KEE/00-04-45.png]]](<https://youtu.be/nH4qjmP2KEE?t=281s>)

#### Bonus: Strangler Fig Pattern
The Strangler Fig Pattern is a method for gradually replacing legacy systems with new implementations. It helps manage risks and complexities associated with system migrations. [![[/snapshots/nH4qjmP2KEE/00-05-13.png]]](<https://youtu.be/nH4qjmP2KEE?t=310s>)

Source: [(156) Top 7 Most-Used Distributed System Patterns - YouTube](https://www.youtube.com/watch?v=nH4qjmP2KEE)
