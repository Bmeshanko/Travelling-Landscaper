import requests
from math import sqrt, pow

def convert_to_coordinates():
    file = open("addresses.txt", "r+")
    outfile = open("coordinates.txt", "w")
    for address in file:
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=AIzaSyDsNJwcIQa1UZg7C05NKBoLoKzYEiUF7jI"
        response = requests.request("GET", url)
        string = response.text
        string = string[string.index("location") + 37:]
        latitude = string[:string.index(",")]
        longitude = string[string.index(",") + 25:string.index("}") - 13]
        outfile.write(latitude + "," + longitude + "\n")

def generate_matrix():
    file = open("clusters.txt", "r+")
    ret = []
    for idx in range(2):
        # Read Clusters lline
        file.readline()
        
        addresses = []
        matrix = []
        for line in file:
            if line == "\n":
                break
            addresses.append(line[:-1])

        for i in addresses:
            distances = []
            for j in addresses:
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + i + "&origins=" + j + "&units=imperial&key=AIzaSyDsNJwcIQa1UZg7C05NKBoLoKzYEiUF7jI"
                response = requests.request("GET", url)
                string = response.text
                string = string[string.index("duration"):]
                string = string[40:string.index(",")]
                mins_str = string[2:string.index("min")]
                if (mins_str.__contains__("hours")):
                    hrs_str = mins_str[:mins_str.index(" ")]
                    mins_str = mins_str[mins_str.index("s") + 2:]
                    mins = int(mins_str) + 60 * int(hrs_str)
                else:
                    mins = int(mins_str)
                distances.append(mins)
            matrix.append(distances)
        ret.append(matrix)
    return ret

def output_file(matrix):
    for i in range(len(matrix)):
        file = open("matrix" + str(i + 1) + ".txt", "w")
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                file.write(str(matrix[i][j][k]) + " "),
            file.write("\n")
        file.write("\n")

matrix = generate_matrix()
output_file(matrix)
#convert_to_coordinates()



