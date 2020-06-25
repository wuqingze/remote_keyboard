import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Test2{
  public static void main(String args[]) throws Exception {
    // 要连接的服务端IP地址和端口
    String host = "localhost";
    int port = 2000;
    // 与服务端建立连接
    Socket socket = new Socket(host, port);
    // 建立连接后获得输出流
    OutputStream outputStream = socket.getOutputStream();
    InputStream inputStream = null;
    Scanner in = new Scanner(System.in);
    while(in.hasNext()){
	outputStream.write(in.next().getBytes("UTF-8"));
	inputStream = inputStream == null?socket.getInputStream():inputStream;
	byte[] b = new byte[inputStream.available()];
	inputStream.read(b);
        System.out.println("get message from server: " + new String(b));
    }
    inputStream.close();
    outputStream.close();
    socket.close();
  }
}
