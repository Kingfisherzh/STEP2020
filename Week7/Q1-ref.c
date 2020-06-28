#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

double get_time()
{
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;
}

int main(int argc, char** argv)
{
	if (argc != 2) {
		printf("usage: %s N\n", argv[0]);
		return -1;
	}

	int n = atoi(argv[1]);
	double* a = (double*)malloc(n * n * sizeof(double)); // Matrix A
	double* b = (double*)malloc(n * n * sizeof(double)); // Matrix B
	double* c = (double*)malloc(n * n * sizeof(double)); // Matrix C

	// Initialize the matrices to some values.
	int i, j, k=0;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			a[i * n + j] = i * n + j; // A[i][j]
			b[i * n + j] = j * n + i; // B[i][j]
			c[i * n + j] = 0; // C[i][j]
		}
	}

	/**************************************/
	/* Write code to calculate C = A * B. */
	/**************************************/

	double begin = get_time();
	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++){
			for (k = 0; k < n; k++){
				c[i * n + j] += a[i* n + k] * b[k* n + j];
			}
		}
	}
	double end = get_time();
	printf("i-j-k time: %.6lf sec\n", end - begin);


	double begin1 = get_time();
	for (i = 0; i < n; i++){
		for (k = 0; k < n; k++){
			for (j = 0; j < n; j++){
				c[i * n + j] += a[i* n + k] * b[k* n + j];
			}
		}
	}
	double end1 = get_time();
	printf("i-k-j time: %.6lf sec\n", end1 - begin1);


	double begin2 = get_time();
	for (j = 0; j < n; j++){
		for (i = 0; i < n; i++){
			for (k = 0; k < n; k++){
				c[i * n + j] += a[i* n + k] * b[k* n + j];
			}
		}
	}
	double end2 = get_time();
	printf("j-i-k time: %.6lf sec\n", end2 - begin2);
	

	double begin3 = get_time();
	for (j = 0; j < n; j++){
		for (k = 0; k < n; k++){
			for (i = 0; i < n; i++){
				c[i * n + j] += a[i* n + k] * b[k* n + j];
			}
		}
	}
	double end3 = get_time();
	printf("j-k-i time: %.6lf sec\n", end3 - begin3);
	

	double begin4 = get_time();
	for (k = 0; k < n; k++){
		for (i = 0; i < n; i++){
			for (j = 0; j < n; j++){
				c[i * n + j] += a[i* n + k] * b[k* n + j];
			}
		}
	}
	double end4 = get_time();
	printf("k-i-j time: %.6lf sec\n", end4 - begin4);


	double begin5 = get_time();
	for (k = 0; k < n; k++){
		for (j = 0; j < n; j++){
			for (i = 0; i < n; i++){
				c[i * n + j] += a[i* n + k] * b[k* n + j];
			}
		}
	}
	double end5 = get_time();
	printf("k-j-i time: %.6lf sec\n", end5 - begin5);
	/*
	// Print C for debugging. Comment out the print before measuring the execution time.
	double sum = 0;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			sum += c[i * n + j];
			// printf("c[%d][%d]=%lf\n", i, j, c[i * n + j]);
		}
	}
	// Print out the sum of all values in C.
	// This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
	printf("sum: %.6lf\n", sum);
	*/
	free(a);
	free(b);
	free(c);
	return 0;
}