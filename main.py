import argparse

from CsvExtractor import CsvExtractor
from JsonLoader import JsonLoader
from Deduplicator import Deduplicator
from Job import Job

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Job")
    parser.add_argument('-i', '--input_path', type=str, help="CSV input",required=True)
    parser.add_argument('-o', '--output_path', type=str, help="JSON output", default="output.json")
    parser.add_argument('-f', '--fields', action='append', help="deduplication fields, e.g -f <field1> -f <field2> ", required=True)
    parser.add_argument('--orient', type=str, default="records")
    parser.add_argument('--index', type=bool, default=False)
    parser.add_argument('--lines', type=bool, default=True)
    args = parser.parse_args()

    job = Job.Job(
      input_path = args.input_path,
      output_path = args.output_path,
      extractor = CsvExtractor.CsvExtractor(),
      transformer = Deduplicator.Deduplicator(args.fields),
      loader = JsonLoader.JsonLoader(orient=args.orient,index=False,lines=True)
    )

    job.run()
