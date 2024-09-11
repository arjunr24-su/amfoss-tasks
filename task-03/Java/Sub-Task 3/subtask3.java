import java.util.Scanner;

public class subtask3 {
    /**
     * @param args
     */
    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
        for (int i = n - 2; i >= 0; i--) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
        scanner.close();
    }
}