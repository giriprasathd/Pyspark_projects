Easy
How do you read the candy dataset into a pandas DataFrame?
How do you display the first 5 rows of the DataFrame?
How do you get the column names of the DataFrame?
How do you filter the DataFrame to show only candies that contain chocolate?
How do you add a new column to the DataFrame indicating whether the candy is both fruity and contains caramel?
Medium
How do you group the DataFrame by the ‘chocolate’ column and calculate the mean win percentage for each group?
How do you handle missing values in the ‘sugarpercent’ column?
How do you sort the DataFrame by ‘winpercent’ and ‘pricepercent’ in descending order?
How do you apply a custom function to create a new column that categorizes candies into ‘High Sugar’ or ‘Low Sugar’ based on the ‘sugarpercent’?
Hard
How do you pivot the DataFrame to show the average ‘winpercent’ for each combination of ‘chocolate’ and ‘fruity’?
How do you calculate the rolling mean of the ‘winpercent’ column with a window size of 5?
How do you use pandas to read data from an SQL database containing candy sales records?
How do you optimize the performance of this DataFrame for large datasets, such as by using categorical data types or chunking?

Medium
How do you create a new DataFrame that contains only the rows where ‘winpercent’ is above 50%?
How do you use the apply function to normalize the ‘sugarpercent’ column?
How do you concatenate two DataFrames vertically and reset the index?
How do you use the map function to replace values in the ‘chocolate’ column with ‘Yes’ or ‘No’?
How do you use the cut function to bin the ‘pricepercent’ column into 4 equal-sized bins?
Hard
How do you use the groupby and transform functions to add a column that shows the mean ‘winpercent’ for each ‘chocolate’ group?
How do you use the pivot_table function to calculate the sum of ‘winpercent’ for each combination of ‘chocolate’ and ‘caramel’?
How do you use the merge function to perform an outer join on two DataFrames with different column names for the join key?
How do you use the query function to filter the DataFrame for candies that are either fruity or contain caramel, but not both?
How do you use the melt function to transform the DataFrame from wide format to long format, keeping ‘competitorname’ as the identifier variable?

## 

How do you use the value_counts function to count the occurrences of each unique value in the ‘chocolate’ column?
How do you use the replace function to change all instances of ‘Yes’ to 1 and ‘No’ to 0 in the ‘chocolate’ column?
How do you use the isin function to filter the DataFrame for rows where ‘competitorname’ is either ‘Candy A’ or ‘Candy B’?
How do you use the agg function to apply multiple aggregation functions (e.g., mean and sum) to the ‘winpercent’ column grouped by ‘chocolate’?
How do you use the nlargest function to get the top 5 rows with the highest ‘winpercent’?
Hard
How do you use the crosstab function to create a cross-tabulation of ‘chocolate’ and ‘fruity’?
How do you use the applymap function to apply a custom function element-wise across the entire DataFrame?
How do you use the pd.cut function to create a new column that bins the ‘pricepercent’ into custom intervals?
How do you use the pd.get_dummies function to convert categorical variables into dummy/indicator variables?
How do you use the pd.read_json function to read a JSON file into a DataFrame and normalize nested JSON data?