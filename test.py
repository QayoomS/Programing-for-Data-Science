import argparse
import statistics
# Noticed that argparse does not have mean() so I imported the statistic to use it.

# Start with basics of Argparse
def main():
    parser = argparse.ArgumentParser(description='Data Analysis')
    parser.add_argument('input_file', help='Please paste the path to the CSV file here')
    args = parser.parse_args()

    try:
        rain_data = []
        temp_data = []
        sun_data = []
# To escape the first 24 lines I am using the below for loop.
        with open(args.input_file) as f:
            for i in range(24):
               next(f)
# Since it is ',' separated file, we have to split the line using ',' as a delimiter
            for line in f:

                database = line.strip().split(',')

# Through tens of tries and fails, I found that there are blank spaces in the database.
# Therefore, I'm replacing them with 0 so that can be converted to float.
                rain_data.append(float(database[2].replace(' ', '0')))
                temp_data.append(float(database[4].replace(' ', '0')))
                sun_data.append(float(database[17].replace(' ', '0')))
# Here we analyze our database
        total_rainfall = sum(rain_data)
        rainy_datapoints = sum(1 for rain in rain_data if rain > 5)
        max_temperature = max(temp_data)
        avg_sunshine = statistics.mean(sun_data)
# Print them in their respective order.
        print(f"1. Total amount of rainfall: {total_rainfall} mm")
        print(f"2. Number of datapoints where rainfall was greater than 5mm: {rainy_datapoints}")
        print(f"3. Maximum temperature ever recorded: {max_temperature} °C")
        print(f"4. Average amount of sunshine per hour: {avg_sunshine} hours")
# When the file path is not provided, the program will give the following error.
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")


if __name__ == "__main__":
    main()