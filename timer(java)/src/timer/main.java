package timer;

import java.util.*;

public class main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		boolean bool_hour = false;
		boolean bool_min = false;
		boolean bool_seccond = false;
		
		System.out.println("enter the hour for timer");
		String inp_hour = sc.nextLine();
		System.out.println("enter the miniut for timer");
		String inp_min = sc.nextLine();
		System.out.println("enter the seccond for timer");
		String inp_seccond = sc.nextLine();
		while (true){
			Date time = new Date();
			int hour = time.getHours();
			int min = time.getMinutes();
			int sec = time.getSeconds();

			if(hour == Integer.parseInt(inp_hour)); bool_hour = true;
			if(hour == Integer.parseInt(inp_hour)); bool_min = true;
			if(hour == Integer.parseInt(inp_hour)); bool_seccond = true;
			
			if(bool_hour == true && bool_min == true && bool_seccond == true) {
				System.out.println("time out");
			}
			
			
		}
	}
	
}