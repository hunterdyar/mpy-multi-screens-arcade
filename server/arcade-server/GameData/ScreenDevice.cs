using System.Text.Encodings.Web;

namespace arcadeServer;

public class ScreenDevice
{
	public string IP => httpClient.BaseAddress.Host.ToString() ?? "";
	private HttpClient httpClient;

	public ScreenDevice(Uri uri)
	{
		httpClient = new HttpClient()
		{
			BaseAddress = uri
		};
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