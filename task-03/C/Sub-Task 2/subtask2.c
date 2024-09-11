#include <stdio.h>
int main() {
    FILE *infile = fopen("input.txt", "r");
    FILE *outfile = fopen("output.txt", "w");
    char ch;
    while ((ch = fgetc(infile)) != EOF) {
        fputc(ch, outfile);
    }
    fclose(infile);
    fclose(outfile);
    return 0;
}