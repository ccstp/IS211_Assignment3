import argparse
import urllib.request
import csv
import re
import datetime


def downloadData(url):
    """Download and decode data from url and return a list of all lines in file"""
    with urllib.request.urlopen(url) as response:
        data = [d.decode('utf-8') for d in response.readlines()]
        return data


def processData(data):
    """Process data using CSV module"""
    csv.reader(data)


def searchImages(data):
    """Search for image files"""
    content = csv.reader(data)
    row_count = 0
    img_count = 0
    for row in content:
        row_count += 1
        images = re.search('PNG|JPG|GIF$', row[0], re.IGNORECASE)
        if bool(images):
            img_count += 1

    percent_images = float(round(img_count / row_count * 100, 1))

    print(f'Image requests account for {percent_images}% of all requests.')


def findBrowser(data):
    """Determine most popular browser"""
    content = csv.reader(data)

    browsers_dict = {
        'Chrome': 0,
        'Firefox': 0,
        'Internet Explorer': 0,
        'Safari': 0
    }

    for row in content:
        c = re.search('Chrome/*.*' + 'Safari/*.*', row[2], re.IGNORECASE)
        f = re.search('Firefox/*.*$', row[2], re.IGNORECASE)
        i = re.search('MSIE', row[2], re.IGNORECASE)
        s = re.search('^(?!.*Chrome).*Safari/*.*$', row[2], re.IGNORECASE)
        if bool(c):
            browsers_dict['Chrome'] += 1
        elif bool(f):
            browsers_dict['Firefox'] += 1
        elif bool(i):
            browsers_dict['Internet Explorer'] += 1
        elif bool(s):
            browsers_dict['Safari'] += 1

    # for key, value in browsers_dict.items():
        # print(key, value)

    most_popular = max(browsers_dict, key=browsers_dict.get)
    most_hits = browsers_dict.get(most_popular)

    print(f'{most_popular} is the most popular browser with {most_hits} hits.')


def extractHours(data):
    """Output list of hours of the day sorted by total number of hits in descending order """
    print()
    print('Extra Credit')

    content = csv.reader(data)

    hours_dict = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                  '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0,
                  '22': 0, '23': 0, }

    for row in content:
        formatted_datetime = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S').hour
        if formatted_datetime == 0:
            hours_dict['00'] += 1
        elif formatted_datetime == 1:
            hours_dict['01'] += 1
        elif formatted_datetime == 2:
            hours_dict['02'] += 1
        elif formatted_datetime == 3:
            hours_dict['03'] += 1
        elif formatted_datetime == 4:
            hours_dict['04'] += 1
        elif formatted_datetime == 5:
            hours_dict['05'] += 1
        elif formatted_datetime == 6:
            hours_dict['06'] += 1
        elif formatted_datetime == 7:
            hours_dict['07'] += 1
        elif formatted_datetime == 8:
            hours_dict['08'] += 1
        elif formatted_datetime == 9:
            hours_dict['09'] += 1
        elif formatted_datetime == 10:
            hours_dict['10'] += 1
        elif formatted_datetime == 11:
            hours_dict['11'] += 1
        elif formatted_datetime == 12:
            hours_dict['12'] += 1
        elif formatted_datetime == 13:
            hours_dict['13'] += 1
        elif formatted_datetime == 14:
            hours_dict['14'] += 1
        elif formatted_datetime == 15:
            hours_dict['15'] += 1
        elif formatted_datetime == 16:
            hours_dict['16'] += 1
        elif formatted_datetime == 17:
            hours_dict['17'] += 1
        elif formatted_datetime == 18:
            hours_dict['18'] += 1
        elif formatted_datetime == 19:
            hours_dict['19'] += 1
        elif formatted_datetime == 20:
            hours_dict['20'] += 1
        elif formatted_datetime == 21:
            hours_dict['21'] += 1
        elif formatted_datetime == 22:
            hours_dict['22'] += 1
        elif formatted_datetime == 23:
            hours_dict['23'] += 1

    sorted_hours_dict = sorted(hours_dict.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_hours_dict:
        print(f'Hour {key} has {value} hits')


def main(url):
    print(f'Running main with URL = {url}...')

    web_data = downloadData(url)

    processData(web_data)

    searchImages(web_data)

    findBrowser(web_data)

    extractHours(web_data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)