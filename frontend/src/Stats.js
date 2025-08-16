import React from 'react';

function Stats({ stats }) {
  return (
    <div>
      <h2>Match Stats</h2>
      <ul>
        {stats.map(stat => (
          <li key={stat.MatchId}>
            {stat.TeamA} vs {stat.TeamB}: {stat.StatsSummary}
          </li>
        ))}
      </ul>
    </div>
  );
}
export default Stats;
