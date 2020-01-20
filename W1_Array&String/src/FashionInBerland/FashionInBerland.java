package FashionInBerland;

import java.util.ArrayList;
import java.util.Scanner;

//Codeforces 691A

public class FashionInBerland {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			arr.add(in.nextInt());
		}
		System.out.println(check(arr));
		in.close();
	}
	
	private static String check(ArrayList<Integer> arr) {
		if (arr.size() == 1) {
			if (arr.get(0) == 1)
				return "YES";
			else
				return "NO";
		}
		int count = 0;
		for (int i = 0; i < arr.size(); i ++) {
			if (arr.get(i) == 0) {
				count ++;
			}
		}
		if (count != 1)
			return "NO";
		return "YES";
	}

}
