import java.io.IOException;
import java.rmi.AlreadyBoundException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Test1{

    public static void main(String[] args) {
	System.out.println("hostname------------"+System.getProperty("java.rmi.server.hostname"));
    }
}
