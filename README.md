# CPRE-550-GFS-system
A small course project on Google File systems and its enhancements majorly focusing on fault tolerance and concurrency handling.

Enhanced Google File System (GFS) Project
This repository houses the Enhanced Google File System (GFS), an ambitious improvement on Google's innovative file storage solution. It aims to bolster fault tolerance, concurrency handling, and overall performance.

Project Structure
GFS_master/: Contains the original and enhanced master server code.
GFS_chunk/: Contains the original and enhanced chunk server code.
GFS_client/: Contains the original and enhanced client code for interacting with GFS.
plot_files/: Contains scripts to plot performance comparisons.
Enhancements
The project includes a series of enhancements over the original GFS implementation:

GFS_master_enhanced: Improved fault tolerance with server health checks and dynamic master election.
GFS_chunk_enhanced: Robust data replication and error recovery.
GFS_client_enhanced: Optimized for faster response times and efficient data caching.
Performance Plots
Performance improvements are demonstrated through two Python plotting scripts:

response_time_plot.py: Illustrates the response time improvements in the enhanced GFS.
system_availability_plot.py: Shows the system availability enhancements in the enhanced GFS.
Usage
Run the master, chunk, and client components within their respective directories. For enhanced performance plots, execute the plotting scripts in the plot_files/ directory.
