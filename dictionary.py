# DICTIONARY :---
"""1) it is a mapping data type in which each element is represented as key value pair. 
   2) it is mutable data type. 
   3) it is orderd data type element first inserted fatched first.
    NOTE --> if we iterate a dictionar using for loop then data must be fetched in the order , 
             in which it has been inserted.
   4) no indexiing in dictionary. """
# REPRESENTATION OF DICTIONARY-->
d={"one":"monday","two":"tuesday","three":"wednesday"}
print(d)
print(d["two"]) # tuesday
print(d["three"])# wednesday


# PROPERTY OF KEY ---->
""" 1) key should be unique.
    2) new key value pair override ode key value pair.
    3) key must be consist of immutable data type.
    """
# PROPERTY OF VALUE ---->
""" 1) value can be duplicate.
    2) value can be consist of any data ."""

d["four"]="thrusday"
d["five"]="friday"
print(d)
d.update({"six":"saturday"})
d.update({"seven":"sunday"})
print(d)
d1={"eight":"days of week"}
d.update(d1)
print(d)
 