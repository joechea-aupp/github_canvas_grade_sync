import csv


def migrate_classroom_to_canvas(canvas_file, classroom_file) -> int:
    """

    :param canvas_file:
    :param classroom_file:

    """
    # open canvas.csv and read the data, store its data in variable canvas
    # open classroom.csv and read the data, store its data in variable classroom
    with open(canvas_file, "r", encoding="utf-8") as file:
        canvas = csv.reader(file)
        canvas = list(canvas)

    with open(classroom_file, "r", encoding="utf-8") as file:
        classroom = csv.reader(file)
        classroom = list(classroom)

    # empty list to store the data that will be imported to canvas
    import_data = []

    # loop through the data in canvas[2:] and classroom[1:]
    # if canvas index 0 is equal to classroom index 4 print canvas data
    for canvas_data in canvas[2:]:
        for classroom_data in classroom[1:]:
            if canvas_data[0] == classroom_data[4]:
                # print(canvas_data)
                canvas_data[5] = classroom_data[8]
                import_data.append(canvas_data)

    # add canvas first and second row to import_data as index 0 and 1
    import_data.insert(0, canvas[0])
    import_data.insert(1, canvas[1])

    # save import_data to canvas_import.csv
    with open(
        "canvas_import.csv", "w", newline="", encoding="utf-8"
    ) as canvas_import_file:
        writer = csv.writer(canvas_import_file)
        writer.writerows(import_data)

    return len(import_data) - 2
