import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        long[] prefixSum = new long[n + 1];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            prefixSum[i + 1] = prefixSum[i] + arr[i];
        }

        double maxAvg = 0.0;

        for (int k = 1; k <= n - 2; k++) {
            // 남은 구간: arr[k] ~ arr[n - 1]
            int minVal = Integer.MAX_VALUE;
            long sum = 0;

            for (int i = k; i < n; i++) {
                sum += arr[i];
                minVal = Math.min(minVal, arr[i]);
            }

            sum -= minVal; // 가장 작은 수 제거
            int count = n - k - 1;

            if (count > 0) {
                double avg = (double) sum / count;
                maxAvg = Math.max(maxAvg, avg);
            }
        }

        System.out.printf("%.2f", maxAvg);
    }
}
