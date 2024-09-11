use std::fs;

fn print_diamond(n: usize) -> String {
    let mut result = String::new();
    for i in 0..n {
        result.push_str(&format!("{:width$}{}\n", "", "*".repeat(2 * i + 1), width = n - i - 1));
    }
    for i in (0..n-1).rev() {
        result.push_str(&format!("{:width$}{}\n", "", "*".repeat(2 * i + 1), width = n - i - 1));
    }
    result
}

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let n: usize = data.trim().parse().expect("Please type a number!");
    let diamond = print_diamond(n);
    fs::write("output.txt", diamond).expect("Unable to write file");
}