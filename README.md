# SimSca.py
A simple Nmap vuln scan script that use some NSE scripts and xsltproc to have a easy to use and readable lightweight vulnscanner .

NSE scripts used : 
      
      default
      auth
      vuln
      discovery
      vulners (https://github.com/vulnersCom/nmap-vulners) ---- Testing it
      
      
Requirements :  

    Linux 
    Nmap     
    xsltproc
    vulners.nse (download at https://github.com/vulnersCom/nmap-vulners then copy the vulners.nse to nmap/script folder           
      
      
Usage : 
   
     ./SimSca.py <target IP>
     
     wait until the script finish 
     
     the results will be in a file called <target IP>_scan.htm in the same directory as the script.
 
Notice: the script is quite slow 
