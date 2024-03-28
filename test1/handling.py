def causeError():
    g=9
    o=6
    try:
        1/1
    except Exception:
        print('what the teeeeeet!')
    finally:
        print(f'{o}1{g}')

def err(r):
    try:
        return 1/r
    except TypeError:
        print('there was a type error!')
    except ZeroDivisionError:
        print('there was a zero diuvision error!')
    except Exception:
        print('there was some sort of error')

def handleException(func):
    def errs(*args):
        try:
            func(*args)
        except TypeError:
            print('there was a type error!')
        except ZeroDivisionError:
            print('there was a zero diuvision error!')
        except Exception:
            print('there was some sort of error')
    return errs

@handleException
def cozErr():
    return 1/0

