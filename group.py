#!/usr/bin/env python

import sys
sys.path.append('../')
import IPLoM

#!/usr/bin/python

import sys, getopt

def main(argv):
	input_dir    = './'
	output_dir   = './'
	log_file     = 'data.csv'
	maxEventLen  = 120
	step2Support = 0  # The minimal support for creating a new partition (default: 0)
	CT           = 0.35  # The cluster goodness threshold (default: 0.35)
	lowerBound   = 0.25  # The lower bound distance (default: 0.25)
	upperBound   = 0.9  # The upper bound distance (default: 0.9)

	header_column='description'
	try:
		opts, args = getopt.getopt(argv,"hi:o:f:n:m:s:c:l:u:",["iinput_dir=","ooutput_dir=","flog_file=","nheader_column=","mmax_event_len=","sstep2support=","cct=","llower_bound=","uupper_bound="])
	except getopt.GetoptError:
		print 'IPLoM_demo.py -i <input_dir> -o <output_dir> -f <log_file_name> -cn <header_column> -m <max_event_len> -s <step2Support> -c <cct> -l <lower_bound> -u <upper_bound>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'IPLoM_demo.py -i <input_dir> -o <output_dir> -f <log_file_name> -n <header_column> -m <mmax_event_len> -s <step2Support> -c <cct> -l <llower_bound> -u <uupper_bound>'
			sys.exit()
		elif opt in ("-i", "--iinput_dir"):
			input_dir = arg

		elif opt in ("-o", "--ooutput_dir"):
			output_dir = arg

		elif opt in ("-f", "--flog_file"):
			log_file = arg

		elif opt in ("-n", "--nheader_column"):
			header_column = arg

		elif opt in ("-m", "--mmax_event_len"):
			maxEventLen = arg

		elif opt in ("-s", "--sstep2support"):
			step2Support = arg

		elif opt in ("-c", "--cct"):
			CT = arg

		elif opt in ("-l", "--llower_bound"):
			lowerBound = arg

		elif opt in ("-u", "--uupper_bound"):
			upperBound = arg

	print(header_column)
	# log_format   = 'category_key	category_type	ci_name	ci_type	description	event_state	event_type	generated_time	id	node_datacenter	node_environment	node_fqdn	node_id	node_ip	node_type	priority	received_time	resource	severity	source_id	source_name	source_node_datacenter	source_node_fqdn	source_node_id	source_node_ip	source_node_type	tags	tenant_id	time_day	time_half	time_hour	time_quarter	time_week	title	user'#'<Date> <Time> <Pid> <Level> <	
	log_format   = '<category_key><category_type><ci_name><ci_type><description><event_state><event_type><generated_time><id><node_datacenter><node_environment><node_fqdn><node_id><node_ip><node_type><priority><received_time><resource><severity><source_id><source_name><source_node_datacenter><source_node_fqdn><source_node_id><source_node_ip><source_node_type><tags><tenant_id><time_day><time_half><time_hour><time_quarter><time_week><title><user>'#'<Date> <Time> <Pid> <Level> <	maxEventLen  = 120  # The maximal token number of log messages (default: 200)
	regex        = []  # Regular expression list for optional preprocessing (default: [])

	parser = IPLoM.LogParser(log_format=log_format, indir=input_dir, outdir=output_dir,
	                         maxEventLen=maxEventLen, step2Support=step2Support, CT=CT, 
	                         lowerBound=lowerBound, upperBound=upperBound, rex=regex,header_column=header_column)
	parser.parse(log_file)


if __name__ == "__main__":
   main(sys.argv[1:])

