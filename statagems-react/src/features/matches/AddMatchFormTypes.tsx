import { TeamSide } from '~/graphql';


export interface FormValues {
  map: string;
  teams: {  
    startSide: TeamSide;
    roundsWon: number | null;
    players: {
      isCaptain: boolean;
      playerId: string | null;
      kills: number | null;
      assists: number | null;
      deaths: number | null;
      key: string;
    }[];
  }[];
}