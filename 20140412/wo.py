# coding:utf-8
"""wo moduke. Contains function: words_occur()"""
# interface func
def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    # Inquiry a file name to count
    file_name = input("Enter the name of the file: ")
    # file open and read to push list of words
    f = open(file_name, "r")
    word_list = f.read().split()
    f.close

    # count words in the file
    occur_dict = {}
    for word in word_list:
        occur_dict[word] = occur_dict.get(word, 0) + 1
    print("File %s has %d words (%d are unique)" % (
        file_name, len(word_list), len(occur_dict)))
    print(occur_dict)
if __name__ == '__main__':
    words_occur()
