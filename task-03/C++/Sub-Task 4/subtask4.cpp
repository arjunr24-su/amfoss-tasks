#include <fstream>
#include <string>
void printDiamond(int n, std::ofstream &outfile) {
    for (int i = 0; i < n; i++) {
        outfile << std::string(n - i - 1, ' ') << std::string(2 * i + 1, '*') << std::endl;
    }
    for (int i = n - 2; i >= 0; i--) {
        outfile << std::string(n - i - 1, ' ') << std::string(2 * i + 1, '*') << std::endl;
    }
}
int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");
    int n;
    infile >> n;
    printDiamond(n, outfile);
    return 0;
}