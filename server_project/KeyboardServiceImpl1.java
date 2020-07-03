import java.rmi.RemoteException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.net.Socket;

public class KeyboardServiceImpl1 implements KeyboardService{

    private InputStream inputStream;

    private OutputStream outputStream;

    // 要连接的服务端IP地址和端口
    String host = "127.0.0.1"; 
    int port = 2000;
    // 与服务端建立连接
    Socket socket;

    public KeyboardServiceImpl1(){
	try{
	    connect();
	}catch(Exception e){
	    System.out.println(String.format("KeyboardServiceImpl 连接键盘socket %s",
		    e.getMessage()
		    )
	    );
	}

//	Runnable r = ()->{
//	    while(true){
//		try{
//		    System.out.println("check socket connetc...");
//		    //if(socket == null || !socket.isConnected()){
//		    if(socket == null || -1==socket.getInputStream().read()){
//			System.out.println("socket connect failed...");
//			try{
//			    // 与服务端建立连接
//			    socket = new Socket(host, port);
//			    // 建立连接后获得输出流
//			    this.outputStream = socket.getOutputStream();
//			    this.inputStream = socket.getInputStream();
//			    System.out.println("KeyboardServiceImpl 与键盘建立连接成功");
//			}catch(Exception e){
//			    System.out.println(String.format("KeyboardServiceImpl 连接键盘socket %s",
//				    e.getMessage()
//				    )
//			    );
//			}    
//		    }
//		    Thread.sleep(1000);
//		}catch(Exception e){e.printStackTrace();}
//	    }
//	};
	//r.run();
//	new Thread(r).start();
    } 

    public String type(String key) throws RemoteException {
	String stackMsg = String.format("[%s %s] - KeyboardServiceImpl#type %s", 
		Thread.currentThread().getName(),
		LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd HH:mm:ss")),
		key);
	System.out.println(stackMsg);
	String result = null;
	try{
	    outputStream.write(key.getBytes());
	    byte[] b = new byte[32];
	    inputStream.read(b);
	    result = new String(b);
	}catch(Exception e){
	    e.printStackTrace();
	    try{
		connect();
	    }catch(Exception e1){
		throw new RemoteException("输入失败,"+e1.getMessage());
	    }
	    throw new RemoteException("输入失败,"+stackMsg);
	}
	return result;
    }

    public void connect() throws Exception{
	// 与服务端建立连接
	socket = new Socket(host, port);
	socket.setSoTimeout(100);
	// 建立连接后获得输出流
	this.outputStream = socket.getOutputStream();
	this.inputStream = socket.getInputStream();
	System.out.println("KeyboardServiceImpl 与键盘建立连接成功");
    }
}
