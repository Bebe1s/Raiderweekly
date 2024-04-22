def add_song(songs, song_name):
    songs.append(song_name)

def display_sorted_songs(songs):
    sorted_songs = sorted(songs)
    print("List of Songs (Alphabetical Order):")
    for song in sorted_songs:
        print(song)

def main():
    songs = []

    while True:
        print("\n1. Add Song")
        print("2. Display Songs (Alphabetical Order)")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            song_name = input("Enter the name of the song: ")
            add_song(songs, song_name)
        elif choice == '2':
            display_sorted_songs(songs)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#!!!ACKNOWLAGEMENTS!!! This code was reviewd and subsiqently edited by chatGPT. !!!ACKNOWLAGEMENTS!!!