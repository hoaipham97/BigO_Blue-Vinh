package Dhoom4;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Dhoom4 {

	private static ArrayList<Long> dist;
	private static int n;
	private static ArrayList<Integer> keys;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		dist = new ArrayList<Long>(100001);
		for (int i = 0; i < 100001; i++) {
			dist.add(-1L);
		}
		Scanner in = new Scanner(System.in);
		int initKey = in.nextInt();
		int des = in.nextInt();
		n = in.nextInt();
		keys = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			keys.add(in.nextInt());
		}

		System.out.println(BFS(Long.valueOf(initKey), des));
		in.close();
	}

	private static int BFS(Long s, int d) {
		Queue<Long> q = new LinkedList<>();
		dist.set(s.intValue(), 0L);
		q.add(Long.valueOf(s));
		while (!q.isEmpty()) {
			s = q.remove();
			if (s == d) {
				break;
			}
			for (int i = 0; i < n; i++) {
				Long temp = Long.valueOf(keys.get(i) * s);
				temp %= 100000;
				if (dist.get(temp.intValue()) == -1) {
					dist.set(temp.intValue(), dist.get(s.intValue()) + 1);
					q.add(temp);
				}
			}
		}
		return dist.get(d).intValue();

	}
}
