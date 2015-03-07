#
# Simple decorator examples
#
def my_decorator(some_func):
    def wrapper():
        print "Something is happening before some_func() is called."
        some_func()
        print "Something is happening after some_func() is called."
    return wrapper


def just_some_function():
    print "Wheee!"

just_some_function = my_decorator(just_some_function)
just_some_function()
# Real world use case: timer


#
# More decorator examples
#
def p_decorate(func):
    def func_wrapper(name):
        print(name)
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

# print get_text("Kitty")

#
# Passing a argument into a decorator
#
def tag_with(tag):
    def tags_decorator(func):
        def func_wrapper(text):
            return "<{tag}>{text}</{tag}>".format(tag=tag, text=func(text))
        return func_wrapper
    return tags_decorator


@tag_with("div")
@tag_with("p")
@tag_with("strong")
def make_text(name):
    return "Hello " + name

# print make_text("Kitty")
