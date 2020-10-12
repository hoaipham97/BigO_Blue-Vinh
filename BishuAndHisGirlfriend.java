package BishuAndHisGirlfriend;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class BishuAndHisGirlfriend {

	private static ArrayList<ArrayList<Integer>> graph;
	private static int V;
	private static ArrayList<Integer> path;
	private static ArrayList<Boolean> visited;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		V = n + 1;
		graph = new ArrayList<ArrayList<Integer>>();
		for (int j = 0; j < V; j++) {
			graph.add(new ArrayList<>());
		}
		for (int i = 0; i < n - 1; i++) {
			int u = in.nextInt();
			int v = in.nextInt();
			graph.get(u).add(v);
			graph.get(v).add(u);
		}
		int m = in.nextInt();
		int min = n;
		int k = 0;
		DFS(1);
		for (int i = 0; i < m; i++) {
			int c = in.nextInt();
			int dist = calPath(1, c);
			if (dist != 0 && dist <= min) {
				if (dist == min) {
					k = k > c ? c : k;
				} else {
					k = c;
				}
				min = dist;
			}
		}
		System.out.println(k);
		in.close();
	}

	private static void DFS(int src) {
		Stack<Integer> s = new Stack<>();
		path = new ArrayList<>();
		visited = new ArrayList<>();
		for (int i = 0; i < V; i++) {
			visited.add(false);
			path.add(-1);
		}
		visited.set(src, true);
		s.add(src);
		while (!s.isEmpty()) {
			int u = s.pop();
			for (int i = 0; i < graph.get(u).size(); i++) {
				int v = graph.get(u).get(i);
				if (!visited.get(v)) {
					visited.set(v, true);
					path.set(v, u);
					s.add(v);
				}
			}
		}
	}

	private static int calPath(int src, int des) {
		if (src == des) {
			return -1;
		}
		if (path.get(des) == -1) {
			return -1;
		}
		int dist = 0;
		while (des != -1) {
			des = path.get(des);
			dist += 1;
			if (src == des) {
				break;
			}
		}
		return dist;
	}

}
