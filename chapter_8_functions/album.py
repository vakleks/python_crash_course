def make_album(artist_name, album_name):
    """Return dictionary with info about music album."""
    album = {'artist': artist_name, 'album': album_name}
    return album

while True:
    print("\nAlbum info:")
    print("(input 'exit' at any time to quit)")

    artist_name = input("Artist is: ")
    if artist_name == 'exit':
        break

    album_name = input("Album is: ")
    if album_name == 'exit':
        break

    album_info = make_album(artist_name, album_name)
    print(album_info)
    