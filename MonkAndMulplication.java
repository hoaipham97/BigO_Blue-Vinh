package MonkAndMultiplication;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class MonkAndMulplication {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			arr.add(in.nextInt());
		}
		PriorityQueue<Integer> q = new PriorityQueue<Integer>(new MaxHeapComparator());
		for (int i = 0; i < n; i++) {
			q.add(arr.get(i));
			long sum = 1;
			if (i <2) {
				System.out.println(-1);
			} else {
				ArrayList<Integer> tops = new ArrayList<Integer>();
				for(int j = 0;j<3;j++) {
					int top = q.poll();
					sum *= top;
					tops.add(top);
				}
				for(int j = 0;j<3;j++) {
					q.add(tops.get(j));
				}
				System.out.println(sum);
			}
		}
		in.close();
	}

	public static class MaxHeapComparator implements Comparator<Integer> {
		@Override
		public int compare(Integer o1, Integer o2) {
			return o2.compareTo(o1);
		}
	}

}
