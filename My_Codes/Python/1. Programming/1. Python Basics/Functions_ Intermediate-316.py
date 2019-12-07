## 1. Interfering with the Built-in Functions ##

a_list = [1, 8, 10, 9, 7]
def max(list):
    max_val="No max value returned"
    return max_val
max_val_test_0=max(a_list)
print(max(a_list))
del max
print(max(a_list))

## 3. Default Arguments ##

# INITIAL CODE
def open_dataset(file_name):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset('AppleStore.csv')

print(apps_data[1:6])

def add_value(x):
    return x+25

add_value(15)

## 4. The Official Python Documentation ##

one_decimal = round(3.43,1)
two_decimals = round(0.23321,2)
five_decimals = round(921.2225227,2)
x = round(5999.499999999990000006)
print(x)

## 5. Multiple Return Statements ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header_row = True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header_row:
        return data[1:]
    return data

apps_data = open_dataset(file_name='AppleStore.csv', header_row = True)

print(apps_data[:6])

## 6. Returning Multiple Variables ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    '''if header:
        return data
    else:
        return data'''
    return data
all_data = open_dataset(file_name='AppleStore.csv', header=True)  
header = all_data[0]
apps_data = all_data[1:]

print(type(all_data))
print(type(header))
print(type(apps_data))

## 7. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
apps_data, header = open_dataset()
print(header)
print(apps_data)

## 8. Functions — Code Running Quirks ##

def print_constant():
    x = 3.14
    print(x)
print_constant()
#print(x)
    

## 9. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50
def exponential(x):
    e = 2.72
    print(e)
    return e**x
result = exponential(5)
print(e)
def divide():
    print(a_sum)
    print(length)
    return a_sum/length
result_2 = divide()

print(result)
print(result_2)