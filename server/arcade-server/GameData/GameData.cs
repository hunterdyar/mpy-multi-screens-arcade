using System.Text.Json;
using Microsoft.AspNetCore.Components;

namespace arcadeServer;

public class GameData
{
		public LiveData LiveData = new LiveData();

		public ScreenDevice[] Screens
		{
			get => LiveData.Screens ?? [];
			set
			{
				LiveData.Screens = value;
				NotifyStateChanged();
			}
		}

		public GameData()
		{
			var dirInfo = new DirectoryInfo(Environment.CurrentDirectory + "/data/");
			if (!dirInfo.Exists)
			{
				dirInfo.Create();
			}
			
			var dataFile = new FileInfo(Environment.CurrentDirectory + "/data/devices.json");
			if (dataFile.Exists)
			{
				string data = System.IO.File.ReadAllText(dataFile.FullName);
				if (!string.IsNullOrEmpty(data))
				{
					var deserialize = JsonSerializer.Deserialize<LiveData>(data);
					if (deserialize != null)
					{
						LiveData = deserialize;
					}
				}
			}
			else
			{
				dataFile.Create();
			}
		}

		public event Action? OnChange;
		private void NotifyStateChanged() => OnChange?.Invoke();
		
		public void AddScreen(ScreenDevice screen)
		{
			if (LiveData.Screens == null)
			{
				LiveData.Screens = [screen];
				NotifyStateChanged();
				Save();
				return;
			}

			if (LiveData.Screens.Any(x => x.IP == screen.IP))
			{
				return;
			}

			LiveData.Screens = LiveData.Screens.Append(screen).ToArray();
			Save();
			NotifyStateChanged();
		}

		public void RemoveScreen(string ip)
		{
			if (LiveData.Screens == null)
			{
				return;
			}

			LiveData.Screens = LiveData.Screens.Where(s => s.IP != ip).ToArray();
			NotifyStateChanged();
			Save();
		}


		public void Save()
		{
			var dataFile = new FileInfo(Environment.CurrentDirectory + "/data/devices.json");
			var text = JsonSerializer.Serialize<LiveData>(LiveData, new JsonSerializerOptions { WriteIndented = true });
			System.IO.File.WriteAllText(dataFile.FullName, text);
		}
}

[Serializable]
public class LiveData
{
	public ScreenDevice[] Screens { get; set; } = [];
}