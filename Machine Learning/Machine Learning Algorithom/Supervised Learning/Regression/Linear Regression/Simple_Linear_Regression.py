import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data
house_sizes = np.array([1400, 1600, 1700, 1875])  # House sizes in square feet
prices = np.array([245000, 312000, 329000, 348000])  # Prices in dollars
house_labels = ['House A', 'House B', 'House C', 'House D']  # Labels for the houses

# Reshape the data (required for sklearn)
house_sizes = house_sizes.reshape(-1, 1)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(house_sizes, prices)

# Predict the price of a new house
new_house_size = np.array([[1500]])  # Size of the new house
predicted_price = model.predict(new_house_size)
print("the predicted price is ",predicted_price)

# Plot the data points with labels
for i in range(len(house_sizes)):
    plt.scatter(house_sizes[i], prices[i], label=house_labels[i])

# Plot the regression line
plt.plot(house_sizes, model.predict(house_sizes), color='red', linewidth=2, label='Linear Regression Line')

# Plot the new house size and predicted price
plt.scatter(new_house_size, predicted_price, color='green', marker='x', s=100, label='Predicted Price')

# Set labels and legend
plt.xlabel('House Size (sq. ft.)')
plt.ylabel('Price ($)')
plt.legend()

# Show the plot
plt.title('Linear Regression for House Prices')
plt.grid(True)
plt.show()
