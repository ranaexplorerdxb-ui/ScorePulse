// API utility for ScorePulse frontend
export async function fetchScores() {
  const res = await fetch('/scores');
  return res.json();
}

export async function fetchSchedule() {
  const res = await fetch('/schedule');
  return res.json();
}

export async function fetchStats() {
  const res = await fetch('/stats');
  return res.json();
}

export async function updateFavorites(favorites) {
  await fetch('/favorites', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ Favorites: favorites })
  });
}
