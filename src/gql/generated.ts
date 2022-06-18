import gql from 'graphql-tag';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  /** Date with time (isoformat) */
  DateTime: any;
  /** 64 bit SteamID. Like: 7656xxxxxxxxxxxxx */
  SteamID: any;
};

export type AddMatchInput = {
  datePlayed?: InputMaybe<Scalars['DateTime']>;
  mapId: Scalars['Int'];
  team1: AddMatchTeamInput;
  team2: AddMatchTeamInput;
};

export type AddMatchPlayerInput = {
  adr?: InputMaybe<Scalars['Int']>;
  assists: Scalars['Int'];
  deaths: Scalars['Int'];
  kills: Scalars['Int'];
  mvps?: InputMaybe<Scalars['Int']>;
  playerId: Scalars['Int'];
  score?: InputMaybe<Scalars['Int']>;
};

export type AddMatchTeamInput = {
  captainId?: InputMaybe<Scalars['Int']>;
  players: Array<AddMatchPlayerInput>;
  roundsWon: Scalars['Int'];
  startSide: TeamSide;
};

export type AvatarUrl = {
  __typename?: 'AvatarUrl';
  bigAvatarUrl: Scalars['String'];
  mediumAvatarUrl: Scalars['String'];
  smallAvatarUrl: Scalars['String'];
  steamAvatarHash: Scalars['String'];
};

export type IPlayer = {
  adr?: Maybe<Scalars['Int']>;
  assists: Scalars['Int'];
  avatar: AvatarUrl;
  deaths: Scalars['Int'];
  gamesLost: Scalars['Int'];
  gamesPlayed: Scalars['Int'];
  gamesTied: Scalars['Int'];
  gamesWon: Scalars['Int'];
  id: Scalars['ID'];
  kills: Scalars['Int'];
  lastSeen: Scalars['DateTime'];
  mvps: Scalars['Int'];
  role: Role;
  roundsLost: Scalars['Int'];
  roundsWon: Scalars['Int'];
  score: Scalars['Int'];
  steamId: Scalars['SteamID'];
  steamProfileUrl: Scalars['String'];
  steamRealName?: Maybe<Scalars['String']>;
  steamUsername: Scalars['String'];
  timesCaptain: Scalars['Int'];
  timesStartedCt: Scalars['Int'];
  timesStartedT: Scalars['Int'];
};

export type Map = Node & {
  __typename?: 'Map';
  activeDuty: Scalars['Boolean'];
  filename: Scalars['String'];
  id: Scalars['ID'];
  mapName: Scalars['String'];
};

export type Match = Node & {
  __typename?: 'Match';
  datePlayed: Scalars['DateTime'];
  id: Scalars['ID'];
  map: Map;
  /** formatted like 'winner_score-loser_score' ex. 16-8, 16-14 */
  score: Scalars['String'];
  teams: Array<MatchTeam>;
};

export type MatchPlayer = {
  __typename?: 'MatchPlayer';
  adr?: Maybe<Scalars['Int']>;
  assists: Scalars['Int'];
  avatar: AvatarUrl;
  deaths: Scalars['Int'];
  kills: Scalars['Int'];
  mvps?: Maybe<Scalars['Int']>;
  playerId: Scalars['Int'];
  score?: Maybe<Scalars['Int']>;
  steamUsername: Scalars['String'];
};

export type MatchTeam = {
  __typename?: 'MatchTeam';
  captainId?: Maybe<Scalars['Int']>;
  matchId: Scalars['Int'];
  matchPlayers: Array<MatchPlayer>;
  outcome: Outcome;
  roundsLost: Scalars['Int'];
  roundsWon: Scalars['Int'];
  startSide: TeamSide;
  teamId: Scalars['Int'];
};

export type Mutation = {
  __typename?: 'Mutation';
  addMatch: Match;
};


export type MutationAddMatchArgs = {
  matchData: AddMatchInput;
};

export type Node = {
  id: Scalars['ID'];
};

export enum Outcome {
  Lost = 'LOST',
  Tied = 'TIED',
  Won = 'WON'
}

