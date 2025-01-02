"""The distance between two cities is input through the keyword . 
write a program to convert and 
print this distance into meter, feet, inches and centimeters"""

#Distance in meters= Distance in kilometers × 1000
#Distance in feet= Distance in kilometers × 3280.84
#Distance in inches= Distance in kilometers × 39370.1
#Distance in centimeters= Distance in kilometers × 100000

distance=float(input("Enter the distance between two cities"))

dist_mtr=distance*1000
dist_feet=distance* 3280.84
dist_inch=distance* 39370.1
dist_centim=distance* 100000

print("Distance between two cities is :- ",distance)
print(dist_mtr)
print(dist_feet)
print(dist_inch)
print(dist_centim)