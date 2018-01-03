import matplotlib.pyplot as plt;
import re;
import numpy as np;
import sys, getopt;

def ping_show(pinglog):
	time_str=[]
	pattern = re.compile(".*time=(.+?) ms.*")
	f = open(pinglog, 'r')
	for line in f:
		time_str+=pattern.findall(line)
	time_np= (np.array(time_str)).astype(np.float)
	x=range(0,time_np.size)
	y=time_np
	plt.title('Ping latency')
	plt.ylabel('Y time (ms)')
	plt.xlabel('X seq')
	plt.plot(x,time_np)
	plt.show()

def main(argv):
	ping_show(argv[0])

if __name__ == '__main__':
	main(sys.argv[1:])
