from mrjob.job import MRJob
import re

class MeanNumbersMapper(MRJob):

    def mapper(self, _, line):
        # Extract numerical values using regular expression
        numbers = re.findall(r'\b\d+\b', line)
        
        # Emit each number with count 1
        for num in numbers:
            yield None, (float(num), 1)

if __name__ == '__main__':
    MeanNumbersMapper.run()
