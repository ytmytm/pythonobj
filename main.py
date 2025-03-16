
from CsvExtractor import CsvExtractor
from JsonLoader import JsonLoader
from Deduplicator import Deduplicator
from Job import Job

job = Job.Job(
    input_path = "pracownicy.csv",
    output_path = "imiona.json",
    extractor = CsvExtractor.CsvExtractor(),
    transformer = Deduplicator.Deduplicator("Imię"),
    loader = JsonLoader.JsonLoader(orient="records",index=False,lines=True)
)

job.run()
