surfaceN = int(input())
for _ in range(surfaceN):
    input()
while True:
    try:
        X, Y, hSpeed, vSpeed, fuel, rotate, power = map(int, input().split())
        thrust_power = 0
        height_threshold = 300  
        if Y < height_threshold:
            thrust_power = 4  
        else:
            if vSpeed < -40:
                thrust_power = min(4, fuel)  
            elif -40 <= vSpeed < -20:
                thrust_power = min(3, fuel)  
            elif -20 <= vSpeed < 0:
                thrust_power = min(2, fuel)  
            else:
                thrust_power = 0
        thrust_power = max(0, min(thrust_power, fuel))
        print(0, thrust_power)
    except ValueError:
        print("Error: Invalid input")
