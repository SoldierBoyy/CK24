disk_space = 1.44  # Мегабайт

char_disk_space = 4
chars_in_line = 25 * char_disk_space
lines_on_paper = 50 * chars_in_line
book_space_in_bytes = 100 * lines_on_paper  # papers * lines_on_paper (размер в байтах)

book_space_in_kilobytes = book_space_in_bytes / 1024
book_space_in_megabytes = book_space_in_kilobytes / 1024

print(f"Количество книг, помещающихся на дискету: {int(disk_space // book_space_in_megabytes)}")
