'''
Created on 24Jul.,2017

@author: DINESHKB
'''

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
            
        print (input_data)
        import re
        m = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', input_data)
        print(len(m))
        for mt in m: 
            print(mt[4:5])
    else:
        print('This study requires an input file.')
        
    
    