package ShortestReach;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class ShortestReach {

	private static ArrayList<ArrayList<Integer>> graph;
	private static int V;
	private static int E;
	private static ArrayList<Integer> path;
	private static ArrayList<Boolean> visited;

	private static void BFS(int s) {
		Queue<Integer> q = new LinkedList<>();
		path = new ArrayList<>();
		visited = new ArrayList<>();
		for (int i = 0; i < V; i++) {
			visited.add(false);
			path.add(-1);
		}
		visited.set(s, true);
		q.add(s);
		while (!q.isEmpty()) {
			int u = q.remove();
			for (int i = 0; i < graph.get(u).size(); i++) {
				int v = graph.get(u).get(i);
				if (!visited.get(v)) {
					visited.set(v, true);
					path.set(v, u);
					q.add(v);
				}
			}
		}

	}

	private static int calPath(int s, int f) {
		if (path.get(f) == -1) {
			return -1;
		}
		ArrayList<Integer> b = new ArrayList<>();
		while (true) {
			b.add(f);
			f = path.get(f);
			if (s == f) {
				b.add(f);
				break;
			}
		}
		if (b.size() == 0) {
			return -1;
		}
		return (b.size() - 1) * 6;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		for (int i = 0; i < n; i++) {
			V = in.nextInt();
			E = in.nextInt();
			graph = new ArrayList<>(V);
			for (int j = 0; j < V; j++) {
				graph.add(new ArrayList<>());
			}
			for (int j = 0; j < E; j++) {
				int u = in.nextInt() -1;
				int v = in.nextInt() -1;
				graph.get(u).add(v);
				graph.get(v).add(u);
			}
			int s = in.nextInt() -1;
			BFS(s);
			for (int j = 0; j < V; j++) {
				if (j  != s) {
					System.out.print(calPath(s, j) + " ");
				}
			}
			System.out.println();
		}
		in.close();
	}

}
