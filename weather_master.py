"""
File: weather_master.py
Name: JeffreyWen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# Constant used to signal the end of input
END_NUMBER = -100


def main():
    # Introduction message
    print("stanCode \"Weather Master 4.0\"!")

    # Ask for the first temperature
    data = int(input("Next temperature: (or -100 to quit)? "))

    # If user quits immediately
    if data == END_NUMBER:
        print("No temperatures were entered.")
    else:
        # Initialize tracking variables using the first input
        maximum_temperature = data
        minimum_temperature = data
        total = data  # for average calculation
        number = 1  # number of entries
        report = 0  # count of cold days (<16°C)

        # Check if the first temperature is a cold day
        if data < 16:
            report += 1

        # Keep reading temperatures until sentinel is entered
        while True:
            data = int(input("Next temperature: (or -100 to quit)? "))

            # Exit loop if sentinel value is entered
            if data == END_NUMBER:
                break

            # Count cold day if temperature < 16
            if data < 16:
                report += 1

            # Update maximum and minimum temperatures
            if data > maximum_temperature:
                maximum_temperature = data
            elif data < minimum_temperature:
                minimum_temperature = data

            # Update total and entry count
            number += 1
            total += data

        # Print final results
        print("Highest temperature = " + str(maximum_temperature))
        print("Lowest temperature = " + str(minimum_temperature))
        print("Average = " + str(total / number))
        print(str(report) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
