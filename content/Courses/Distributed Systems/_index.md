---
title: "Distributed Systems"
weight: -20
---

![](background.jpg)

## What is a distributed system?

### Some Definitions:

1. Working definition: system comprised of several **physically disjoint compute resources** interconnected by a **network**.
2. Coulouris et al.: **hardware** or **software** components located at **networked computers communicate** and **coordinate** their actions by **passing messages**.
3. Tanenbaum: **collection of  independent computers** that appears to its users as **a single coherent system**.
4. Google Code University: **Application** that executes a collection of **protocols** to **coordinate the actions** of multiple **processes** on a **network**, such that all components **cooperate** together to perform a **single** or small set of **related tasks**.

We are managing **trade-offs** and how to **navigate the systems design space**.

**Node**: Physically separable computing entity (process, client, server, machine, container)

**Message**: Unit of communication among nodes (packet, data, RPC (remote procedure call), communication)

## Why build a distributed system?

Centralized system is simpler:

- local memory, storage
- failure model
- maintenance
- data security

BUT,

- **Vertical scaling** costs more than horizontal scaling (disks, IO channels, sockets)
- single point of failure
- resources can be inherently distributed (IOT)

### Related Disciplines:

- Networking (Layers, protocols, TCP/IP)
- Databases (Data management, Transactions, Consistency)
- Security (Threats, defenses)
- Parallel Computing (Concurrency, Massively parallel, HPC, NUMA, UMA)

## Characteristics of distributed systems

#### Reliability

Probability of a system to perform its required functions under stated conditions for a specified period of time (to run correctly without failure). Expressed as Mean Time Between Failure (MTBF), failure rate.

#### Availability and high-availability

Proportion of time a system is an a functioning state, (1 - unavailable). Expressed as decimal or percentage. Ratio of time usable over entire time.

Class of 9. E.g. One 9 is available 90% of the time.

**Note**: Availability {{< katex >}}\neq{{< /katex >}} Reliability (down 1 ms every hour (highly available) vs. down two weeks a year (highly reliable))

## Distributed Systems Design Fallacies

1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

## Course Overview

- Time in distributed systems (Lampert clocks, vector clocks)
- Coordination and agreement
- Consensus with Paxos
- Replication
- Consistency and transactions
- Consistent hashing, CAP theorem, web caching
- Distributed file systems (GFS)
- MapReduce, Spark
- Peer-to-peer systems, distributed hash tables (DHTs)
- Blockchains
- Time-permitting: Publish/Subscribe, clouds

