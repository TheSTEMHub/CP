import check50
import check50.c

@check50.check()
def exists():
    """hello.cpp exists."""
    check50.exists("hello.cpp")
    
@check50.check(exists)
def Towfeq():
    """responds to name Towfeq."""
    check50.run("./hello").stdin("Towfeq").stdout("Towfeq").exit()

@check50.check(exists)
def brian():
    """responds to name Yasmine."""
    check50.run("./hello").stdin("Yasmine").stdout("Yasmine").exit()
