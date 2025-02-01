from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("local").getOrCreate()  # type: ignore

dummy_data = [(1, 100), (2, 200), (3, 300)]
columns = ["id", "salary"]

df = spark.createDataFrame(dummy_data, columns)
df.createOrReplaceTempView("Employee")

result_all = spark.sql("SELECT * FROM Employee")
print("All employees:")
result_all.show()

query = """
select distinct salary as SecondHighestSalary from Employee order by salary desc limit 1 offset 1 
"""

second_highest_salary = spark.sql(query)
print("Second higest salary:")
second_highest_salary.show()

dummy_data_2 = [(1, 100)]
df2 = spark.createDataFrame(dummy_data_2, columns)
df2.createOrReplaceTempView("Employee")

second_highest_salary = spark.sql(query)
print("Second higest salary single employee:")
second_highest_salary.show()
