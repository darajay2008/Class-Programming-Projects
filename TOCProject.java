import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;
public class TOCProject
{
	public static void main(String[] args) throws IOException
	{
		TOCProject.Exponential();
		TOCProject.Uniform();
	}
	public static void Exponential() throws IOException
	{
		int noOfDevices1;
		int latency1 = 0;
		int lastSuccessfulSlot1 = 0;
		int runs1 = 1;
		
		System.out.println("Exponential backoff");
		PrintWriter result1 = new PrintWriter("TOCexponentiallatency.txt");
		PrintWriter rounds1 = new PrintWriter("TOCexponentialrounds.txt");
		for (noOfDevices1=100; noOfDevices1<501; noOfDevices1+=100)//5000
		{
			 int TotalLatency1=0;
			 int AverageLatency1=0;
			
			
				int slotsPerWindow1=100;
				int noOfDev = noOfDevices1;
				int noOfRounds=0;
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
						noOfRounds++;
					}
					else
					{
						//System.out.printf("Last successful slot: %d\n", lastSuccessfulSlot);
						latency1 = latency1 + lastSuccessfulSlot1;
						noOfRounds++;
						break Loop;
					}
					
				}
				//System.out.printf("Latency: %d\n", latency1);
				TotalLatency1 = TotalLatency1 + latency1;
				latency1 =0;
			
			//System.out.printf("Total Latency: %d", TotalLatency1);
			AverageLatency1 = (int)Math.floor(TotalLatency1/10);
			//System.out.printf("Average Latency: %d", AverageLatency1);
			System.out.printf("Run %d of 5 completed\n",runs1);
			System.out.printf("Number of rounds: %d\n", noOfRounds);
			runs1 = runs1 + 1;
			rounds1.println(noOfRounds);
			rounds1.flush();
			result1.println(AverageLatency1);
			result1.flush();
		}
		result1.close();
		rounds1.close();
	}
	
	public static void Uniform() throws IOException
	{
		int noOfDevices2;
		int latency2 = 0;
		int lastSuccessfulSlot2 = 0;
		int runs2 = 1;
		
		System.out.println("Uniform backoff");
		PrintWriter result2 = new PrintWriter("TOCuniformlatency.txt");
		PrintWriter rounds2 = new PrintWriter("TOCuniformrounds.txt");
		for (noOfDevices2=100; noOfDevices2<501; noOfDevices2+=100)//5000
		{
			 int TotalLatency2=0;
			 int AverageLatency2=0;
			int noOfRounds = 0;
			
				int slotsPerWindow2=100;
				int noOfDev = noOfDevices2;
				Loop:
				while(noOfDev > 0)
				{
					int[] DevicesInSlot = new int [slotsPerWindow2];
					for (int dev=0; dev<noOfDev; dev++)
					{
						Random gen = new Random();
						int randomSlot = gen.nextInt(slotsPerWindow2);
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
							lastSuccessfulSlot2 = dev+1;
						}
					}
					if (noOfDev > 0)
					{
						latency2 = latency2 + slotsPerWindow2;
						//slotsPerWindow2 = slotsPerWindow2;
						noOfRounds++;
					}
					else
					{
						//System.out.printf("Last successful slot: %d\n", lastSuccessfulSlot);
						latency2 = latency2 + lastSuccessfulSlot2;
						noOfRounds++;
						break Loop;
					}
					
				}
				//System.out.printf("Latency: %d\n", latency1);
				TotalLatency2 = TotalLatency2 + latency2;
				latency2 =0;
		
			//System.out.printf("Total Latency: %d", TotalLatency1);
			AverageLatency2 = (int)Math.floor(TotalLatency2/10);
			//System.out.printf("Average Latency: %d", AverageLatency1);
			System.out.printf("Run %d of 5 completed\n",runs2);
			System.out.printf("Number of rounds: %d\n", noOfRounds);
			runs2 = runs2 + 1;
			rounds2.println(noOfRounds);
			rounds2.flush();
			result2.println(AverageLatency2);
			result2.flush();
		}
		result2.close();
		rounds2.close();
	}
}