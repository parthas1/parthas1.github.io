words = [
    "CPU",
	"GPU",
	"SIMD",
	"OpenMP",
    "TBB",
    "MPI",
    "CUDA",
    "HIP",
    "OpenCL",
    "SYCL",
    "DPC++",
    "parallel",
    "Memory",
    "Cache",
    "Numba",
    "Halide",
    "Codegen",
    "Thoroughput",
    "Latency",
    "AVX",
    "SSE",
	"supercomputing",
	"distributed",
	"multicore",
	"manycore",
	"shared memory",
	"threads",
	"multiprocessing",
	"vectorized",
	"instruction parallel"
]
weights = [10] * len(words)
colors = [""] * len(words)
urls = [""] * len(words)

def wrap(w):
	return r'"' + w + r'"'

def custom_format(w, word, c, u):
	delimit = ";"
	return str(w) + delimit + wrap(word) + delimit + wrap(c) + delimit + wrap(u)

associations = map(lambda t : custom_format(*t), zip(weights, words, colors, urls))
for association in associations:
	print(association)
