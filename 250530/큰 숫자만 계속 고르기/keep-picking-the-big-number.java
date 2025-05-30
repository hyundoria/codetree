import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            pq.add(sc.nextInt() * -1);
        }
        for (int i = 0; i < M; i++) {
            int max = pq.poll();
            max = (max * -1) -1;
            pq.add(max * -1);
        }
        System.out.println(-pq.peek());




    }
}
