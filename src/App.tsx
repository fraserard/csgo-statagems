import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Provider } from 'urql'
import { client } from './gql/urqlClient';
import AddMatchPage from './pages/AddMatchPage';
import HomePage from './pages/HomePage';
import MatchPage from './pages/MatchPage';
import PlayerPage from './pages/PlayerPage';

function App() {

  return (
    <Provider value={client}>
      <BrowserRouter>
        {/* <Header /> */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/match/:matchId" element={<MatchPage />} />
          <Route path="/match/add" element={<AddMatchPage />} />
          <Route path="/player/:id" element={<PlayerPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
