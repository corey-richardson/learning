# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())
# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed,codecademy.score)
plt.title("Completed lessons against Score")
plt.xlabel("Completed")
plt.ylabel("Score")
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula("score ~ completed", data = codecademy)
results = model.fit()
print(results.params)
# Intercept interpretation:
# - Someone who has completed 0 lessons will get 13.2 as their score
# Slope interpretation:
# - For every lesson completed, score increases by 1.3
# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.title("Completed lessons against Score with regression line")
plt.xlabel("Completed")
plt.ylabel("Score")
plt.plot(codecademy.completed, results.predict(codecademy))
# Show then clear plot
plt.show()
plt.clf()
# Predict score for learner who has completed 20 prior lessons
completed = {"completed":20}
pred_score = results.predict(completed)
print(pred_score)
# Calculate fitted values
fitted_values = results.predict(codecademy)
print(fitted_values)
# Calculate residuals
residuals = codecademy.score - fitted_values
print(residuals)
# Check normality assumption
plt.hist(residuals)
plt.title("Residuals - Normality check")
# Show then clear the plot
plt.show()
plt.clf()
# Check homoscedasticity assumption
plt.axhline(y=0,color="black")
plt.scatter(fitted_values, residuals)
plt.title("Homoscedasticity assumption check")
# Show then clear the plot
plt.show()
plt.clf()
# Create a boxplot of score vs lesson
sns.boxplot(data=codecademy,x="lesson",y="score")
plt.title("Boxplot comparing scores for each lesson")
plt.xlabel("Lesson")
plt.ylabel("Score")
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula("score ~ lesson", data = codecademy)
results = model.fit()
print(results.params)
# Calculate and print the group means and mean difference (for comparison)
lesson_a_mean = np.mean(codecademy.score[codecademy.lesson== "Lesson A"])
lesson_b_mean = np.mean(codecademy.score[codecademy.lesson== "Lesson B"])
print("Lesson A Mean: %f" % lesson_a_mean)
print("Lesson B Mean: %f" % lesson_b_mean)
# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(data=codecademy,x="score",y="completed",hue="lesson")
plt.show()
plt.clf()
