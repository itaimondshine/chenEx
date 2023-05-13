# Data-Diode

### What is a Data Diode?
A data diode is a unidirectional network communication device that enables the safe, one-way transfer of data between segmented networks.
 Data diode design maintains physical and electrical separation of source and destination networks, 
establishing a non-routable, completely closed one-way data transfer between networks. 
Data diodes effectively eliminate external points of entry to the sending system, preventing intruders and contagious elements from infiltrating the network. 
Securing all of a network’s data outflow with data diodes makes it impossible for an insecure or hostile network
to pass along malware, access your system, or accidentally make harmful changes. (for more info click <a href=https://owlcyberdefense.com/blog/what-is-data-diode-technology-how-does-it-work/> here </a>).

<img src=https://github.com/ChenLipschitz/Network-Diode/blob/main/images/dataDiode%20idea.jpg alt="data diode img" width="632" height="180">


## Our Data Diode Components:

*	Sender- encodes a file and sends it to Proxy1 using the TCP
*	Proxy1- receives the encoded file, decodes it, and sends the file to the Data Diode using our RUDP.
*	Data Diode
*	Proxy2- receives the encoded file, decodes it and sends the encoded file to End User using the TCP.
*	End User- receives the encoded file, decode it and saves the file.


<b> NOTE- </b>
In our solution, we utilize a protocol break between the sender and end user to ensure secure data transfer. This break enables data to be transferred via different protocols, concealing sensitive source network information and preventing the transmission of malicious data. Our proxies facilitate two-way communication on each side of the data diode (Sender-Proxy1, Proxy2-EndUser), allowing for unidirectional network communication using two-way protocols like TCP.

## Bibliography
* <a href=https://owlcyberdefense.com/blog/what-is-data-diode-technology-how-does-it-work/> owlcyberdefense </a>
* <a href=https://athenadynamics.com/demystifying-data-diodes-data-diodes-explaine> athenadynamics </a>
* <a href=https://www.geeksforgeeks.org/reliable-user-datagram-protocol-rudp/> geeksforgeeks </a>
* <a href=https://openai.com/blog/chatgpt> ChatGPT </a>
