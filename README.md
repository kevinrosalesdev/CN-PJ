What we have to define:

- What networks ? (Simulated and real?)
    * Try both approaches [[Link](http://networkrepository.com/tech-routers-rf.php)]
    * Remember to attach the isolated nodes!
- Initial State ?
    * Single Point [Default].
    * Several Points.
- Strategies for defending ?
    * Defending => Hackers attacks, percolation...
    * Taking `N` hubs [Default].
    * Taking `N` nodes with most betweenness.
    * `N/2` hubs and `N/2` with most betweenness.
- Algorithms ? (Monte-Carlo, MMCA, other ?)
    * Number of defensive nodes proportional to `G.nodes()` [Default: 10%]
    * Monte-Carlo.
    * MMCA.
- **Issue:**
    * **SI vs SIS vs SIR Model.**

Division [BEFORE NEXT SUNDAY]:

- Descriptors of the network and Degree Histograms [Paul]
- Network generation/finding [Alex/Kevin]
    - Alex: parsing graphs.
    - Alex/Kevin: isolated nodes problem.
    - Generating Scale-Free networks (w/o nodes problem) and save graphs.
- Script for testing [All]
    - Done meanwhile programming.
- Defending strategy [Kevin]:
  * Taking `N` hubs [Default].
  * Taking `N` nodes with most betweenness.
  * `N/2` hubs and `N/2` with most betweenness.
- Algorithm with honeypot implemented
  * Monte-Carlo [Paul].
  * MMCA [Kevin].
- Visualizing the network [Alex].
  * Status per iteration.
  * Graph visualization.
  * Rho-b
  * Rho-time
  
  
- Start report