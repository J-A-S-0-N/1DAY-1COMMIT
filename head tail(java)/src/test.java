import java.util.*;
public class test {

	public static void main(String[] args) {
		List<String> my_words = new LinkedList<String>();
		my_words.add("1153 3494 9509 2 0 0 0 0");
		my_words.add("1153 3487 9509 2 0 0 0 0");
		my_words.add("1153 3491 9525 2 0 0 0 0");
		my_words.add("1153 3464 9513 2 0 0 0 0");

		//Maybe a loop to load all your strings here...

		Random random = new Random(); //Create random class object
		int randomNumber = random.nextInt(my_words.size()); //Generate a random number (index) with the size of the list being the maximum
		System.out.println(randomNumber);
		System.out.println(my_words.get(randomNumber));

	}

}
