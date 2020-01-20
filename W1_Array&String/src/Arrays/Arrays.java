package Arrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//Codeforces 572A

public class Arrays {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n1 = in.nextInt();
		int n2 = in.nextInt();
		int k = in.nextInt();
		int m = in.nextInt();

		ArrayList<Integer> a1 = new ArrayList<Integer>();
		ArrayList<Integer> a2 = new ArrayList<Integer>();
		for (int i = 0; i < n1; i++) {
			a1.add(in.nextInt());
		}
		for (int i = 0; i < n2; i++) {
			a2.add(in.nextInt());
		}
		in.close();
		Collections.sort(a1);
		Collections.sort(a2);
		if (a1.get(k - 1) < a2.get(n2 - m)) {
			System.out.println("YES");
			return;
		}
		System.out.println("NO");

	}

}
