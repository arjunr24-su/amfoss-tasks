#include <fstream>
#include <string>
int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");
    std::string data((std::istreambuf_iterator<char>(infile)), std::istreambuf_iterator<char>());
    outfile << data;
    return 0;
}