package streambms;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import streambms.constant.BatteryConstant;
import streambms.response.BatteryResponse;

public class BatteryManagementSystem {

	public static BatteryResponse sendBatteryParameters(BatteryResponse battery) {
		if (battery == null)
			return null;

		return battery;
	}

	public static BatteryResponse getBatteryParameters() {
		float temperature = getRandomNumber(BatteryConstant.MIN_TEMPERATURE, BatteryConstant.MAX_TEMPERATURE);
		float soc = getRandomNumber(BatteryConstant.MIN_SOC, BatteryConstant.MAX_SOC);
		float chargeRate = getRandomNumber(BatteryConstant.MIN_CHANGE_RATE, BatteryConstant.MAX_CHANGE_RATE);

		return new BatteryResponse(temperature, soc, chargeRate);
	}

	public static void sendToReceiver(boolean isConsumed) {
		ObjectMapper mapper = new ObjectMapper();
		try {
			for (int i = 0; i <= 10; i++) {
				sendToConsole(mapper.writeValueAsString(sendBatteryParameters(getBatteryParameters())), isConsumed);
			}
			
		} catch (JsonProcessingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static void sendToConsole(String batteryData, boolean isConsumed) {
		if (!isConsumed) {
			try {
				Thread.sleep(2000);
				System.out.println(batteryData);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}

	}

	public static float getRandomNumber(float min, float max) {
		float rounded = Math.round(((Math.random() * (max - min)) + min) * 100);
		return (float) (rounded / 100.0);
	}

}
