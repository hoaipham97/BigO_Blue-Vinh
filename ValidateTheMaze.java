package ValidateTheMaze;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class ValidateTheMaze {

	private static ArrayList<ArrayList<Integer>> graph;
	private static int V;
	private static ArrayList<Integer> path;
	private static ArrayList<Boolean> visited;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		for (int i = 0; i < t; i++) {
			int M = in.nextInt();
			int N = in.nextInt();
			V = M * N;
			graph = new ArrayList<>(V);
			for (int j = 0; j < V; j++) {
				graph.add(new ArrayList<>());
			}
			ArrayList<ArrayList<Integer>> temp = new ArrayList<ArrayList<Integer>>();
			for (int j = 0; j < M; j++) {
				temp.add(new ArrayList<Integer>());
				for (int k = 0; k < N; k++) {
					temp.get(j).add(0);
				}
			}
			ArrayList<Integer> edgeNode = new ArrayList<Integer>();

			for (int j = 0; j < M; j++) {
				String next = in.next();
				for (int k = 0; k < N; k++) {
					if ('.' == next.charAt(k)) {
						temp.get(j).set(k, 1);
						if (k == 0 || k == N - 1 || j == 0 || j == M - 1) {
							edgeNode.add(j * N + k);
						}
					}
				}
			}
			if (edgeNode.size() == 2) {
				for (int j = 0; j < M; j++) {
					for (int k = 0; k < N; k++) {
						if (temp.get(j).get(k) == 1) {
							if (j + 1 < M) {
								Integer down = temp.get(j + 1).get(k);
								if (down != null && down == 1) {
									graph.get(j * N + k).add((j + 1) * N + k);
									graph.get((j + 1) * N + k).add(j * N + k);
								}
							}
							if (j - 1 >= 0) {
								Integer up = temp.get(j - 1).get(k);
								if (up != null && up == 1) {
									graph.get(j * N + k).add((j - 1) * N + k);
									graph.get((j - 1) * N + k).add(j * N + k);
								}
							}
							if (k - 1 >= 0) {
								Integer left = temp.get(j).get(k - 1);
								if (left != null && left == 1) {
									graph.get(j * N + k).add(j * N + k - 1);
									graph.get(j * N + k - 1).add(j * N + k);
								}
							}
							if (k + 1 < N) {
								Integer right = temp.get(j).get(k + 1);
								if (right != null && right == 1) {
									graph.get(j * N + k).add(j * N + k + 1);
									graph.get(j * N + k + 1).add(j * N + k);
								}
							}

						}
					}
				}
				BFS(edgeNode.get(0));
				if (isConnect(edgeNode.get(0), edgeNode.get(1))) {
					System.out.println("valid");
				} else {
					System.out.println("invalid");
				}

			} else {
				System.out.println("invalid");
			}

		}
		in.close();
	}

	private static boolean isConnect(Integer s, Integer f) {
		if (s == f) {
			return false;
		}
		if (path.get(f) == -1) {
			return false;
		}
		ArrayList<Integer> b = new ArrayList<>();
		while (true) {
			b.add(f);
			if (path.get(f) == -1) {
				break;
			}
			f = path.get(f);
			if (s == f) {
				b.add(f);
				break;
			}
		}
		if (b.size() == 0) {
			return false;
		}
		return true;
	}

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

}
