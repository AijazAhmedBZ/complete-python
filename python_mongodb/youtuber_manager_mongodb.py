from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.rgtgm.mongodb.net/")

db = client["ytmanager"]

video_collection = db["videos"]
print(video_collection)

def add_video():
    name = input("Enter video name: ")
    video_collection.insert_one({"name": name})
    print("Video added successfully")

def list_videos():
    videos = video_collection.find()
    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']}")

def update_video():
    name = input("Enter video name to update: ")
    new_name = input("Enter new video name: ")
    video_collection.update_one({"name": name}, {"$set": {"name": new_name}})
    print("Video updated successfully")

def delete_video():
    name = input("Enter video name to delete: ")
    video_collection.delete_one({"name": name})
    print("Video deleted successfully")


def main():
    while True:
        print("1. Add video")
        print("2. List videos")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_video()
        elif choice == "2":
            list_videos()
        elif choice == "3":
            update_video()
        elif choice == "4":
            delete_video()
        elif choice == "5":
            break
        else:
            print("Invalid choice")
 
if __name__ == "__main__":
    main()