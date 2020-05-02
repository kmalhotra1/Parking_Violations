import argparse
from src.bigdata1.api import get_results, write_results


if __name__ == "__main__":
	# parse arguments to get parameters from input
	parser = argparse.ArgumentParser()
	parser.add_argument("--page_size", type=int)
	parser.add_argument("--num_pages", type=int)
	parser.add_argument("--output")
	args = parser.parse_args()
	
	write_results(args.output)
	get_results(args.page_size, args.num_pages, args.output)


