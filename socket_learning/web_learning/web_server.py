import socket
import threading
import sys
from socket_learning.web_learning import framework
class HTTPSEVER(object):
    def __init__(self, port):
        self.tcp_web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_web_server.bind(("", port))
        self.tcp_web_server.listen(128)

    def main(self):
        while True:
            new_web_server, ip_port = self.tcp_web_server.accept()
            print(f"{ip_port}用户已经连接")
            threading1 = threading.Thread(target=self.parse_data,args=(new_web_server,ip_port),daemon=True)
            threading1.start()

    def parse_data(self,new_web_server,ip_port):
        recv_data = new_web_server.recv(4096)
        recv_data1 = recv_data.decode("utf8")
        try:
            data_path = recv_data1.split(" ")[1]
            if "Referer:" in recv_data1:
                referer = "站内访问"
            else:
                referer = "站外访问"
            if data_path == "/":
                data_path = "/index.html"
                # 这里如果要请求html文档，就要把请求信息传递给web框架
            if data_path.endswith(".html"):
                env = {
                    "data_path":data_path,
                    "referer": referer
                }
                response_line,file_data = framework.frame_work(env)
            else:
                with open("static" + data_path, "rb") as file:
                    file_data = file.read()
                response_line = "HTTP/1.1 200 OK\r\n"
        except:
            data_path = "/error.html"
            with open("static" + data_path, "rb") as file:
                file_data = file.read()
            response_line = "HTTP/1.1 404 Not Found\r\n"


        print(f"{ip_port}用户访问了http://localhost:8000{data_path}")
        response_headers1 = "Server: PWS/1.0\r\n"
        response_headers2 = "Content-Type: text/html;charset=utf-8\r\n"
        response_data = (response_line +  # 响应行
                         response_headers1 + # 响应头1
                         response_headers2 + # 响应头2
                         "\r\n").encode("utf8") + file_data  # 空行 和 数据
        new_web_server.send(response_data)
        new_web_server.close()
        print(f"{ip_port}用户已经断开连接")

    @classmethod
    def start(self):
        # port = self.get_port()
        # if port:
        #     HTTPSEVER1 = HTTPSEVER(port)
        #     HTTPSEVER1.main()
        # else:
        #     print("调用此函数必须遵循如下命令:python3 xxx 9000")
        #     return
        HTTPSEVER1 = HTTPSEVER(8000)
        HTTPSEVER1.main()

    # @staticmethod
    # def get_port():
    #     params = sys.argv
    #     if params[1].isdigit() and len(params) == 2:
    #         port = params[1]
    #         return int(port)
    #     else:
    #         return None

if __name__ == '__main__':
    HTTPSEVER.start()