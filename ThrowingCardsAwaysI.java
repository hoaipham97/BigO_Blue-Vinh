package ThrowingCardsAwayI;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class ThrowingCardsAwaysI {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		ArrayList<Stack<Integer>> arr = new ArrayList<Stack<Integer>>();
		int k = in.nextInt();
		while (k != 0) {
			Stack<Integer> temp = new Stack<Integer>();
			for (int i = k; i > 0; i--) {
				temp.add(i);
			}
			arr.add(temp);
			k = in.nextInt();
		}
		for (int i = 0; i < arr.size(); i++) {
			System.out.print("Discarded cards: ");
			ArrayList<Integer> discard = new ArrayList<Integer>();
			int last = throwingcards(arr.get(i), discard);
			for (int j = 0; j < discard.size() - 1; j++) {
				System.out.print(discard.get(j) + ",");
			}
			System.out.println(discard.get(discard.size() - 1));
			System.out.println("Remaining card: " + last);
		}
		in.close();
	}

	public static int throwingcards(Stack<Integer> st, ArrayList<Integer> discards) {
		if (st.size() == 1) {
			return st.pop();
		}
		Stack<Integer> temp = new Stack<Integer>();
		while (st.size() > 1) {
			discards.add(st.pop());
			temp.add(st.pop());
		}
		throwingcards(temp, discards);
		return -1;
	}
}
