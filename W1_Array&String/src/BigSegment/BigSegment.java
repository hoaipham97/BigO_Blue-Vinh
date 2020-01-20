package BigSegment;

import java.util.ArrayList;
import java.util.Scanner;

//Codeforces Round #149 (Div. 2)

public class BigSegment {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		ArrayList<Integer> lowBound = new ArrayList<Integer>();
		ArrayList<Integer> upBound = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			lowBound.add(in.nextInt());
			upBound.add(in.nextInt());
		}
		in.close();
		for (int i = 0; i < n; i++) {
			if (isMin(lowBound, lowBound.get(i)) == true) {
				if (isMax(upBound, upBound.get(i)) == true) {
					System.out.println(i + 1);
					return;
				}
			}
		}
		System.out.println(-1);

	}

	public static boolean isMin(ArrayList<Integer> arr, int min) {
		for (int i = 0; i < arr.size(); i++) {
			if (arr.get(i) < min)
				return false;
		}
		return true;
	}

	public static boolean isMax(ArrayList<Integer> arr, int max) {
		for (int i = 0; i < arr.size(); i++) {
			if (arr.get(i) > max)
				return false;
		}
		return true;

	}

}
