import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class JavaClient{
  public static void main(String args[]) throws Exception {
    // 监听指定的端口
    int port = args.length<1?55533:Integer.parseInt(args[0]);
    ServerSocket server = new ServerSocket(port);
    // server将一直等待连接的到来
    System.out.println("server将一直等待连接的到来");

    //如果使用多线程，那就需要线程池，防止并发过高时创建过多线程耗尽资源
    ExecutorService threadPool = Executors.newFixedThreadPool(4);
    
    while (true) {
      Socket socket = server.accept();
      
      Runnable runnable=()->{
	  InputStream inputStream = null;
	  OutputStream outputStream = null;
	  try {
	    // 建立好连接后，从socket中获取输入流，并建立缓冲区进行读取
	    inputStream = inputStream==null?socket.getInputStream():inputStream;
	    outputStream = outputStream==null?socket.getOutputStream():outputStream;
	    byte[] bytes = new byte[32];
	    inputStream.read(bytes);
	    outputStream.write(bytes);
	    System.out.println("get message from client: " + new String(bytes));
	  } catch (Exception e) {
	    e.printStackTrace();
	  }finally{
	      try{
		  inputStream.close();
		  outputStream.close();
		  socket.close();
	      }catch(Exception e){ e.printStackTrace();}
	 }
      };
      threadPool.submit(runnable);
    }
  }
}
