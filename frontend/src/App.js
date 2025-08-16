
import React, { useEffect, useState } from 'react';
import Amplify, { Auth } from 'aws-amplify';
import awsconfig from './aws-exports';
import Favorites from './Favorites';
import Schedule from './Schedule';
import Stats from './Stats';
import { fetchScores, fetchSchedule, fetchStats, updateFavorites } from './api';
Amplify.configure(awsconfig);

function App() {
  const [scores, setScores] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [matches, setMatches] = useState([]);
  const [stats, setStats] = useState([]);

  useEffect(() => {
    fetchScores().then(setScores);
    fetchSchedule().then(setMatches);
    fetchStats().then(setStats);
  }, []);

  useEffect(() => {
    if (favorites.length > 0) {
      updateFavorites(favorites);
    }
  }, [favorites]);

  return (
    <div>
      <h1>ScorePulse - Live Sports Scoreboard</h1>
      <ul>
        {scores.map(score => (
          <li key={score.MatchId}>{score.TeamA} vs {score.TeamB}: {score.Score}</li>
        ))}
      </ul>
      <Favorites favorites={favorites} setFavorites={setFavorites} />
      <Schedule matches={matches} />
      <Stats stats={stats} />
    </div>
  );
}
export default App;
