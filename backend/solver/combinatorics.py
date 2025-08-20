def factorial(n):

    solver ={'step1':f'n! = n(n-1) (n-2) (n-3)...'
    ,'step2':f'{n}! = {n}({n-1})  ({n-2})  ({n-3})...'}

    factorial =1
    for i in range (1,n+1):
        factorial*=i
    return {'solution':factorial,'steps':solver}



def combination(n,r):
    factorial_n =1
    for i in range (1,n+1):
        factorial_n*=i

    factorial_r =1 
    for j in range (1,r+1):
        factorial_r*=j

    factorial_n_r = 1
    num =n-r
    for k in range (1,num+1):
        factorial_n_r *= k


    solver = {'step1':f"n! /(n-r)!(r)!", 'step2': f"{n}! /({n} -{r}!)({r})!", 'step3': f"{factorial_n}! /{factorial_n_r}!({factorial_r})!"}

    answer = factorial_n/((factorial_n_r)*(factorial_r))

    return {'solution':answer,'steps':solver}



def permutation(n,r):
    factorial_n =1
    for i in range (1,n+1):
        factorial_n*=i
        
    factorial_n_r = 1
    num =n-r
    for k in range (1,num+1):
        factorial_n_r *= k
        
        
    solver = {'step1':f"n! /(n-r)!(r)!", 'step2': f"{n}! /({n} -{r}!)({r})!", 'step3': f"{factorial_n}! /{factorial_n_r}!"}


    answer = factorial_n/factorial_n_r

    return {'solution':answer,'steps':solver}
