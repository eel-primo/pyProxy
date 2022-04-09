from pyProxy import proxyscrape

ps = proxyscrape()
print("Proxy found:", ps.get_proxy(int(input("Enter limit: "))))

input()
