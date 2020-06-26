import java.io.OutputStream;
import java.io.InputStream;
import java.io.IOException;
import java.net.Socket;
import java.rmi.AlreadyBoundException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class JavaServer{
  public static void main(String args[]) throws Exception {
    // 要连接的服务端IP地址和端口
    String host = "127.0.0.1"; 
    int port = 2000;
    // 与服务端建立连接
    Socket socket = new Socket(host, port);
    // 建立连接后获得输出流
    OutputStream outputStream = socket.getOutputStream();
    InputStream inputStream = socket.getInputStream();

    KeyboardService keyboardService = new KeyboardServiceImpl(inputStream, outputStream);
    try {
	KeyboardService stub = (KeyboardService) UnicastRemoteObject.exportObject(keyboardService, 4000); //导出服务，使用4000端口
	Registry registry = LocateRegistry.createRegistry(8000);
	registry.bind("keyboardService", stub); //使用名字hello，将服务注册到Registry
    } catch (AlreadyBoundException | IOException e) {
	e.printStackTrace();
    }
    
    outputStream.close();
    socket.close();
  }
}

