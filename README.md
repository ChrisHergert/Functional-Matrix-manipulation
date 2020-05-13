# Functional-Matrix-manipulation
For research project into Restart-avoiding techinques with Dr. R. Morgan at Baylor University department of Mathematics, 2017.
This library presents a basic implementation of the matric class available in MATLAB. While a similar implementation is available via the SciPy library, we needed to be able to calculate elapsed time for various computations at a lower level than is available via SciPy. This library allows integration on a functional level with the logging module to calculate time elapsed for various internal calculations relative to matrix size and sparsity.
In previous use, this library was compiled via Cython and integrated into a MATLAB simulation setup via Simulink.
