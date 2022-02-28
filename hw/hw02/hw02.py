from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    term -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    ret = 1
    for i in range(1,n+1):
        ret *= term(i)
    return ret

def square(x):
    return x * x


def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    return combiner(base,term(1),term(2)...,term(n))

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    58
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    ret = base
    for i in range(1,n+1):
        ret = combiner(ret,term(i))
    return ret

def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add,0,n,term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul,1,n,term)

def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    return func(..func(func(func))..)

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    '''
    def work(val):
        #递归版本
        nonlocal n
        if n==0:
            return val
        n -= 1
        return func(work(val))
        #迭代版本
        nonlocal func,n
        for i in range(1,n+1):
            val = func(val)
        return val
    return work
    '''
    return accumulate(compose1,identity,n,lambda _: func) 

#input a func f, return the func "lambda x: x" ,x->x
def zero(f):
    return lambda x: x
 
def successor(n):
    return lambda f: lambda x: f(n(f)(x))

#input a func f, return the func successor(zero),which is "lambda f: lambda x:f(x)""
#  f -> (x->f(x))
def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)

#input a func f, return the func successor(successor(zero)) 
# which is "lambda f: lambda x:f(f(x))"
# f -> (x->f(f(x)))
#通俗来说，two的作用就是 输入一个函数f,返回的函数lambda满足:将输入的x 映射成 f(f(x))

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))

three = successor(two)


#church 0 lambda f: lambda x:x
#church 1 lambda f: lambda x:f(x)
#church 2 lambda f: lambda x:f(f(x))
#...
#我们用符号标记 church numeral: 
#   zero(f)=identity,one(f)=f,two(f)=ff, ..., n(f)=f...f =f_n，n个f

#   zero(f)(x)=x,one(f)(x)=f(x),two(f)(x)=f(f(x)) ,..., n(f)(x)=f..f(x)=f_n(x)

#   zero one ... n m这些函数就是 church numeral,
#  church numeral m可以理解成将第一个参数(函数参数)复刻m次的函数,m(f)(x)=m...m(x)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    #由于n(f)(x)=f...f(x) 当n等于0,n(f)(x)=x=0
    #所以我们取 x=0, f=lambda x:x+1
    "*** YOUR CODE HERE ***"
    return n(lambda x: x+1)(0)


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    # add(n,m)(f)(x)=f_{n+m}(x)=f_m f_n(x)=m(f)(n(f)(x))
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(f)(n(f)(x))


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    # mul(n,m)(f)(x)=f_{n*m}(x),(将f_n复刻m次)，=m(n(f))(x)
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(n(f))(x)


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    # pow(m,n)(f)(x)=f_{m**n}(x)=m...m(f)(x)=n(m)(f)(x)
    # 相当于把m调用n次,即： m..m ,等于 n(m)
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: n(m)(f)(x)