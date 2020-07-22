import java.util.*;

public class main {

	public static void main(String[] args) {
		
		long startTime = System.nanoTime();
		
		Scanner sc = new Scanner(System.in);
		Random rand = new Random();

		// list

        List<String> list = new ArrayList<>(); 
		list.add("head");
		list.add("tail");
		
		// list



		int tail = 0;
		int head = 0;	
		System.out.println("how many coin do you want?");
		System.out.println(">>> ");
		int inp = sc.nextInt();

		for(int i = 0; i < inp; i++) {
			int randomNumber = rand.nextInt(list.size());
			if(list.get(randomNumber) == list.get(0)) {
				tail++;
			}
			if(list.get(randomNumber) == list.get(1)) {
				head++;
	
			}
			
		}
		System.out.println("\n\n\nhead : " + head);
		System.out.println("\n\n\n" + "tail : " + tail);
		double sum_head = head/inp * 100;
		double sum_tail = tail/inp * 100; 
		System.out.println("\n\n\nhead percentage : " + sum_head);
		System.out.println("\n\n\ntail percentage : " + sum_tail);
		long endTime = System.nanoTime();
		long totalTime = endTime - startTime;
		long totalTimeinmilli = totalTime / 1000000;
		System.out.println("nanosecconds "+totalTime);
		System.out.println("milliseconds "+ totalTimeinmilli);


			
			
	}
}