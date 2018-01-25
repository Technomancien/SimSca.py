# SimSca.py
A simple Nmap vuln scan Script that use some NSE scripts and xsltproc to have a easy to use and readable vulnscanner for situations when you have limited resources.


NSE scripts used : 
      
      auth
      vuln
      discovery
      vulners (https://github.com/vulnersCom/nmap-vulners) ---- Testing it
      
      
Requirements :  

    Nmap     (apt-get install nmap)
    xsltproc (apt-get install xsltproc)
    vulners.nse (download at https://github.com/vulnersCom/nmap-vulners then copy the vulners.nse to nmap/script folder           
      
 
Notice: the script is quite slow right now 
