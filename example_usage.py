from client import FAQMatcherClient
def main():
    c = FAQMatcherClient()
    print(c.find_match("how do I return my order?"))
if __name__ == '__main__':
    main()
