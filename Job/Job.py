
class Job:
    def __init__(self, input_path, output_path, extractor, transformer, loader):
        self.input_path = input_path
        self.output_path = output_path
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
    
    def run(self):
        source_data = self.extractor.extract(self.input_path)
        transformed_data = self.transformer.transform(source_data)
        self.loader.load(transformed_data, self.output_path)
