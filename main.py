class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def __str__(self):
    return f"{round(self.value, 2)} {self.unit}"

  def __repr__(self):
    return f"Currency({self.value}, {self.unit})"

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
  
  def __str__(self):
    return f"{round(self.value, 2)} {self.unit}"

  def __repr__(self):
    return f"Currency({self.value}, {self.unit})"
  
  def __add__(self,other):
if type(other) == int or type(other) == floar:
  x = (other * Currency.currencies[other,unit] * Currency.currencies[self.unit])
  return Currency(x+self.value, self.unit)
                
      
  

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
