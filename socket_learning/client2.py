import socket # 导入socket模块
import threading
# 1. 创建tcp客户端套接字
# socket.AF_INET 表示ip地址的类型为ipv4，socket.SOCK_STREAM表示tcp协议
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 与服务端建立连接
socket_client.connect(("127.0.0.1", 6565))  # 注意这里要写入一个元组，元组中包含ip地址和端口号
# 3. 向服务端发送信息
send_data1 = "\n与客户端2成功建立连接"
socket_client.sendall(send_data1.encode("utf8"))


def send_data(socket_client):
    while True:
        # resv_data = socket_client.recv(1024).decode("utf8")
        # print(resv_data)
        send_data = input("")
        bytes_data = send_data.encode("utf8")
        socket_client.sendall(bytes_data)

def resv_data(socket_client):
    pass


#     # 4. 关闭套接字连接
# socket_client.close()
if __name__ == '__main__':
    threading1 = threading.Thread(target=send_data, args=(socket_client,), daemon=True)
    threading1.start()
    while True:
        bytes_data1 = socket_client.recv(1024)
        data_truth = bytes_data1.decode(encoding="utf8")
        print(data_truth)

    # threading2 = threading.Thread(target=resv_data, args=(socket_client,), daemon=True)
    # threading2.start()