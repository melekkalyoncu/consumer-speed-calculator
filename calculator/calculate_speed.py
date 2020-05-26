import config
import zipfile

consumer_name = config.consumer_name
zip_file_path = config.zip_file_path
count_of_processed_file = 0
sum_of_each_average = 0

def find_matchers():
    zip_file = zipfile.ZipFile(zip_file_path, 'r')
    file_paths_list = zip_file.namelist()

    for file_path in file_paths_list:
        if file_path.endswith('.txt'):
            content = zip_file.read(file_path).split('\n')
            matching = [s for s in content if consumer_name in s]
            if matching != '' and matching is not None:
                calculate_average_for_one(matching)


def calculate_average_for_one(matching):
    global count_of_processed_file
    global sum_of_each_average
    consumer_array = []
    average = 0

    for matched_line in matching:
        splitted_matches = matched_line.split(' - ')
        for item in splitted_matches:
            try:
                item = float(item)
                consumer_array.append(item)
            except ValueError:
                pass

        if len(consumer_array) == 2:
            if consumer_array[0] != 0.0 and consumer_array[1] != 0.0:
                count_of_processed_file += 1
                average = float(consumer_array[1] / consumer_array[0])

    sum_of_each_average += average

def calculate_total_average():
    result = float(sum_of_each_average / count_of_processed_file)

    print 'Sum of average speed of {} is {:.2f} and processed file count is {}.'.format(consumer_name, sum_of_each_average, count_of_processed_file)
    print '{} consumes {:.2f} number of messages per second.'.format(consumer_name, result)


if __name__ == '__main__':
    find_matchers()
    calculate_total_average()
