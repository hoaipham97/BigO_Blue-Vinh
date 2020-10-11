package ThatIsYourQueue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class ThatIsYourQuueue {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int p = in.nextInt();
		int c = in.nextInt();
		int caseNumber = 1;
		while (p != 0) {
			System.out.println("Case " + caseNumber + ":");
			Queue<Integer> q = new LinkedList<Integer>();
			for (int i = 1; i <= p; i++) {
				q.add(i);
			}
			for (int j = 0; j < c; j++) {
				String next = in.next();
				if ("N".equals(next)) {
					System.out.println(q.peek());
					q.add(q.remove());
				}
				if ("E".equals(next)) {
					expediteCommand(q, in.nextInt());
				}
			}
			caseNumber += 1;
			p = in.nextInt();
			c = in.nextInt();

		}
		in.close();

	}

	public static void expediteCommand(Queue<Integer> q, int x) {
		Queue<Integer> temp = new LinkedList<Integer>();
		temp.add(x);
		while (!q.isEmpty()) {
			if (q.peek() != x) {
				temp.add(q.remove());
			} else {
				q.remove();
				q = addQueueToQueue(q, temp);
				break;
			}
		}
	}

	public static Queue<Integer> addQueueToQueue(Queue<Integer> q, Queue<Integer> s) {
		Queue<Integer> sum = new LinkedList<Integer>();
		while (!s.isEmpty()) {
			sum.add(s.remove());
		}
		while (!q.isEmpty()) {
			sum.add(q.remove());
		}
		return sum;
	}

}
