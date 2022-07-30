def numberstring(number):
    if number == 0:
        return "Zero"

    stack = []
    units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    digit = 0
    num = number
    while (num > 0):        
        remainder = num % 10
        num = int(num / 10)
        digit += 1
        if (digit == 2 or digit == 5) and remainder == 1:            
            stack.append(teens[units.index(stack.pop())])
        elif (digit == 2  or digit == 5) and remainder > 1:
            stack.append(tens[remainder])
        else:
            if digit % 3 == 0 and remainder > 0:
                stack.append('Hundred')
            elif digit == 4:
                stack.append('Thousand')
            stack.append(units[remainder])        
    
    stack.reverse()
    return ' '.join(stack)
        

if __name__ == "__main__":
    number = input("Enter number: ")
    print(numberstring(int(number)))