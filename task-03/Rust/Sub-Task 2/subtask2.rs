use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    fs::write("output.txt", data).expect("Unable to write file");
}