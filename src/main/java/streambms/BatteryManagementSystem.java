package streambms;

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

	public static String sentToConsole(BatteryResponse batteryResponse, boolean isConsumed) {
		ObjectMapper mapper = new ObjectMapper();
		try {
			String batteryData = "";
			for (int i = 0; i <= 10; i++) {
				if (!isConsumed || batteryData.isEmpty()) {
					Thread.sleep(2000);
					batteryData = mapper.writeValueAsString(batteryResponse);
					System.out.println(batteryData);
				} else {
					break;
				}
			}

			return batteryData;

		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}

	public static String sendToReceiver(boolean isConsumed) {
		return sentToConsole(sendBatteryParameters(getBatteryParameters()), isConsumed);

	}

	public static float getRandomNumber(float min, float max) {
		float rounded = Math.round(((Math.random() * (max - min)) + min) * 100);
		return (float) (rounded / 100.0);
	}

}
