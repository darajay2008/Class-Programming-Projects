#include <iostream>
#include <stdint.h>
#include<bitset>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

void encrypt (uint32_t* v, uint32_t* k, uint32_t &v0, uint32_t &v1)
{
  v0 = v[0];
  v1 = v[1];
  uint32_t sum = 0, i;
  //  uint32_t v0=v[0], v1=v[1], sum=0, i;           /* set up */
    uint32_t delta=0x9e3779b9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i < 32; i++) {                       /* basic cycle start */
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);  
    }/* end cycle */
   
    uint32_t y[]={v0,v1};
   
   
}



int main()
{
  int sum = 0;
  
  double average;
  int trials = 10000;
  int randno = (rand()%(2^32))+1;
  //cout<<"Random 32bit number: "<<randno<<endl<<endl;
   uint32_t k[]= {0b1110011000010101,0b1010110100101000,0b10011010011001011,0b1111001101100000};
    uint32_t p[] = {0b1000110000000100110, 0b10001001011110110100};
   
 
 uint32_t a= p[1];
      
 uint32_t arr[1][15];
      
	  
        for (int b=8; b<16; b++)
	 {
	    int count = 0;
	     for (int trial=0; trial<trials; trial++)
		 {
	       int aprime= a ^ (1u << b);
	     
	       //    cout << "the new integer produced when bit "<<b<<" of "<<std::bitset<32>(a)<<" is flipped is: "<<std::bitset<32>(aprime)<<endl;
	       
   uint32_t pprime[]={p[0],aprime};
   uint32_t* y;
   uint32_t e0;
   uint32_t e1;
   encrypt(p, k, e0, e1);
   uint32_t* yprime;
   // cout << "E: " << std::bitset<32>(e0) << std::bitset<32>(e1) << endl;
   uint32_t eP0;
   uint32_t eP1;
   
   encrypt (pprime, k, eP0, eP1);
   // cout << "E-Prime: " << std::bitset<32>(eP0) << std::bitset<32>(eP1) << endl;

   uint32_t Z0 = e0 ^ eP0;
   uint32_t Z1 = e1 ^ eP1;

   std::bitset<32> Z0bits(Z0);
   //  std::cout<<Z0bits.to_string()<<std::endl;
   std::bitset<32>Z1bits(Z1);
   // std::cout<<Z1bits.to_string()<<std::endl;

   // cout << "Z: " << std::bitset<32>(Z0) << std::bitset<32>(Z1) << endl;

    
  
   
            for (int j=0; j<32; j++)
	      {
		if (Z0bits[j]==1)
		  count++;
		if (Z1bits[j]==1)
		  count++;
	      }
     }
      average = count/trials;
       cout<<"Average of 1s in "<<trials<<" number of trials: "<<average;
      cout<<endl;
   }
      
}


