import socket
import threading
import time
ADDR = ("",6565)
listen_client = 128
client_pool = []
data_pool = {}
data1 = []
data2 = []
def accept_client(tcp_server):
    while True:
        # 4. 等待接受客户端的请求 这一步会阻塞，等待连接
        new_client, ip_port = tcp_server.accept()
        # 6. 发送数据到客户端
        # send_content = input("（服务端）请输入你要发送的信息：")
        # send_data = send_content.encode("utf8")
        # new_client.send(send_data)
        # 5. 接受客户端的数据
        # result (new_client, ip_port)为一个元组第一个元素是一个新的套接字（以后和客户端通信用这个新的套接字），第二个是ip地址和端口号
        client_pool.append(new_client)
        resv_data1 = new_client.recv(1024)
        bytes_data = resv_data1.decode("utf8")
        print(bytes_data)
        threading1 = threading.Thread(target=client_response, args=(new_client, ip_port), daemon=True)
        threading1.start()


def client_response(new_client, ip_port):
    new_client.sendall("\n连接服务器成功!".encode(encoding="utf8"))
    while True:
        resv_data = new_client.recv(1024)
        data_pool[new_client] = resv_data
        data_truth = resv_data.decode("utf8")
        print(f"接受到{ip_port}发来的信息：", data_truth)
        if len(resv_data)==0:
            print(f"{ip_port}客户断开连接")
            client_pool.remove(new_client)
            break
    new_client.close()


if __name__ == '__main__':
    # 1. 创建一个服务端的套接字
    # AF_INET是ipv4的意思，SOCK_STREAM是TCP协议的意思
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定端口号 第一个参数表示ip地址一般不用指定，第二个参数表示端口号
    # 设置端口号复用，防止出现端口号短暂占用的情况
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server.bind(ADDR)
    # 3. 设置监听 128表示最大等待建立的连接的个数 一般都写128
    tcp_server.listen(listen_client)
    threading2 = threading.Thread(target=accept_client,args=(tcp_server,),daemon=True)
    threading2.start()
    while True:
        cmd = int(input("""请输入你要选择的命令：
1. 查看当前用户数量
2. 给指定用户发送信息
3. 让两个用户开始沟通
4. 关闭服务器"""))
        if cmd == 1:
            num = len(client_pool)
            print(f"当前在线人数为{num}")
        elif cmd == 2:
            data = input("请输入你要发送的信息和指定用户编号").split(",")
            client_pool[int(data[1])-1].sendall(data[0].encode(encoding="utf8"))
        elif cmd == 3:
            i = input("请输入你让谁和谁通信").split(",")
            client_pool[int(i[1]) - 1].sendall(f"您已经跟用户{int(i[0])}建立连接，可以通过服务器进行正常通话了".encode())
            client_pool[int(i[0]) - 1].sendall(f"您已经跟用户{int(i[1])}建立连接，可以通过服务器进行正常通话了".encode())
            n = 1
            while True:
                if client_pool[int(i[0])-1] in data_pool.keys():
                    data_1 = data_pool[client_pool[int(i[0])-1]]
                    if data_1 not in data1:
                        data1.append(data_1)
                        client_pool[int(i[1])-1].sendall(data_1)
                        if len(data1)==2:
                            data1.pop(0)

                if client_pool[int(i[1])-1] in data_pool.keys():
                    data_2 = data_pool[client_pool[int(i[1])-1]]
                    if data_2 not in data2:
                        data2.append(data_2)
                        client_pool[int(i[0])-1].sendall(data_2)
                        if len(data2)==2:
                            data2.pop(0)
                n += 1
                time.sleep(0.5)
        else:
            exit()




    # # 7. 关闭套接字
    # tcp_server.close()