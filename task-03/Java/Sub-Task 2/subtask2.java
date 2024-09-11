import java.io.IOException;
import java.nio.file.*;

public class subtask2 {
    public static void main(String[] args) throws IOException {
        String data = new String(Files.readAllBytes(Paths.get("input.txt")));
        Files.write(Paths.get("output.txt"), data.getBytes());
    }
}