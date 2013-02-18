from __future__ import print_function
import timeit
from instancevars import *

class AutoVars(object):
	@instancevars
	def __init__(self, arg1, arg2, arg3, arg4, arg5=5, arg6=6):
		pass

class ExplicitVars(object):
	def __init__(self, arg1, arg2, arg3, arg4, arg5=5, arg6=6):
		self.arg1 = arg1
		self.arg2 = arg2
		self.arg3 = arg3
		self.arg4 = arg4
		self.arg5 = arg5
		self.arg6 = arg6

def bench_microseconds(stmt):
	iterations = 10000
	bench_import = 'import instancevars_bench as bench\n'
	total = timeit.timeit(bench_import + stmt, number=iterations)
	return total * 1000000 / iterations

if __name__ == '__main__':
	auto_time = bench_microseconds('bench.AutoVars(1, 2, arg3=3, arg4=4)')
	explicit_time = bench_microseconds('bench.ExplicitVars(1, 2, arg3=3, arg4=4)')

	print("The microseconds per iteration for '@instancevars' was: %.04f" % auto_time)
	print("The microseconds per iteration for explicit init. was: %.04f" %  explicit_time)
	print("Explicit vars are %.04f times faster than using '@instancevars'" % (auto_time / explicit_time))
