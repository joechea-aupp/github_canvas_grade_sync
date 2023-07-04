from dir import list_csv
from migrate import migrate_classroom_to_canvas


# menu section
print("---------------------------------------------")
print("Chose specific file for canvas and classroom")
print("---------------------------------------------")

for index, file in enumerate(list_csv()):
    print(f"{index+1} - {file}")

print("\n")

input_canvas = input("Choose canvas file: ")
input_classroom = input("Choose classroom file: ")

# print chosen file for user to confirm
print("canvas file: ", list_csv()[int(input_canvas) - 1])
print("classroom file: ", list_csv()[int(input_classroom) - 1])

# start the migration
migrate = migrate_classroom_to_canvas(
    list_csv()[int(input_canvas) - 1], list_csv()[int(input_classroom) - 1])

print("\n")

if migrate:
    print(f"{migrate} data imported to canvas_import.csv")
