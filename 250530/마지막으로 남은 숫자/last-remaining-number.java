import java.util.PriorityQueue;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            pq.add(-sc.nextInt());
        }

        while (pq.size() > 1) {

            int a = -pq.poll();
            int b = -pq.poll();
            if (a != b) {
                pq.add(-a+b);
            }
        }

        if (pq.isEmpty()) {
            System.out.println(-1);
        }
        else {
            System.out.println(-pq.poll());
        }



    }
}