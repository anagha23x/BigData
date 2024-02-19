from mrjob.job import MRJob

class MeanNumbersReducer(MRJob):

    def reducer(self, _, values):
        total_sum, count = 0, 0

        # Aggregate sum and count for each number
        for num, c in values:
            total_sum += num
            count += c

        # Calculate mean and emit the result
        mean = total_sum / count if count > 0 else 0
        yield None, mean

if __name__ == '__main__':
    MeanNumbersReducer.run()
