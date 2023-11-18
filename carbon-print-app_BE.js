const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const User = require('./models/User');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/carbon_footprint', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.post('/api/login', async (req, res) => {
  // Implement user login authentication
  // Check credentials and generate a JWT token
});

app.get('/api/user', async (req, res) => {
  const token = req.headers.authorization.split(' ')[1];
  const decoded = jwt.verify(token, 'your_secret_key');
  
  // Fetch user data based on the decoded token
  const user = await User.findById(decoded.userId);

  res.json({
    userId: user._id,
    username: user.username,
    carbonFootprint: user.carbonFootprint,
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
