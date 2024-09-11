use std::io;

fn print_diamond(n: usize) {
    for i in 0..n {
        println!("{:width$}{}", "", "*".repeat(2 * i + 1), width = n - i - 1);
    }
    for i in (0..n-1).rev() {
        println!("{:width$}{}", "", "*".repeat(2 * i + 1), width = n - i - 1);
    }
}

fn main() {
    let mut input = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Please type a number!");
    print_diamond(n);
}