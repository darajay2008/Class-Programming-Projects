/*-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------JAIYEOLA, MERCY OLUWADARA-------------------------------------------------------------------moj31------------------------------------------------------------------------*/

#include "packet.h"
#include "packet.cpp"
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <cstdlib>
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
#include <sys/time.h>

using namespace std;


void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
  int eportno,cportno, n;
  struct sockaddr_in emsend, emrecv;
  struct hostent *server;
   socklen_t emsendlen, emrecvlen;
   int max_win_size = 7;
  int win_size =0;
  bool win_full=false;

    int sendsocket = 0;
  eportno = atoi(argv[2]);  
    
    sendsocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (sendsocket < 0)
      {
       printf("socket not created in client\n");
       exit(0);
      }
    else
      {
	printf("socket created in client");
      }
   
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }

    
    bzero((char *) &emsend, sizeof(emsend));
    emsend.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&emsend.sin_addr.s_addr,server->h_length);
    emsend.sin_port = htons(eportno);
    emsendlen = sizeof emsend;
       if (connect(sendsocket, (struct sockaddr *)&emsend, emsendlen) < 0) 
        error("ERROR connecting");

    FILE *pf;
    char buff[31];
    char spacket[50];
    int seq_no = 0;
     int recvsocket = 0;
     pf = fopen (argv[4], "r");
     	std::ofstream seq_log("seqnum.log");
		std::ofstream ack_log("ack.log");
		
     cportno = atoi(argv[3]); 
    recvsocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (recvsocket==-1)
      {
       printf("socket not created in client\n");
       exit(0);
      }
    else
      {
	printf("socket created in client\n");
      }
    
   
    emrecv.sin_port = htons(cportno);
    emrecv.sin_family = AF_INET;
    emrecv.sin_addr.s_addr = INADDR_ANY;
   
     if (bind(recvsocket, (struct sockaddr *)&emrecv, sizeof(emrecv)) < 0)
      {
	printf("Not binded\n");
	exit(1);
      }
    
    printf ("Binded\n");
    printf("\n");

    struct timeval timer;
    
     timer.tv_sec = 2;
    

    setsockopt(recvsocket,SOL_SOCKET, SO_RCVTIMEO, &timer, sizeof(timer));
   
   
    char spacket1[25];
    char buff1[16];
    
     emrecvlen = sizeof emrecv;
   
    
    packet* rcvdPacket = new packet(0,0,0,buff1);
    
  
    
    memset(spacket1, 0, 25);
    memset(buff1, 0, 16);
     if (pf!= NULL)
    {
      while (!feof(pf)&&(win_full==false))
        {
	  memset(buff, 0, 31);
	  memset(spacket,0 ,50);
     int res = fread(buff, 1, (sizeof buff)-1, pf);
	    memset((char *) &server, 0, sizeof(server));
	    
	     packet dataPacket(1,seq_no % 8,30,buff);
	     
	     
	    dataPacket.printContents();
	    dataPacket.serialize(spacket);
	    
	   
		
	    	sendto (sendsocket,spacket, 50, 0, (struct sockaddr*)&emsend, emsendlen);
		seq_no++;
		win_size++;
		
		//	seq_log<<'\n';
		seq_log<<(seq_no-1)%8<<" \r\n";
	
	
		
   

      
  
    if (win_size==max_win_size)
      {
	win_full = true;
      }
    
    	    
    if (recvfrom(recvsocket, spacket1, 25, 0, (struct sockaddr *)&emrecv, &emrecvlen)==-1)
      {
 while (!feof(pf)&&(win_full==false))
        {
	  memset(buff, 0, 31);
	  memset(spacket,0 ,50);
     int res = fread(buff, 1, (sizeof buff)-1, pf);
	    memset((char *) &server, 0, sizeof(server));
	    
	     packet dataPacket(1,seq_no % 8,30,buff);
	     
	    
	    dataPacket.printContents();
	    dataPacket.serialize(spacket);
	    
	    
		
	    	sendto (sendsocket,spacket, 50, 0, (struct sockaddr*)&emsend, emsendlen);
		seq_no++;
		win_size++;
		
		//	seq_log<<'\n';
		seq_log<<(seq_no-1)%8<<" \r\n";
		 if (win_size==max_win_size)
		   {
		     win_full = true;
		   }
	}	
      }
    else
      {
    
    win_size= win_size-1;	
    win_full=false;
      
    rcvdPacket -> deserialize(spacket1);
    rcvdPacket -> printContents();
    cout<<""<<endl<<endl;
    int rcvseqno = rcvdPacket -> getSeqNum();
    
    ack_log<<rcvseqno<<" \r\n";
    //	printf("%s",buff);

      }

  		 
	}
      	fclose(pf);
      //send EOT packet to server
      		 packet EOTPacket(3,seq_no%8,0,NULL);
	     
		
	    EOTPacket.printContents();
	    EOTPacket.serialize(spacket);
	    sleep(3);
	    	sendto(sendsocket,spacket, 50, 0, (struct sockaddr*)&emsend, emsendlen);
		//	seq_log<<'\n';
		seq_log<<seq_no%8<<" \r";

		 //RECEIVE EOT PACKET FROM server
		 
		char buff[5];
		packet* rcvdPacket2 = new packet (0,0,0,buff);
			memset(buff, 0, 5);
		sleep(4);
     recvfrom(recvsocket, spacket,50,0, (struct sockaddr *)&emrecv, &emrecvlen);
      rcvdPacket2 -> deserialize(spacket);
     rcvdPacket2 -> printContents();
     int rcvseqno = rcvdPacket2 -> getSeqNum();
     ack_log<<rcvseqno<<" \n";

	   
	
			
   }
 else
    printf("File not found.\r\n");
   	  
	      
     close(recvsocket);
    close(sendsocket);
	

      
    return 0;

}
