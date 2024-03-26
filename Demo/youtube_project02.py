import sqlite3

conn = sqlite3.connect('TEST.db')

cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
   )
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    video_id = cursor.lastrowid  # Get the newly generated id 
    print("Video added successfully with ID:", video_id)


def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id) )
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()
    

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit an App")

        choice = input("Enter Your Choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video nmae : ")
            time = input("Enter the video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update : ")
            name = input("Enter the video nmae : ")
            time = input("Enter the video time : ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("Enter video ID to deleted : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ...")
    
    conn.close()
if __name__ == "__main__":
    main()