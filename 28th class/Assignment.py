import numpy as np


temperature_random = np.random.randint(25, 51, size=(10, 7))


print(temperature_random)
print("Random Temperature Array (10x7):")
print(temperature_random)


avg_temp = np.mean(temperature_random, axis=1)

print("\nAverage Temperature of Each City:")
for i, avg in enumerate(avg_temp):
    print(f"City {i} : {avg:.2f}")

hottest_city = np.argmax(avg_temp)
coldest_city = np.argmin(avg_temp)

print("\n Hottest City:")
print(f"City {hottest_city} with Avg Temp = {avg_temp[hottest_city]:.2f}")

print("\n Coldest City:")
print(f"City {coldest_city} with Avg Temp = {avg_temp[coldest_city]:.2f}")
