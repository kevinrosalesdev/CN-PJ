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

- Descriptors of the network and Degree Histograms [Paul] [DONE]
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
  * Monte-Carlo [Paul] [Average of maximums in SIR].
  * MMCA [Kevin] [Adapt to SIS].
- Visualizing the network [Alex].
  * Status per iteration. [DONE]
  * Graph visualization. [DONE]
  * Rho-b [DONE]
  * Rho-time [DONE]
  * Percolation threshold plot [DONE].
  * LogLog Plot.
  
  
- Start report
  * Two worklines:
    - SIR Model (MonteCarlo) so as to explain which is the averaged upperbound of epidemic that a specific network can get before it gets recovered.
    - SIS Model (MMCA & MonteCarlo) in order to explain which is the epidemic threshold given a specific network.
  * Graphs:
    - 1 Real Graph.
    - 2 CM Graphs (exponent = 3.5, exponent = 2.7)
