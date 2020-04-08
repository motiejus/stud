from math import cos, tan, asin, sqrt
from deg import deg

L12 = 396.942
B12 = deg('40-19-21.0')
D12 = L12 * cos(B12)

L23 = 421.159
H23 = 25.771
B23 = asin(H23 / L23)
D23 = sqrt(L23**2 - H23**2)

L34 = 294.911
B34 = deg('31-56-51.2')
D34 = L34 * cos(B34)

H41 = 77.226
B41 = deg('38-45-7.8')
D41 = H41 / tan(B41)

print("D12 = %4.3f""" % D12)
print("D23 = %4.3f""" % D23)
print("D34 = %4.3f""" % D34)
print("D41 = %4.3f""" % D41)
print("Sum = %4.3f""" % (D12 + D23 + D34 + D41))
