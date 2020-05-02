import argparse
from src.bigdata1.api import get_results


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--page_size", type=int)
	parser.add_argument("--num_pages", type=int)
	parser.add_argument("--output")
	args = parser.parse_args()

	get_results(args.output, args.page_size, args.num_pages)

