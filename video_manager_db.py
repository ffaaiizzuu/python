import sqlite3

# Connect to the database
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

# Function to list videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

# Function to add a video
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

# Function to update a video
def update_video(new_name, new_time, video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

# Function to delete a video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# Main application loop
def main():
    while True:
        print("\nYoutube manager app with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = int(input("Enter video ID: "))
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(name, time, video_id)
        elif choice == '4':
            video_id = int(input("Enter video ID: "))
            delete_video(video_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()

if __name__ == "__main__":
    main()