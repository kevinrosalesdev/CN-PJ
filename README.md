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
    * **SI vs SIS vs SIR Model**
      * Fix: Use a SIR/SIS model but with some novel approach such as random infections + neighbors infections.

Division [BEFORE NEXT SUNDAY]:

- Descriptors of the network and Degree Histograms [Paul]
- Network generation/finding [Alex/Kevin]
    - Alex: parsing graphs. [DONE]
    - Alex/Kevin: isolated nodes problem. [DONE]
    - Generating Scale-Free networks (w/o nodes problem) [DONE]
- Script for testing [All]
    - Done meanwhile programming.
- Defending strategy [Kevin]:
  * Taking `N` hubs [Default] [DONE].
  * Taking `N` nodes with most betweenness [DONE].
  * `N/2` hubs and `N/2` with most betweenness [DONE].
- Algorithm with honeypot implemented
  * Monte-Carlo [Paul].
  * MMCA [Kevin].
- Visualizing the network [Alex].
  * Status per iteration. [DONE]
  * Graph visualization. [DONE]
  * Rho-b [DONE]
  * Rho-time [DONE]
  * Percolation threshold plot.
  
  
- Start report
