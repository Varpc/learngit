# div.py

def div(a, b):
    try:
        ans = a / b
    except ZeroDivisionError as e:
        print('error:', e)
        return None
    return ans
