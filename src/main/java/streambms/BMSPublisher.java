package streambms;

public class BMSPublisher {

	public static void main(String[] args) {
		BatteryManagementSystem.sendToReceiver(false);
	}
}
