import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }
        for (int i = 0; i < M; i++) {
            Arrays.sort(nums);
            nums[N-1]--;
        }
        Arrays.sort(nums);
        System.out.println(nums[N-1]);




    }
}
