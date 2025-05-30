import java.util.PriorityQueue;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        float totalsum = 0;

        for (int i = 0; i < n-2; i++) {

            PriorityQueue<Integer> pq = new PriorityQueue<>();
            float sum = 0;
            
            for (int j = i+1; j < n; j++) {
                pq.add(arr[j]);
            }
            
            pq.poll();
            int size = pq.size();
            for (int j = 0; j < size; j++) {
                sum += pq.poll();
            }
            sum = sum/size;
            if (totalsum < sum){
                totalsum = sum;
            }
            
        }

        System.out.printf("%.2f", totalsum);





    }
}