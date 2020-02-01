import csv
WRITE_CSV_PATH = "./csv/page_info.csv"

class WriteCSV():
    def __init__(self):
        pass

    def write_csv(self, info):
        try:
            with open(WRITE_CSV_PATH, mode='x', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([info])
        except FileExistsError:
            with open(WRITE_CSV_PATH, mode='a', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([info])

        return 0


if __name__ == "__main__":
    instance = WriteCSV()
    instance.write_csv("hogehoge")
