import React from 'react';

function Schedule({ matches }) {
  return (
    <div>
      <h2>Upcoming Matches</h2>
      <ul>
        {matches.map(match => (
          <li key={match.MatchId}>
            {match.TeamA} vs {match.TeamB} - {match.DateTime}
          </li>
        ))}
      </ul>
    </div>
  );
}
export default Schedule;
