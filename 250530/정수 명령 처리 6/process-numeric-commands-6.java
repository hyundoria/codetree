import java.util.Scanner;

public class Main {

    static int size = 0;
    static int[] arr = new int[100001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {

            String s = sc.next();

            switch (s) {
                case "push":
                    insert(sc.nextInt());
                    break;
                case "pop":
                    System.out.println(remove());
                    break;
                case "size":
                    System.out.println(size);
                    break;
                case "empty":
                    System.out.println(size == 0 ? 1 : 0);
                    break;
                case "top":
                    System.out.println(arr[1]);
            }


        }
    }

    static void insert(int val) {
        arr[++size] = val;
        int idx = size;
        while(idx != 1 && arr[idx] > arr[idx/2]) {
            swap(idx, idx/2);
            idx /= 2;
        }
    }

    static int remove() {
        if (size == 0) {
            return 0;
        }
        int root = arr[1];
        arr[1] = arr[size];
        arr[size--] = 0;
        heapify(1);
        return root;
    }

    static void heapify(int idx) {
        while(true) {
            int smallest = idx;
            int left = idx * 2;
            int right = idx * 2 + 1;

            if(left <= size && arr[left] > arr[smallest]) {
                smallest = left;
            }
            if(right <= size && arr[right] > arr[smallest]) {
                smallest = right;
            }
            if(smallest != idx) {
                swap(idx,smallest);
                idx = smallest;
            }
            else {
                break;
            }

        }
    }

    static void swap(int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }


}
