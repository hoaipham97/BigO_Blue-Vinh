package NightAtTheMuseum;

import java.util.Scanner;

//Codeforces 731A

public class NightAtTheMuseum {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String str = in.next();
		int sum = getMax('a', str.charAt(0));
		for (int i = 1; i < str.length(); i++) {
			sum += getMax(str.charAt(i), str.charAt(i - 1));
		}
		in.close();
		System.out.println(sum);
	}

	private static int getMax(char a, char b) {
		int range = Math.abs(a - b);
		int min = (26 - range) > range ? range : (26 - range);
		return min;
	}

}
