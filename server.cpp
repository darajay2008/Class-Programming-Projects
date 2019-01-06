/*-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------JAIYEOLA, MERCY OLUWADARA-------------------------------------------------------------------moj31------------------------------------------------------------------------*/

#include "packet.h"
#include "packet.cpp"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <fstream>
#include <iostream>
#include <netinet/ip.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <algorithm>
#include<signal.h>
#include<ctype.h>

using namespace std;



int  eportno, sportno, n;
struct sockaddr_in client, emsend, emrecv;
socklen_t emrecvlen, emsendlen;



void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
  int recvsocket=0;
  int sendsocket=0;
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }

     
   
       sportno = atoi(argv[2]);

       recvsocket= socket(AF_INET, SOCK_DGRAM, 0);
	

     if (recvsocket==-1)
       {
	 printf("socket not created in server\n");
	 exit(0);
       }
     else
       {
	 printf("socket created in server\n");
       }
          
     
     emrecv.sin_port = htons(sportno);
     emrecv.sin_family = AF_INET;  
     emrecv.sin_addr.s_addr = INADDR_ANY;

      
     
        if(bind(recvsocket, (struct sockaddr *)&emrecv, sizeof(emrecv))<0)
       {
       printf("Not binded\n");
       exit(1);
       }
       
       printf("Binded\n");
 
       emrecvlen = sizeof emrecv;
       


     char spacket[50];
     char buff[31];
    
     std::ofstream output (argv[4]);
    
 packet* rcvdPacket = new packet(0,0,0,buff);
 eportno = atoi(argv[3]);
      sendsocket= socket(AF_INET, SOCK_DGRAM, 0);
      
       emsend.sin_port = htons(eportno);
     emsend.sin_family = AF_INET;  
     emsend.sin_addr.s_addr = INADDR_ANY;

     
      if (sendsocket==-1)
       {
	 printf("socket not created in server\n");
	 exit(0);
       }
     else
       {
	 printf("socket created in server\n");
       }
      if(connect(sendsocket, (struct sockaddr *)&emsend, sizeof(emsend))<0)
       {
       error("error connecting\n");
       // exit(1);
       }
       
       printf("Binded\n");
       printf("\n");
       emsendlen = sizeof emsend; 
    


     char spacket1[25];
     char buff1[16]="";
     std::ofstream arr_log("arrival.log");
     int i =0;   
     while (i<11)
       {
	 memset(spacket, 0, 50);
	 memset (buff,0, 31);
	
     n = recvfrom(recvsocket, spacket,50,0, (struct sockaddr *)&emrecv, &emrecvlen);
    
     rcvdPacket -> deserialize(spacket);
     rcvdPacket -> printContents();
     
     int seq_no = rcvdPacket -> getSeqNum();
     arr_log<<seq_no<<" \r\n";
     output.write(buff, 31);
     
     i++;

     
      
     memset(spacket1, 0, 25);
      packet dataPacket(0,seq_no,0,NULL);
    
      dataPacket.printContents();
      dataPacket.serialize(spacket1);
      
      sleep(1);
      
	n = sendto(sendsocket, spacket1, 25, 0, (struct sockaddr *)&emsend, emsendlen);
	cout<<endl<<endl;
   
      // printf("%s",buff);
       }
       sleep(4);
     //RECEIVE EOT PACKET FROM CLIENT
     recvfrom(recvsocket, spacket,50,0, (struct sockaddr *)&emrecv, &emrecvlen);
      rcvdPacket -> deserialize(spacket);
      rcvdPacket -> printContents();
     int seq_no = rcvdPacket -> getSeqNum();
     arr_log<<seq_no<<" \r\n";
     
      //send EOT packet TO CLIENT
	    packet EOTPacket(2,seq_no%8,0,NULL);
	   		
	    EOTPacket.printContents();
	    EOTPacket.serialize(spacket);
	    sleep(3);
	    	sendto(sendsocket,spacket, 50, 0, (struct sockaddr*)&emsend, emsendlen);
     close(sendsocket);

           
     close(recvsocket);

      


     
     return 0;
}
