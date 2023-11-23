age = int(input("Enter your age: "))

max_heart_rate = 220 - age

lower_target = 0.5 * max_heart_rate
upper_target = 0.85 * max_heart_rate

print(f"\nYour Maximum Heart Rate: {max_heart_rate} beats per minute")
print(f"Your Target Heart Rate Range: {lower_target:.2f} to {upper_target:.2f} beats per minute")
