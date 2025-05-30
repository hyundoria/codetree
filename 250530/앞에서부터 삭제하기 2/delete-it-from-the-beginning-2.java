import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        long[] prefixSum = new long[n + 1];
        int[] suffixMin = new int[n + 1];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            prefixSum[i + 1] = prefixSum[i] + arr[i];
        }

        // suffixMin[i] = min(arr[i] ~ arr[n-1])
        suffixMin[n] = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            suffixMin[i] = Math.min(arr[i], suffixMin[i + 1]);
        }

        double maxAvg = 0.0;
        for (int k = 1; k <= n - 2; k++) {
            long sum = prefixSum[n] - prefixSum[k];
            int min = suffixMin[k];
            sum -= min;

            int count = n - k - 1;
            if (count > 0) {
                double avg = (double) sum / count;
                maxAvg = Math.max(maxAvg, avg);
            }
        }

        System.out.printf("%.2f", maxAvg);
    }
}
