import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class JavaClient{

    private static KeyboardService keyboardService;

    public static void main(String args[]) throws Exception {
        System.out.println("连接远程服务...");
        try {
            Registry registry = LocateRegistry.getRegistry("192.168.0.108", 8000);  //获取注册中心引用
            keyboardService = (KeyboardService) registry.lookup("keyboardService"); //获取keyboardService服务
            System.out.println("远程服务连接成功");
        } catch (RemoteException | NotBoundException e) {
            e.printStackTrace();
            System.out.println("远程服务连接失败");
	    return;
        }
  
        // 监听指定的端口
        int port = args.length<1?55533:Integer.parseInt(args[0]);
        ServerSocket server = new ServerSocket(port);
        //等待键盘输入
        System.out.println("等待键盘输入...");
  
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
                    String msg = new String(bytes); 
                    System.out.println(String.format("[%s] 发送消息:%s",
                	    LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")),
                	    msg)
          	    );
                    String result = keyboardService.type(msg);
                    System.out.println(String.format("[%s] 接受消息:%s",
                	    LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")),
                	    result)
          	    );
		    System.out.println("result==========="+result);
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

    public static String parseArg(String arg){

	return null;
    }
}
