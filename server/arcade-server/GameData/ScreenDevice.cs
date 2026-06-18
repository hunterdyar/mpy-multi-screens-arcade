using System.Text.Encodings.Web;

namespace arcadeServer;

[System.Serializable]
public class ScreenDevice
{
	public string IP { get; set; }
	private HttpClient httpClient;

	public ScreenDevice()
	{
		//from deserialize?
		if (IP != null)
		{
			httpClient = new HttpClient()
			{
				BaseAddress = new Uri(IP)
			};
		}
	}
	public ScreenDevice(Uri uri)
	{
		httpClient = new HttpClient()
		{
			BaseAddress = uri
		};
		IP = httpClient.BaseAddress.Host;
	}
	public async void SendText(string text)
	{
		Console.WriteLine($"Trying to send {text} to {IP}...");
		try
		{
			var r = await httpClient.GetAsync($"?t={UrlEncoder.Default.Encode(text)}");
			if(r.IsSuccessStatusCode)
			{
				Console.WriteLine($"sent {text} to {IP}");
			}
			else
			{
				Console.WriteLine(r.StatusCode);
			}
		}
		catch (Exception e)
		{
			//i'm not sending valid status codes back so, uh. yeah. 
			Console.WriteLine(e.Message);
		}
	}
}