import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Pair implements Comparable<Pair> {

    int x,y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pair o) {

        if (x+y == o.x+o.y){
            if (x != o.x) {
                return x - o.x;
            }
            return y - o.y;
        }
        return (x+y) - (o.x+o.y);
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] points = new int[n][2];

        PriorityQueue<Pair> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
            pq.add(new Pair(points[i][0], points[i][1]));
        }

        for (int i = 0; i < m; i++) {
            Pair pair = pq.poll();
            pair.x += 2;
            pair.y += 2;
            pq.add(pair);
        }
        
        System.out.println(pq.peek().x + " " + pq.peek().y);






    }
}
