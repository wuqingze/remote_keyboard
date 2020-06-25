import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("127.0.0.1", 8000);  //获取注册中心引用
            RemoteHello remoteHello = (RemoteHello) registry.lookup("hello"); //获取RemoteHello服务
            System.out.println(remoteHello.sayHello("World"));  //调用远程方法
        } catch (RemoteException | NotBoundException e) {
            e.printStackTrace();
        }
    }
}
