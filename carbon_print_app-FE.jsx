import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data after login
    const fetchUserData = async () => {
      try {
        const response = await axios.get('/api/user', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        });
        setUser(response.data);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    if (localStorage.getItem('token')) {
      fetchUserData();
    }
  }, []);

  const handleLogin = async () => {
    // Implement login functionality
    // Call your authentication API endpoint
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  return (
    <div>
      {user ? (
        <div>
          <h1>Hello, {user.username}!</h1>
          <p>Carbon Footprint: {user.carbonFootprint} kgCO2e</p>
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div>
          <h1>Login</h1>
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
}

export default App;
