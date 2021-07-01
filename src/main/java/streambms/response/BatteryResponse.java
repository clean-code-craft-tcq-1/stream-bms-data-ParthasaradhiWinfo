package streambms.response;

public class BatteryResponse {
	public float temperature;
	public float soc;
	public float chargeRate;

	public BatteryResponse(float temperature, float soc, float chargeRate) {
		this.temperature = temperature;
		this.soc = soc;
		this.chargeRate = chargeRate;
	}
}
