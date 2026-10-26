to_meters = {
    "mile": 1609.34,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "kilometer": 1000.0,
    "meter": 1.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
}
# (наприклад, 15.5 foot in mile)
data = input("Введіть рядок: ").split()
value = float(data[0])
from_unit = data[1]
to_unit = data[3]

value_in_meters = value * to_meters[from_unit]
result = value_in_meters / to_meters[to_unit]

print(f"{result:.2e}")