import java.io.IOException;
import java.rmi.AlreadyBoundException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class RMIServer {

    public static void main(String[] args) {

        RemoteHello remoteHello = new RemoteHelloImpl();
        try {
            RemoteHello stub = (RemoteHello) UnicastRemoteObject.exportObject(remoteHello, 4000); //导出服务，使用4000端口
            //Registry registry = LocateRegistry.getRegistry("127.0.0.1", 8000); //获取Registry
	    //System.setProperty("java.rmi.server.hostname","192.168.0.108");
            //Registry registry = LocateRegistry.getRegistry("192.168.0.108", 8000); //获取Registry
	    Registry registry = LocateRegistry.createRegistry(8000);
            registry.bind("hello", stub); //使用名字hello，将服务注册到Registry
        } catch (AlreadyBoundException | IOException e) {
            e.printStackTrace();
        }

    }
}
