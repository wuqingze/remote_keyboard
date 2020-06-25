import java.rmi.RemoteException;
import java.time.LocalDate;

public class RemoteHelloImpl  implements RemoteHello {
    public String sayHello(String name) throws RemoteException {
	    System.out.println("akldjfldasj");
	System.out.println(String.format("[%s] [%s] sayHello[%s]", Thread.currentThread().getName(), LocalDate.now().toString(), name));
        return String.format("Hello, %s!", name);
    }
}
