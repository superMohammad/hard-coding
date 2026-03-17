'''
### Problem 86 — Delivery Fee Wizard

**Scenario:** Write a function that calculates delivery fee based on city and order amount.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.
'''

delivery_fees = {
    'Makkah':0.15,
    'Jeddah':0.20,
    'Riyadh':0.30
}

def calc(city,order_amount):
    try:
        if not isinstance(city,str):
            raise TypeError('enter a valid data type , only string')
        
        if not isinstance(order_amount,(float,int)) or isinstance(order_amount, bool):
            raise TypeError('enter a valid data type , only float or int')
        return f"{delivery_fees[city] * order_amount} SAR"
    
    except KeyError as e:
        raise KeyError(f"City '{city}' not found in delivery fees")
    except Exception as e:
        raise e
    
print(calc('Riyadh',100))
