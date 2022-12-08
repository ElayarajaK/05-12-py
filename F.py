
from decimal import DivisionByZero


try:
    i=10/0
except DivisionByZero as msg:
    print(msg);

print("End");
    