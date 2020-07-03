import java.rmi.RemoteException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Arrays;

public class Test3{


    public static void main(String[] args){

    InputStream inputStream=null;

    OutputStream outputStream=null;
    // 要连接的服务端IP地址和端口
    String host = "127.0.0.1"; 
    int port = 2000;
    // 与服务端建立连接
    Socket socket=null;

	try{
            // 与服务端建立连接
            socket = new Socket(host, port);
            // 建立连接后获得输出流
            outputStream = socket.getOutputStream();
            inputStream = socket.getInputStream();
	    System.out.println("KeyboardServiceImpl 与键盘建立连接成功");
	}catch(Exception e){
	    System.out.println(String.format("KeyboardServiceImpl 连接键盘socket %s",
		    e.getMessage()
		    )
	    );
	}
	
	try{
	    byte[] b = null;
	    outputStream.write(("release:Key.ctrl_l").getBytes());
	    inputStream.read(b);
	    System.out.println("result---"+new String(b));
	}catch(Exception e){
	    e.printStackTrace();
	}
    } 
}
