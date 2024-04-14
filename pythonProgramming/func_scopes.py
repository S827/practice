def local_func():
    get_it = 23

    def enclosing_func():
        tri = get_it * 2
        print("enclosing ", tri)
        print("local ", get_it)

    enclosing_func()
    print("local ", get_it)
    # print("enclosing ", tri)
local_func()