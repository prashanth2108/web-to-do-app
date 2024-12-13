FILEPATH = "to_do_list.txt"

def get_to_do_list(filepath=FILEPATH):
    """
    Read a text file and returns a list which
    returns the to_do_list
    """
    with open(filepath,"r") as file_local:
        to_do_list_local=file_local.readlines()
    return to_do_list_local

def write_to_do_list_files(to_do_list_local,filepath=FILEPATH):
    """
    Write the to_do_items in a text file by getting the to_do_list
    :param to_do_list_local:
    :param filepath:
    :return: None
    """
    with open(filepath,"w") as file_local:
        file_local.writelines(to_do_list_local)
        return None

if __name__ == "__main__":
    print("Hello")
    print(get_to_do_list())