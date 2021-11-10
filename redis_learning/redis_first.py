import redis

if __name__ == '__main__':
    rs = redis.Redis()
    rs.mset({"major":"AEE","school":"unnc"})
    result = rs.mget("username","age")
    print(result)
