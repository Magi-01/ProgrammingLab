class ExamException(Exception):
    pass


class MovingAverage:
    def __init__(self,window):
        if not isinstance(window,int):
            raise ExamException('Division by non integer.')
        if window < 1:
            raise ExamException('Window < 1.')
        self.window = window

    def compute(self,data):
        if data == [] or data == None or not isinstance(self.window,int):
            raise ExamException('Error, list is empty')

        if not isinstance(data,list):
            if self.window > 1:
                raise ExamException('Error, data is not a list')
            return data

        if self.window > len(data):
            raise ExamException('Error, window > than length of data')

        if self.window == 0:
            raise ExamException('Error, bug found (window not checked on init)')

        if self.window == 1:
            return data
            
        if self.window < 0:
            self.window *= -1

        avg = []
        wind = self.window

        for i in range(len(data)):
            if wind <= len(data):
                k = sum(data[i:wind])
                avg.append(k/self.window)
                wind = wind + 1
        if avg == []:
            return data
        return avg

mavg = MovingAverage(5)
#self.assertEqual(mavg.compute([2,4,8,16]), [3,6,12])
print(mavg.compute([2,4,8,16,32]))