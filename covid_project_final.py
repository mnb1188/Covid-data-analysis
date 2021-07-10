import sys
import matplotlib.pyplot as plt


def main(filename, countries, parameter):
    countries_data = read_data_for_countries(filename, countries)
    if (parameter == "abc"):
        display_data(countries_data)
    if (parameter == "general"):
        display_data2(countries_data)
    if (parameter == ""):
        display_data(countries_data)


def read_data_for_countries(filename, countries):
    countries_data = dict()

    with open(filename, "r") as f:
        for line in f:
            may_be_country = line.split(",")[1]

            if may_be_country in countries:
                line = line.strip()
                n_of_patients_in_time = get_patients_as_vector(line)

                countries_data[may_be_country] = n_of_patients_in_time

    return countries_data


def display_data(n_of_patients_in_countries):
    # for country, data in n_of_patients_in_countries.items():
    #   plt.semilogy(data, label=country)

    countdict1 = {}
    countdict2 = {}
    countdict3 = {}
    countdict4 = {}
    i = 0

    if (len(n_of_patients_in_countries) > 6):
        for x in n_of_patients_in_countries:
            countdict1[x] = n_of_patients_in_countries[x]
            i = i + 1
            if (i == 6): break
        i = 0

        for x in n_of_patients_in_countries:
            if (i < 6):
                i = i + 1
            else:
                countdict2[x] = n_of_patients_in_countries[x]
                i = i + 1
            if (i == 12): break

    i = 0

    if (len(n_of_patients_in_countries) > 12):
        for x in n_of_patients_in_countries:
            if (i < 12):
                i = i + 1
            elif (i < 18):
                countdict3[x] = n_of_patients_in_countries[x]
                i = i + 1
            if (i == 18): break

    i = 0

    if (len(n_of_patients_in_countries) > 18):
        for x in n_of_patients_in_countries:
            if (i < 18):
                i = i + 1
            elif (i < 24):
                countdict4[x] = n_of_patients_in_countries[x]
                i = i + 1
            if (i == 24): break

    plt.subplot2grid([2, 2], [0, 0])
    for country, data in countdict1.items():
        plt.semilogy(data, label=country)
    plt.xlabel("Days (subsequent date)")
    plt.ylabel("Num of patients in days")
    plt.legend(loc="best")

    if (len(n_of_patients_in_countries) > 6):
        plt.subplot2grid([2, 2], [0, 1])
        for country, data in countdict2.items():
            plt.semilogy(data, label=country)
        plt.xlabel("Days (subsequent date)")
        plt.ylabel("Num of patients in days")
        plt.legend(loc="best")

        if (len(n_of_patients_in_countries) > 12):
            plt.subplot2grid([2, 2], [1, 0])
            for country, data in countdict3.items():
                plt.semilogy(data, label=country)
            plt.xlabel("Days (subsequent date)")
            plt.ylabel("Num of patients in days")
            plt.legend(loc="best")

            if (len(n_of_patients_in_countries) > 18):
                plt.subplot2grid([2, 2], [1, 1])
                for country, data in countdict4.items():
                    plt.semilogy(data, label=country)
                plt.xlabel("Days (subsequent date)")
                plt.ylabel("Num of patients in days")
                plt.legend(loc="best")

    plt.show()


def display_data2(n_of_patients_in_countries):
    val_list = {}
    key_list = {}
    tmplist = {}  # lista wektorów wartości
    sorted_count = {}
    tmpcount = {}
    countdict1 = {}
    countdict2 = {}
    countdict3 = {}
    countdict4 = {}
    i = 0

    countdict0 = {}

    for x in n_of_patients_in_countries:
        countdict0[x] = n_of_patients_in_countries[x]

    tmplist = list(countdict0.values())

    for x in range(len(tmplist)):
        val_list[x] = sum(tmplist[x])
    val_list = list(val_list.values())

    key_list = list(n_of_patients_in_countries.keys())
    ziplist = zip(key_list, val_list)
    countdict0 = {}
    countdict0 = dict(ziplist)

    tmpcount = sorted(countdict0.items(), key=lambda x: x[1], reverse=True)
    for k, v in tmpcount:
        sorted_count[k] = v

    for x in sorted_count:
        for k in n_of_patients_in_countries:
            if (x == k):
                sorted_count[x] = n_of_patients_in_countries[k]

    print(sorted_count)

    if (len(n_of_patients_in_countries) > 6):
        for x in sorted_count:
            countdict1[x] = sorted_count[x]
            i = i + 1
            if (i == 6): break
        i = 0

        for x in sorted_count:
            if (i < 6):
                i = i + 1
            else:
                countdict2[x] = sorted_count[x]
                i = i + 1
            if (i == 12): break

    i = 0

    if (len(n_of_patients_in_countries) > 12):
        for x in sorted_count:
            if (i < 12):
                i = i + 1
            elif (i < 18):
                countdict3[x] = sorted_count[x]
                i = i + 1
            if (i == 18): break

    i = 0

    if (len(n_of_patients_in_countries) > 18):
        for x in sorted_count:
            if (i < 18):
                i = i + 1
            elif (i < 24):
                countdict4[x] = sorted_count[x]
                i = i + 1
            if (i == 24): break

    plt.subplot2grid([2, 2], [0, 0])
    for country, data in countdict1.items():
        plt.semilogy(data, label=country)
    plt.xlabel("Days (subsequent date)")
    plt.ylabel("Num of patients in days")
    plt.legend(loc="best")

    if (len(n_of_patients_in_countries) > 6):
        plt.subplot2grid([2, 2], [0, 1])
        for country, data in countdict2.items():
            plt.semilogy(data, label=country)
        plt.xlabel("Days (subsequent date)")
        plt.ylabel("Num of patients in days")
        plt.legend(loc="best")

        if (len(n_of_patients_in_countries) > 12):
            plt.subplot2grid([2, 2], [1, 0])
            for country, data in countdict3.items():
                plt.semilogy(data, label=country)
            plt.xlabel("Days (subsequent date)")
            plt.ylabel("Num of patients in days")
            plt.legend(loc="best")

            if (len(n_of_patients_in_countries) > 18):
                plt.subplot2grid([2, 2], [1, 1])
                for country, data in countdict4.items():
                    plt.semilogy(data, label=country)
                plt.xlabel("Days (subsequent date)")
                plt.ylabel("Num of patients in days")
                plt.legend(loc="best")

    plt.show()


def get_patients_as_vector(country_data_line):
    n_of_unimportant_column = 4
    n_of_patients_in_time = country_data_line.split(",")[n_of_unimportant_column:]
    n_of_patients_in_time = [int(val) for val in n_of_patients_in_time]

    return n_of_patients_in_time


def validate_args(args):
    if len(args) < 2:
        print("No args with filename and countries", file=sys.stderr)
        exit(-1)


if __name__ == "__main__":
    args = sys.argv
    validate_args(args)

    parameter = args[3]
    county_names = args[2].split(",")
    file_path = args[1]

    main(file_path, county_names, parameter)
