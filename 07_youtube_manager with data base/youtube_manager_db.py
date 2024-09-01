import sqlite3

connection = sqlite3.connect('youtube_videos.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS youtube_videos
                  (id INTEGER PRIMARY KEY, title TEXT NOT NULL, duration TEXT)''')

def add_video(title, duration):
    cursor.execute("INSERT INTO youtube_videos (title, duration) VALUES (?, ?)", (title, duration))
    print("\nVideo added successfully:")

def get_all_videos():
    cursor.execute("SELECT * FROM youtube_videos")
    print("\nAll videos in the database:")
    print("\nID\tTitle\tDuration")
    return cursor.fetchall()


def update_video(video_id, title, duration):
    cursor.execute("UPDATE youtube_videos SET title = ?, duration = ? WHERE id = ?", (title, duration, video_id))
    print("\nVideo updated successfully")

def delete_video(video_id):
    cursor.execute("DELETE FROM youtube_videos WHERE id = ?", (video_id,))
    print("\nVideo deleted successfully")

def main():
    print("\nYoutube Manager App using SQLite Database")
    
    while True:
        print("\n1. Add a video")
        print("2. List all videos")
        print("3. Update a video")
        print("4. Delete a video")
        print("\n5. Exit")
    
        choice = input("Enter your choice: ")
    
        if choice == '1':
            title = input("Enter video title: ")
            duration = (input("Enter duration: "))
            add_video(title, duration)

        elif choice == '2':
            videos = get_all_videos()
            for video in videos:
                print(f"ID: {video[0]}, Title: {video[1]}, Duration: {video[2]}")

        elif choice == '3':
            video_id = int(input("Enter video ID to update: "))
            title = input("Enter new video title: ")
            duration = input("Enter new number of views: ")
            update_video(video_id, title, duration)

        elif choice == '4':
            video_id = int(input("Enter video ID to delete: "))
            delete_video(video_id)

        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()