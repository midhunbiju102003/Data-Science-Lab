import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Cherry", "Mango", "Grapes"]
sales = [90, 20, 30, 40, 40]

# Bar Chart
plt.bar(fruits, sales, color="yellow", edgecolor="red")

plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Fruits Sales - Bar Chart")
plt.show()

# Scatter Plot
plt.scatter(fruits, sales, ls="--",marker="s",  edgecolors="red", s=10)
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Fruits Sales - Scatter Plot")
plt.show()
