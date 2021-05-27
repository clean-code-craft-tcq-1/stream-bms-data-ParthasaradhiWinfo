package streambms;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;

import org.junit.Test;

import streambms.response.BatteryResponse;

public class BatteryManagementSystemTest {

	@Test
	public void givenBatteryParametesAsNull() {
		BatteryResponse battery = null;

		assertNull(BatteryManagementSystem.sendBatteryParameters(battery));
	}

	@Test
	public void givenBatteryParametesAsValid() {
		BatteryResponse battery = BatteryManagementSystem.getBatteryParameters();

		assertNotNull(BatteryManagementSystem.sendBatteryParameters(battery));
	}
	
	@Test
	public void isConsumedFalse() {
		String generatedValue = BatteryManagementSystem.sendToReceiver(false);
		assertNotNull(generatedValue);
	}
	
	@Test
	public void isConsumedTru() {
		String generatedValue = BatteryManagementSystem.sendToReceiver(true);
		assertNotNull(generatedValue);
	}
	
	
}
