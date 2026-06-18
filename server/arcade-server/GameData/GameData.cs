namespace arcadeServer;

public class GameData
{
		private ScreenDevice[]? _screens;

		public ScreenDevice[] Screens
		{
			get => _screens ?? [];
			set
			{
				_screens = value;
				NotifyStateChanged();
			}
		}

		public event Action? OnChange;
		private void NotifyStateChanged() => OnChange?.Invoke();
		
		public void AddScreen(ScreenDevice screen)
		{
			if (_screens == null)
			{
				_screens = [screen];
				NotifyStateChanged();
				return;
			}

			if (_screens.Any(x => x.IP == screen.IP))
			{
				return;
			}
			_screens = _screens.Append(screen).ToArray();
			NotifyStateChanged();
		}
		public void RemoveScreen(ScreenDevice screen)
		{
			_screens = _screens.Where(s => s != screen).ToArray();
			NotifyStateChanged();
		}

		public void RemoveScreen(string ip)
		{
			if(_screens == null)
				return;
			_screens = _screens.Where(s => s.IP != ip).ToArray();
			NotifyStateChanged();
		}
}

