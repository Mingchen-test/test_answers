class Inputnum():
    def keyboard(input):
        num = {'0':' ', '1':' ', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        first = [i for i in num[input[0]]]
        if len(input) == 1:
            for value in range(0,len(first)):
                print (first[value], end=' ')
        else:
            outputs = []
            for y in range(1, len(input)):
                last = input[y]
                if last in [0,1]:
                    continue
                for key in num[last]:
                    outputs += [output+key for output in first]

            for value in range(0,len(outputs)):
                print (outputs[value], end=' ')


if __name__ == '__main__':
    number = input("请输入0-99之间的数字，Input:")
    if 0<=int(number)<100:
        input_number = list(number)
        print ("Output:", end='')
        Inputnum.keyboard(input_number)
    else:
        print ('输入值错误，请输入0-99之间的数字')
