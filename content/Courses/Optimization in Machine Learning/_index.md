---
title: "Optimization in ML"
weight: -20
---

![](opt_background.png)

## Introduction and Motivation

Humans learn to design algorithms.

Can algorithms *learn* to design algorithms? This is the domain of <u>machine learning</u> and <u>discrete optimization</u>.

{{< hint type=note icon=gdoc_star title="Data Center Resource Management Example" >}}
Given Services $S$ with varying CPU and Memory demands and Machines $M$, how would you design a job scheduler?

Each machine has multiple processors, so ideally we would want the minimum number of machines active while servicing all the jobs. Each service is on one machine only, and machine is "ON" if a job is assigned to it. Machines should have enough memory and CPU capacity to run all the services. Rewriting in mathematical notation:
| Variables                                                    | Metrics                           | Constraints                                                  |
| ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ |
| \(y_m = 1\) if machine ***m*** is used <br /> {{< katex >}}x_{s,m} = 1{{< \katex >}} if service ***s*** runs on ***m***<br /> $x \in \{0,1\}^{S \times M}, y \in \{0,1\}^M$ | **minimize** $\sum_{m=1}^{M} y_m$ | $\sum_{m=1}^M x_{s,m} =1 \: \forall s$<br /> $y_m \geq x_{s,m} \: \forall s,m$<br /> $\sum_{s=1}^S \mathbf{mem}(s) \cdot x_{s,m} \leq \mathbf{MEMCAP}(m) \: \forall m$<br />   $\sum_{s=1}^S \mathbf{cpu}(s) \cdot x_{s,m} \leq \mathbf{CPUCAP}(m) \: \forall m$<br /> |

{{< /hint >}}


variables, constraints, metrics --> optimization problem

data center example, using services and machines

importance: linear optimization accounts for 5% (1 trillion dollars) of economy quote

tailor algorithms to family of instances, eg resource management or online matching

overview

AI: do non-trivial tasks well, do hard tasks that humans struggle with

subgoals: perception, reasoning, control, planning

examples: game playing - reasoning + planning, autonomous driving - all four

knowledge based ai - known facts, first order logic, and/or/not constraint satisfaction, need deep domain knowledge, 

data-based ai = machine learning: dont need to know, need many examples, explainability?

supervised learning task: performance P (optimization here, loss function, metrics), task T (learn mapping from input to output), experience E (examples)

not done