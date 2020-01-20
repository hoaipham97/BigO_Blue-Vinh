package BearAndGame;

import java.util.ArrayList;
import java.util.Scanner;

//Codeforces 673A

public class BearAndGame {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		arr.add(0);
		for (int i = 1; i < n + 1; i++) {
			arr.add(in.nextInt());
		}
		int index = interestIndex(arr, n + 1);
		if (index == n && n != 1 && (arr.get(index) + 15 >= 90)) {
			System.out.println(90);
		} else
			System.out.println(arr.get(index) + 15);
		in.close();
	}

	private static int interestIndex(ArrayList<Integer> arr, int n) {
		int index = 0;
		for (int i = 1; i < n; i++) {
			if ((arr.get(i) - arr.get(i - 1)) > 15) {
				index = i - 1;
				break;
			}
			index = i;
		}
		return index;

	}

}
