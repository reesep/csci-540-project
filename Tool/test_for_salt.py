


def test(da_list):

    len_og = len(da_list)
    no_duplicates = len(set(da_list))

    if len_og != no_duplicates:
        print("WARNING: Duplicate hashes found. Consider adding salt to authentication system")




if __name__ == "__main__":
    test()