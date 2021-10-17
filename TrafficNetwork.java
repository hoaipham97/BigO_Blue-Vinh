package Dijkstra;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class TrafficNetwork {

    static final int MAX = 10005;
    static final int INF = (int)1e9 + 7;

    public static class Node implements Comparable<Node>{
        Integer id;
        Integer dist;

        public Node(int id, int dist) {
            this.id = id;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node other) {
            return this.dist.compareTo(other.dist);
        }

    }

    public static ArrayList<ArrayList<Node>> graphS;
    public static ArrayList<ArrayList<Node>> graphT;
    public static int[] distS = new int[MAX];
    public static int[] distT = new int[MAX];

    public static void dijkstra(int s, int[] dist, ArrayList<ArrayList<Node>> maze) {
        PriorityQueue<Node> pq = new PriorityQueue<>();

        dist[s] = 0;
        pq.add(new Node(s, 0));
        while(!pq.isEmpty()) {
            Node temp = pq.poll();
            for(Node node: maze.get(temp.id)) {
                if (temp.dist + node.dist < dist[node.id]) {
                    dist[node.id] = temp.dist + node.dist;
                    pq.add(new Node(node.id, dist[node.id]));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int cases = in.nextInt();

        for(int i = 0; i < cases ; i++) {
            int n = in.nextInt();
            int m = in.nextInt();
            int k = in.nextInt();
            int s = in.nextInt() - 1;
            int t = in.nextInt() - 1;

            graphS = new ArrayList<>();
            graphT = new ArrayList<>();
            for (int j = 0; j <n; j++) {
                graphS.add(new ArrayList<>());
                graphT.add(new ArrayList<>());
                distT[j] = INF;
                distS[j] = INF;
            }

            int shortesPath = INF;

            for(int j = 0;j < m; j++ ){
                int u = in.nextInt() - 1;
                int v = in.nextInt() - 1;
                int d = in.nextInt();
                graphS.get(u).add(new Node(v, d));
                graphT.get(v).add(new Node(u, d));
            }

            dijkstra(s, distS, graphS);
            dijkstra(t, distT, graphT);
            for(int j = 0; j < k; j++) {
                int u = in.nextInt() - 1;
                int v = in.nextInt() - 1;
                int d = in.nextInt();

                int dS = distS[u] + d + distT[v];
                int dT = distS[v] + d + distT[u];
                int min = Math.min(dS, dT);
                if (shortesPath > min)
                    shortesPath = min;
            }

            if (shortesPath == INF) {
                System.out.println(-1);
            } else {
                System.out.println(shortesPath);
            }
        }
    }
}
