import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { Provider as UrqlProvider } from "urql";
import PrivateRoute from "./components/PrivateRoute";
import MantineProviders from "./contexts/MantineProviders";
import UserProvider from "./contexts/UserContext";
import { Role } from "./graphql";
import AddMatchPage from "./pages/AddMatchPage";
import HomePage from "./pages/HomePage";
import ManageMapsPage from "./pages/ManageMapsPage";
import ManagePlayersPage from "./pages/ManagePlayersPage";
import MatchPage from "./pages/MatchPage";
import PlayerPage from "./pages/PlayerPage";
import { client } from "./urqlClient";

function App() {
  return (
    <UrqlProvider value={client}>
      <MantineProviders>
        <UserProvider>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/match/:matchId" element={<MatchPage />} />
              <Route
                path="/match/add"
                element={<PrivateRoute minRole={Role.Ref} page={<AddMatchPage />} />}
              />
              <Route path="/player/:playerId" element={<PlayerPage />} />
              <Route
                path="/manage/players"
                element={<PrivateRoute minRole={Role.Mod} page={<ManagePlayersPage />} />}
              />
              <Route
                path="/manage/maps"
                element={<PrivateRoute minRole={Role.Mod} page={<ManageMapsPage />} />}
              />
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
          </BrowserRouter>
        </UserProvider>
      </MantineProviders>
    </UrqlProvider>
  );
}

export default App;
