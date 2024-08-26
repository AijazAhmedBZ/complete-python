
import json

file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name, "r") as file:
            print("Loading data from file")
            return json.load(file)
             
    except FileNotFoundError:
            print("File not found")
            return []
    finally:
        print("\n Data loaded successfully")    

def save_data_helper(videos):
    with open(file_name, "w") as file:
        print("Saving data to file")
        json.dump(videos, file)
        print("Data saved successfully")

def list_all_youtube_videos(videos):
    print("\n")
    print("*" * 40)
    print("\tList of all youtube videos")
    print("*" * 40)
    print("\n")

    print("S.No\tName\tDuration")
    print("-" * 40)
    for index, video, in enumerate(videos, start=1):
        print(f"{index}. \t{video['name']}, \tDuration: {video['time']}")

def add_video(video):
    name =input("Enter Video Name: ")
    time = input("Enter video time: ")
    video.append({"name": name, "time": time})
    save_data_helper(video)

def update_video(video):
    list_all_youtube_videos(video)
    index =int(input("Enter the video number to update: "))
    if 1 <= index <= len(video):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        video[index - 1] = {"name": name, "time": time}
        save_data_helper(video)
    else:
        print("Invalid video number")

def delet_video(video):
    list_all_youtube_videos(video)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(video):
        del video[index - 1]
        save_data_helper(video)
    else:
        print("Invalid video number")

def main():
    
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube videos details ")
        print("4. Delete a a youtube videos ")
        print("5. Exit the app ")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_all_youtube_videos(videos)
                # print("Listing all youtube videos")
            case 2:
                add_video(videos)
                print("Adding a youtube videos")
            case 3:
                update_video(videos)
                print("Updating a youtube videos")
            case 4:
                delet_video(videos)
                print("Deleting a youtube videos")
            case 5:
                print("Exiting the app")
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()