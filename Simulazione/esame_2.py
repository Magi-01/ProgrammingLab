#capture the raise Excpetion in case of errors (in this case does nothing and sends it to the super class Exception)
class ExamException(Exception):
    pass

#Class that takes a list of numbers and a ratio (defaulted to 1)
#and returns a list of differences on a window of 2 elements ratioed
class Diff:
    def __init__(self,ratio=1):
        #checks if ratio is a number bigger than 0 else raises an ExamException
        if ratio == None:
            raise ExamException('Errore, ratio of None type')
        if type(ratio) == str:
            raise ExamException('Errore, ratio of str type')
        if ratio <= 0:
            raise ExamException('Errore, division by 0 or <0')
        #assigns ratio as attribute of Diff
        self.ratio = ratio


    def compute(self,data):
        #checks if data is empty
        if data == [] or data == None:
            raise ExamException('Errore, lista vuota')

        #in case of a bug, checks if ratio is 0 or none again
        if self.ratio == 0 or self.ratio == None:
            raise ExamException('Errore, bug found.')

        #checks if data is a list
        if not isinstance(data,list):
            raise ExamException('Errore, data is not list')

        #checks if the length of data (list) is <= 1
        #if so raises ExamException because we can't have a ratio of a sigle
        #element
        if len(data) <= 1:
            raise ExamException('Errore, data is not list')

        #checks if the elements inside data are convertable to int or float
        for item in data:
            try:
                int(item) or float(item)
            except:
                raise ExamException('Errore, lista non interamente di interi')

        avg = []
        wind = 1
        k = 0

        #does the computation where for every window of size 2,
        #the 2 elements are subtracted, divide by ratio then
        #stored in a new list called avg that is the returned
        for i in range(len(data)):
            if wind < len(data):
                for j in range (i,wind+1):
                    if k == 0:
                        k = data[j]
                    else:
                        k = k - data[j]
                avg.append((k*(-1))/(self.ratio))
                wind = wind + 1
                k = 0
        if avg == []:
            return data
        return avg

