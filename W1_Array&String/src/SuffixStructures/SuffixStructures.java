package SuffixStructures;

import java.util.ArrayList;
import java.util.Scanner;

//Codeforces Round #256 (Div. 2)

public class SuffixStructures {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String s = in.next();
		String t = in.next();

		if (s.length() == t.length()) {
			if (checkArray(s, t)) {
				System.out.println("array");
			} else if (s.indexOf(t) == -1) {
				System.out.println("need tree");
			}
		} else {
			if (isAutomaton(s, t)) {
				System.out.println("automaton");
			} else if (checkArray(s, t)) {
				System.out.println("both");
			} else {
				System.out.println("need tree");
			}
		}
		in.close();

	}

	public static boolean checkArray(String s, String t) {
		ArrayList<Character> arr = new ArrayList<Character>();
		for (int i = 0; i < s.length(); i++) {
			arr.add(s.charAt(i));
		}
		for (int i = 0; i < t.length(); i++) {
			if (arr.indexOf(t.charAt(i)) == -1) {
				return false;
			}
			arr.remove(arr.indexOf(t.charAt(i)));
		}
		return true;
	}

	public static boolean isAutomaton(String s, String t) {
		StringBuilder x = new StringBuilder(s);
		for (int i = 0; i < x.length(); i++) {
			if ((i >= t.length()) || (x.charAt(i) != t.charAt(i))) {
				x.deleteCharAt(i);
				i--;
			}
		}
		if (x.toString().equals(t)) {
			return true;
		}
		return false;

	}

}
