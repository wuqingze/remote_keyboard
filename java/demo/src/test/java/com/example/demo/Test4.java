import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Test4{

    public static void main(String[] args){
	System.out.println(String.format("[%s] 发送消息:%s",
		//LocalDate.now().format(DateTimeFormatter.ofPattern("yyyyMMdd hh:mm:ss")),
		//LocalDate.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd")),
		//LocalDate.now().format(DateTimeFormatter.ofPattern("yyyyMMdd HH:mm:ss")),
		//LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MMM-dd HH:mm:ss")),
		LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")),
		"akdjf")
	);
    }
}
