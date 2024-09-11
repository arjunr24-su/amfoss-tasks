import java.io.IOException;
import java.nio.file.*;

public class subtask4{
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(new String(Files.readAllBytes(Paths.get("input.txt"))).trim());
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < n; i++) {
            output.append(" ".repeat(n - i - 1)).append("*".repeat(2 * i + 1)).append("\n");
        }
        for (int i = n - 2; i >= 0; i--) {
            output.append(" ".repeat(n - i - 1)).append("*".repeat(2 * i + 1)).append("\n");
        }
        Files.write(Paths.get("output.txt"), output.toString().getBytes());
    }
}