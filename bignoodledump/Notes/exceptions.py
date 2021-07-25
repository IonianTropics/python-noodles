def divide(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        print("Error: Divide by zero")
    except TypeError:
        print("Error: Types")
    except ValueError:
        print("Values")
    except:     # catches all errors, but is considered unpythonic
        print("all other errors")
    else:
        print("No error occurred")
    finally:
        print("Always prints")


def dblpwr(a):
    if a == 0:
        raise ValueError


if __name__ == '__main__':
    assert 2+2 == 4    # unit test, raises an error if value is false
