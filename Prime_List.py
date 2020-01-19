print('List Prime Numbers\n\n')

prime_list = []
def list_primes():
    print('Lowest Integer To Check?')
    n = int(input())
    while n > -1:
        try:
            if n <= 1:
                n = n + 1
            elif n > 1:
                x = 1
                print("\nHighest Integer To Check?")
                i = int(input())
                print('')
                while x <= n:
                    try:
                        if n == i + 1:
                            print('')
                            return
                        elif x == 1:
                            x = x + 1
                        elif n%x != 0:
                            x = x + 1
                        elif n%x == 0:
                            if x < n:
                                x = 1
                                n = n + 1
                            elif x == n:
                                prime_list.append(str("{:,}".format(n)))
                                #print(prime_list[-1])
                                x = 1
                                n = n + 1
                            else:
                                return
                        else:
                            return
                    except:
                        return
            else:
                return
        except:
            return
    return prime_list()

def again():
    print('Total: ' + str(len(prime_list)))
    print('\nList ALL Primes, or Highest?')
    p = input()
    if p == "all":
        print('\n' + '\n'.join(map(str, prime_list)))
    if p == "highest":
        print('\n' + prime_list[-1])
    print('\nTotal: ' + str(len(prime_list)))
    prime_list.clear()
    print('\n\nAgain?')
    b = input()
    print('')
    if b == "yes":
        list_primes()
    if b == "no":
        quit()
    again()

list_primes()
again()