export type Player = IPlayer & Node & PlayerAggregates & TeamAggregates & {
  __typename?: 'Player';
  adr?: Maybe<Scalars['Int']>;
  assists: Scalars['Int'];
  avatar: AvatarUrl;
  deaths: Scalars['Int'];
  gamesLost: Scalars['Int'];
  gamesPlayed: Scalars['Int'];
  gamesTied: Scalars['Int'];
  gamesWon: Scalars['Int'];
  id: Scalars['ID'];
  kills: Scalars['Int'];
  lastSeen: Scalars['DateTime'];
  matches?: Maybe<Array<Match>>;
  mvps: Scalars['Int'];
  role: Role;
  roundsLost: Scalars['Int'];
  roundsWon: Scalars['Int'];
  score: Scalars['Int'];
  steamId: Scalars['SteamID'];
  steamProfileUrl: Scalars['String'];
  steamRealName?: Maybe<Scalars['String']>;
  steamUsername: Scalars['String'];
  timesCaptain: Scalars['Int'];
  timesStartedCt: Scalars['Int'];
  timesStartedT: Scalars['Int'];
};

export type PlayerAggregates = {
  adr?: Maybe<Scalars['Int']>;
  assists: Scalars['Int'];
  deaths: Scalars['Int'];
  kills: Scalars['Int'];
  mvps: Scalars['Int'];
  score: Scalars['Int'];
  timesCaptain: Scalars['Int'];
};

export type PlayerList = IPlayer & Node & PlayerAggregates & TeamAggregates & {
  __typename?: 'PlayerList';
  adr?: Maybe<Scalars['Int']>;
  assists: Scalars['Int'];
  avatar: AvatarUrl;
  deaths: Scalars['Int'];
  gamesLost: Scalars['Int'];
  gamesPlayed: Scalars['Int'];
  gamesTied: Scalars['Int'];
  gamesWon: Scalars['Int'];
  id: Scalars['ID'];
  kills: Scalars['Int'];
  lastSeen: Scalars['DateTime'];
  mvps: Scalars['Int'];
  role: Role;
  roundsLost: Scalars['Int'];
  roundsWon: Scalars['Int'];
  score: Scalars['Int'];
  steamId: Scalars['SteamID'];
  steamProfileUrl: Scalars['String'];
  steamRealName?: Maybe<Scalars['String']>;
  steamUsername: Scalars['String'];
  timesCaptain: Scalars['Int'];
  timesStartedCt: Scalars['Int'];
  timesStartedT: Scalars['Int'];
};

export type Query = {
  __typename?: 'Query';
  match: Match;
  matches: Array<Match>;
  /** Get a single player by their SteamID. */
  player: Player;
  /** Get a list of all players. */
  players: Array<PlayerList>;
};


export type QueryMatchArgs = {
  matchId: Scalars['Int'];
};


export type QueryPlayerArgs = {
  steamId: Scalars['SteamID'];
};

export enum Role {
  Admin = 'ADMIN',
  Mod = 'MOD',
  Ref = 'REF',
  User = 'USER'
}

export type TeamAggregates = {
  gamesLost: Scalars['Int'];
  gamesTied: Scalars['Int'];
  gamesWon: Scalars['Int'];
  roundsLost: Scalars['Int'];
  roundsWon: Scalars['Int'];
  timesStartedCt: Scalars['Int'];
  timesStartedT: Scalars['Int'];
};

export enum TeamSide {
  Ct = 'CT',
  T = 'T'
}

export type MatchDataFragment = { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', mapName: string }, teams: Array<{ __typename?: 'MatchTeam', captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> };

export type GetMatchQueryVariables = Exact<{
  matchId: Scalars['Int'];
}>;


export type GetMatchQuery = { __typename?: 'Query', match: { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', mapName: string }, teams: Array<{ __typename?: 'MatchTeam', captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> } };

export type GetMatchListQueryVariables = Exact<{ [key: string]: never; }>;


export type GetMatchListQuery = { __typename?: 'Query', matches: Array<{ __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', mapName: string }, teams: Array<{ __typename?: 'MatchTeam', matchPlayers: Array<{ __typename?: 'MatchPlayer', playerId: number, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> }> };

export const MatchData = gql`
    fragment matchData on Match {
  datePlayed
  id
  score
  map {
    mapName
  }
  teams {
    captainId
    outcome
    roundsWon
    startSide
    teamId
    matchPlayers {
      deaths
      kills
      playerId
      assists
      steamUsername
      avatar {
        smallAvatarUrl
      }
    }
  }
}
    `;
export const GetMatch = gql`
    query GetMatch($matchId: Int!) {
  match(matchId: $matchId) {
    ...matchData
  }
}
    ${MatchData}`;
export const GetMatchList = gql`
    query GetMatchList {
  matches {
    datePlayed
    id
    score
    map {
      mapName
    }
    teams {
      matchPlayers {
        playerId
        avatar {
          smallAvatarUrl
        }
      }
    }
  }
}
    `;