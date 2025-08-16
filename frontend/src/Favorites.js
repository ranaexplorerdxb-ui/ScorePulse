import React, { useState } from 'react';

function Favorites({ favorites, setFavorites }) {
  const [input, setInput] = useState('');
  const addFavorite = () => {
    if (input && !favorites.includes(input)) {
      setFavorites([...favorites, input]);
      setInput('');
    }
  };
  return (
    <div>
      <h2>Favorite Teams</h2>
      <input value={input} onChange={e => setInput(e.target.value)} placeholder="Add team" />
      <button onClick={addFavorite}>Add</button>
      <ul>
        {favorites.map(f => <li key={f}>{f}</li>)}
      </ul>
    </div>
  );
}
export default Favorites;
