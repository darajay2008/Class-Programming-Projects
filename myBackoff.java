import java.util.Random;
import java.io.*;
import java.lang.Math;

public class myBackoff
{
	public static void main(String[] args) throws IOException
	{
		myBackoff.Linear();
		myBackoff.Exponential();
		myBackoff.Logarithmic();
		
	}
	
	public static void Linear() throws IOException
	{
		int noOfDevices1;
		int latency1 = 0;
		int lastSuccessfulSlot1 = 0;
		int runs1 = 1;
		
		System.out.println("Linear backoff");
		PrintWriter result1 = new PrintWriter("linearLatency.txt");
		for (noOfDevices1=100; noOfDevices1<5001; noOfDevices1+=100)//5000
		{
			 int TotalLatency1=0;
			 int AverageLatency1=0;
			
			for (int sim=0; sim<10; sim++)//10
			{
				int slotsPerWindow1=2;
				int noOfDev = noOfDevices1;
				Loop:
				while(noOfDev > 0)
				{
					int[] DevicesInSlot = new int [slotsPerWindow1];
					for (int dev=0; dev<noOfDev; dev++)
					{
						Random gen = new Random();
						int randomSlot = gen.nextInt(slotsPerWindow1);
						DevicesInSlot[randomSlot]++;
					}
					//System.out.printf("Num of slots in window: %d\n", slotsPerWindow1);
					
					/*for (int dev=0; dev<slotsPerWindow1; dev++)
					{
						System.out.print(DevicesInSlot[dev]);
						System.out.println();
					}
					System.out.println("");*/
					
					for (int dev=0; dev<DevicesInSlot.length; dev++)
					{
						if (DevicesInSlot[dev]==1)
						{
							noOfDev--;
							lastSuccessfulSlot1 = dev+1;
						}
					}
					if (noOfDev > 0)
					{
						latency1 = latency1 + slotsPerWindow1;
						slotsPerWindow1 = slotsPerWindow1 + 1;
					}
					else
					{
						//System.out.printf("Last successful slot: %d\n", lastSuccessfulSlot);
						latency1 = latency1 + lastSuccessfulSlot1;
						break Loop;
					}
					
				}
				//System.out.printf("Latency: %d\n", latency1);
				TotalLatency1 = TotalLatency1 + latency1;
				latency1 =0;
			}
			//System.out.printf("Total Latency: %d", TotalLatency1);
			AverageLatency1 = (int)Math.floor(TotalLatency1/10);
			//System.out.printf("Average Latency: %d", AverageLatency1);
			System.out.printf("Run %d of 50 completed\n",runs1);
			runs1 = runs1 + 1;
			result1.println(AverageLatency1);
			result1.flush();
		}
		result1.close();
	}

	public static void Exponential() throws IOException
	{
		int noOfDevices1;
		int latency1 = 0;
		int lastSuccessfulSlot1 = 0;
		int runs1 = 1;
		
		System.out.println("Exponential backoff");
		PrintWriter result1 = new PrintWriter("exponentialLatencyextra.txt");
		for (noOfDevices1=100; noOfDevices1<5001; noOfDevices1+=100)//5000
		{
			 int TotalLatency1=0;
			 int AverageLatency1=0;
			
			for (int sim=0; sim<10; sim++)//10
			{
				int slotsPerWindow1=2;
				int noOfDev = noOfDevices1;
				Loop:
				while(noOfDev > 0)
				{
					int[] DevicesInSlot = new int [slotsPerWindow1];
					for (int dev=0; dev<noOfDev; dev++)
					{
						Random gen = new Random();
						int randomSlot = gen.nextInt(slotsPerWindow1);
						DevicesInSlot[randomSlot]++;
					}
					//System.out.printf("Num of slots in window: %d\n", slotsPerWindow1);
					
					/*for (int dev=0; dev<slotsPerWindow1; dev++)
					{
						System.out.print(DevicesInSlot[dev]);
						System.out.println();
					}*/
					//System.out.println("");
					
					for (int dev=0; dev<DevicesInSlot.length; dev++)
					{
						if (DevicesInSlot[dev]==1)
						{
							noOfDev--;
							lastSuccessfulSlot1 = dev+1;
						}
					}
					if (noOfDev > 0)
					{
						latency1 = latency1 + slotsPerWindow1;
						slotsPerWindow1 = slotsPerWindow1 * 2;
					}
					else
					{
						//System.out.printf("Last successful slot: %d\n", lastSuccessfulSlot);
						latency1 = latency1 + lastSuccessfulSlot1;
						break Loop;
					}
					
				}
				//System.out.printf("Latency: %d\n", latency1);
				TotalLatency1 = TotalLatency1 + latency1;
				latency1 =0;
			}
			//System.out.printf("Total Latency: %d", TotalLatency1);
			AverageLatency1 = (int)Math.floor(TotalLatency1/10);
			//System.out.printf("Average Latency: %d", AverageLatency1);
			System.out.printf("Run %d of 50 completed\n",runs1);
			runs1 = runs1 + 1;
			result1.println(AverageLatency1);
			result1.flush();
		}
		result1.close();
	}
	
	public static void Logarithmic() throws IOException
	{
		int noOfDevices1;
		int latency1 = 0;
		int lastSuccessfulSlot1 = 0;
		int runs1 = 1;
		
		System.out.println("Logarithmic backoff");
		PrintWriter result1 = new PrintWriter("logarithmicLatency.txt");
		for (noOfDevices1=100; noOfDevices1<5001; noOfDevices1+=100)//5000
		{
			 int TotalLatency1=0;
			 int AverageLatency1=0;
			
			for (int sim=0; sim<10; sim++)//10
			{
				int slotsPerWindow1=2;
				int noOfDev = noOfDevices1;
				Loop:
				while(noOfDev > 0)
				{
					int[] DevicesInSlot = new int [slotsPerWindow1];
					for (int dev=0; dev<noOfDev; dev++)
					{
						Random gen = new Random();
						int randomSlot = gen.nextInt(slotsPerWindow1);
						DevicesInSlot[randomSlot]++;
					}
					//System.out.printf("Num of slots in window: %d\n", slotsPerWindow1);
					
					/*for (int dev=0; dev<slotsPerWindow1; dev++)
					{
						System.out.print(DevicesInSlot[dev]);
						System.out.println();
					}
					System.out.println("");*/
					
					for (int dev=0; dev<DevicesInSlot.length; dev++)
					{
						if (DevicesInSlot[dev]==1)
						{
							noOfDev--;
							lastSuccessfulSlot1 = dev+1;
						}
					}
					if (noOfDev > 0)
					{
						latency1 = latency1 + slotsPerWindow1;
						double LogSlots	= Math.log(slotsPerWindow1)/Math.log(2);
						slotsPerWindow1 = (int)Math.floor((1 + 1/LogSlots) * slotsPerWindow1);
					}
					else
					{
						//System.out.printf("Last successful slot: %d\n", lastSuccessfulSlot);
						latency1 = latency1 + lastSuccessfulSlot1;
						break Loop;
					}
					
				}
				//System.out.printf("Latency: %d\n", latency1);
				TotalLatency1 = TotalLatency1 + latency1;
				latency1 =0;
			}
			//System.out.printf("Total Latency: %d", TotalLatency1);
			AverageLatency1 = (int)Math.floor(TotalLatency1/10);
			//System.out.printf("Average Latency: %d", AverageLatency1);
			System.out.printf("Run %d of 50 completed\n",runs1);
			runs1 = runs1 + 1;
			result1.println(AverageLatency1);
			result1.flush();
		}
		result1.close();
	}

}