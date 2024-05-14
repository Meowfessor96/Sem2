#include <stdio.h>

int main() {
    int n;
    double y;

    FILE *fp = fopen("data.dat", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "n\ty\n");
	y = 1 ;
    for (n = 0; n < 10; n++) {
	fprintf(fp, "%d\t%.5f\n", n, y);
        y = (n >= 0) ? y*0.5 : 0; // Apply unit step function
    }

    // Close the file
    fclose(fp);

    return 0;
}

