#define _BSD_SOURCE
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
//#define output "C:\\Cygwin\\home\\daraj\\output.txt"

using namespace std;

char file_buffer[2000];
     int mysocket=0;

int sockfd, newsockfd, portno, r_port;
     socklen_t clilen;
     char buffer[256];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
void error(const char *msg)
{
    perror(msg);
    exit(1);
}
 



int main(int argc, char *argv[])
{
  
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     // create a socket
     // socket(int domain, int type, int protocol)
     sockfd =  socket(AF_INET, SOCK_STREAM, 0);
     
if (sockfd < 0) 
        error("ERROR opening socket");

     // clear address structure
     bzero((char *) &serv_addr, sizeof(serv_addr));

     portno = atoi(argv[1]);

     /* setup the host_addr structure for use in bind call */
     // server byte order
     serv_addr.sin_family = AF_INET;  

     // automatically be filled with current host's IP address
     serv_addr.sin_addr.s_addr = INADDR_ANY;  

     // convert short integer value for port must be converted into network byte order
     serv_addr.sin_port = htons(portno);

    
     if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
              error("ERROR on binding");

    
     listen(sockfd,5);

     // The accept() call actually accepts an incoming connection
     clilen = sizeof(cli_addr);

  
     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
     if (newsockfd < 0) 
          error("ERROR on accept");

     printf("server: got connection from %s port %d\n",inet_ntoa(cli_addr.sin_addr), ntohs(cli_addr.sin_port));


     // This send() function sends the 13 bytes of the string to the new socket
     send(newsockfd, "Hello, world!\n", 13, 0);

     bzero(buffer,256);

     n = read(newsockfd,buffer,255);
     if (n < 0) error("ERROR reading from socket");
     printf("Here is the message: %s\n",buffer);
     
     r_port = (rand()%64512) + 1024;

     bzero(buffer,256);
     // int tmp = htonl((uint32_t)r_port);
     n = write(newsockfd, &r_port, sizeof(r_port));
     
     printf ("Negotiation detected. Selected the following random port: %d\n", r_port);

     //send(newsockfd, r_port, 5, 0);

     close(newsockfd);
     close(sockfd);


  
     

     mysocket= socket(AF_INET, SOCK_DGRAM, 0);

     if (mysocket==-1)
       {
	 printf("socket not created in server\n");
	 exit(0);
       }
     else
       {
	 printf("socket created in server\n");
       }

     serv_addr.sin_port = htons(r_port);

     if(bind(mysocket, (struct sockaddr *)&serv_addr,sizeof(serv_addr))<0)
       printf("Not binded\n");
     else
       printf("Binded\n");
     printf("");
     clilen = sizeof cli_addr;   
     char buff[5];
    
     
     std::ofstream fp("output.txt");

     
       while (buff[n-1]!='1')
	{
	  memset(buff, 0, 5);
	   n = recvfrom(mysocket, buff, 5, 0, (struct sockaddr *)&cli_addr, &clilen);

	   printf("%s\n", buff);
	   
	   fp.write(buff, n-1);
	  
	 for (int i=0; i<n; i++)
	    {
	      buff[i] = toupper(buff[i]);
	    }
	 sendto(mysocket, buff, n, 0, (struct sockaddr*)&cli_addr, clilen);
	
	}
		 
		      
       fp.close();
       
      	   
       close(mysocket);
     return 0; 
      
}
    
    
