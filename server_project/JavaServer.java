import java.rmi.AlreadyBoundException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class JavaServer{
  public static void main(String args[]) throws Exception {
       KeyboardService keyboardService = new KeyboardServiceImpl1();
       //KeyboardService keyboardService = new KeyboardServiceImpl1();
       try {
	   System.out.println("开始注册服务");
      	   KeyboardService stub = (KeyboardService) UnicastRemoteObject.exportObject(keyboardService, 4000); //导出服务，使用4000端口
      	   Registry registry = LocateRegistry.createRegistry(8000);
      	   registry.bind("keyboardService", stub); //使用名字hello，将服务注册到Registry
	   System.out.println("服务注册成功");
       } catch (AlreadyBoundException e) {
   	   e.printStackTrace();
       }
  }
}
