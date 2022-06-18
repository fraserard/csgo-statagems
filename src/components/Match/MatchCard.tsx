
import { GetMatchListQuery } from '~/gql/generated';
import { Link } from "react-router-dom";
import styles from "./MatchCard.module.css";


interface Props {
  match: GetMatchListQuery['matches'][0];
}

function MatchCard({match}: Props){
  return (
    <li>
      <Link to={`match/${match.id}`}>
        <div className={styles.details}>          
          <p>{match.map.mapName}</p>    
          <p>{match.datePlayed}</p>
        </div>
        <div className={styles.players}>
          <div>
            {match.teams[0].matchPlayers.map(player => 
              <img key={player.playerId} src={player.avatar.smallAvatarUrl}/> )}
          </div>
          <p>{match.score}</p>
          <div>
            {match.teams[1].matchPlayers.map(player => 
              <img key={player.playerId} src={player.avatar.smallAvatarUrl}/> )}
          </div>
        </div>
      </Link>
    </li>
  );
}

export default MatchCard;