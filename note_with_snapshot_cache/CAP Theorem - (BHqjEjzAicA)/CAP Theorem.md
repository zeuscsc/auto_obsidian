## CAP Theorem
### CAP Theorem Definition
The CAP theorem is a concept in computer science that explains the trade-offs between consistency, availability, and partition tolerance in distributed systems. [![[/snapshots/BHqjEjzAicA/00-00-04.png]]](<https://youtu.be/BHqjEjzAicA?t=0s>)

### Network Partition
A network partition happens when nodes in a distributed system are unable to communicate with each other due to network failures, forcing a system to choose between consistency and availability. [![[/snapshots/BHqjEjzAicA/00-00-54.png]]](<https://youtu.be/BHqjEjzAicA?t=52s>)

### CAP Theorem Trade-offs
- Consistency: All nodes have a consistent view of the data. [![[/snapshots/BHqjEjzAicA/00-00-27.png]]](<https://youtu.be/BHqjEjzAicA?t=25s>)
- Availability: A system responds to user requests at all times. [![[/snapshots/BHqjEjzAicA/00-00-37.png]]](<https://youtu.be/BHqjEjzAicA?t=35s>)
- Partition Tolerance: A system continues operating even if there is a network partition. [![[/snapshots/BHqjEjzAicA/00-00-44.png]]](<https://youtu.be/BHqjEjzAicA?t=42s>)

### Example: Tiny Bank with Two ATMs [![[/snapshots/BHqjEjzAicA/00-01-27.png]]](<https://youtu.be/BHqjEjzAicA?t=86s>)
A system chooses between consistency and availability when there is a network partition, leading to potential undesirable outcomes like negative account balances. [![[/snapshots/BHqjEjzAicA/00-01-05.png]]](<https://youtu.be/BHqjEjzAicA?t=63s>)

### Example: Social Media Platform
A social media platform may prioritize availability over consistency, resulting in users sometimes seeing slightly different views on the platform. [![[/snapshots/BHqjEjzAicA/00-03-17.png]]](<https://youtu.be/BHqjEjzAicA?t=195s>)

### CAP Theorem Limitations
The CAP theorem assumes 100% availability or 100% consistency, but in reality, there are degrees of consistency and availability that distributed system designers must carefully consider. [![[/snapshots/BHqjEjzAicA/00-03-39.png]]](<https://youtu.be/BHqjEjzAicA?t=217s>)

### Real-Life Trade-Offs
During normal operation without network failures, there are additional trade-offs between latency and consistency, which are covered by the Peckel theorem. [![[/snapshots/BHqjEjzAicA/00-05-14.png]]](<https://youtu.be/BHqjEjzAicA?t=313s>)

### CAP Theorem Conclusion
The CAP theorem is a useful tool to help think through high-level trade-offs when there's a network partition, but it does not provide a complete picture of the trade-offs to consider when designing a well-rounded distributed system. [![[/snapshots/BHqjEjzAicA/00-04-46.png]]](<https://youtu.be/BHqjEjzAicA?t=285s>)

Source: [CAP Theorem Simplified - YouTube](https://www.youtube.com/watch?v=BHqjEjzAicA)
