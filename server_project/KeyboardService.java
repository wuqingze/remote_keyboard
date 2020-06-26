import java.rmi.Remote;
import java.rmi.RemoteException;

public interface KeyboardService extends Remote {
    String type(String key) throws RemoteException;
}
