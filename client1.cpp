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
//#define BUF_SIZE 4096
//#define filename "C:\Cygwin\home\daraj\myfile.txt.txt"
using namespace std;

void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;
int mysocket = 0;
 int bytes;
 
 
    char buffer[256];
    char nbuffer[]= "123";
    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    
    
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr,server->h_length);
    serv_addr.sin_port = htons(portno);

    if (connect(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
        error("ERROR connecting");
    
   
    bzero(buffer,256);
    // fgets(buffer,255,stdin);
    //nbuffer = '123';
    n = write(sockfd, nbuffer, strlen(nbuffer));
    if (n < 0) 
         error("ERROR writing to socket");
    bzero(buffer,256);
    n = read(sockfd, buffer, 255);
    if (n < 0) 
         error("ERROR reading from socket");
    printf("%s\n", buffer);
    
    int r_port;
    n = read(sockfd, &r_port, sizeof(r_port));
    printf("Random port: %d\n", r_port);
    
    close(sockfd);




    printf( "Jello\n");  
// Declaring a socket on the client side

mysocket = socket(AF_INET, SOCK_DGRAM, 0);

 if (mysocket==-1)
   {
     printf("socket not created in client\n");
     exit(0);
   }
 else
   {
     printf("socket created in client\n");
   }
 
 

serv_addr.sin_port = htons(r_port);
socklen_t slen = sizeof serv_addr;
char inputarray[4];

 if (connect(mysocket, (struct sockaddr *)&serv_addr, slen) < 0) 
        error("ERROR connecting");
FILE *pf;
unsigned long fsize;
char buff[5];
 
    pf = fopen(argv[3], "r");
 if (pf!= NULL)
   {
     while (!feof(pf))
       {
      int res = fread(buff, 1, (sizeof buff)-1, pf);
     buff[res]=0;
     if (res>0)
       {
	 sendto(mysocket, buff,res, 0, (struct sockaddr*)&serv_addr, slen);

          n = recvfrom(mysocket, buff, res, 0, NULL, NULL);

          printf("%s\n", buff);
       }
       
     }
     fclose(pf);
   }
 else
   printf("File not found.\r\n");



 
close(mysocket);
    
    return 0;
}
