import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';
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
  /** Represents NULL values */
  Void: any;
};

export type AddMapErrors = FilenameTooLong | MapNameTooLong;

export type AddMapInput = {
  activeDuty: Scalars['Boolean'];
  filename: Scalars['String'];
  mapName: Scalars['String'];
  removed: Scalars['Boolean'];
};

export type AddMapPayload = {
  __typename?: 'AddMapPayload';
  errors: Array<AddMapErrors>;
  map?: Maybe<Map>;
};

export type AddMatchErrors = CaptainNotOnTeam | DuplicatePlayers | DuplicateStartSide | MapNotFound | OnlyOneCaptainSet | PlayerNotFound | ScoreRulesInvalid;

export type AddMatchInput = {
  mapId: Scalars['Int'];
  team1: AddMatchTeamInput;
  team2: AddMatchTeamInput;
};

export type AddMatchPayload = {
  __typename?: 'AddMatchPayload';
  errors: Array<AddMatchErrors>;
  match?: Maybe<Match>;
};

export type AddMatchPlayerInput = {
  assists: Scalars['Int'];
  deaths: Scalars['Int'];
  kills: Scalars['Int'];
  playerId: Scalars['Int'];
};

export type AddMatchTeamInput = {
  captainId?: InputMaybe<Scalars['Int']>;
  player1: AddMatchPlayerInput;
  player2: AddMatchPlayerInput;
  player3: AddMatchPlayerInput;
  player4: AddMatchPlayerInput;
  player5: AddMatchPlayerInput;
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

export type CaptainNotOnTeam = ExpectedError & {
  __typename?: 'CaptainNotOnTeam';
  message: Scalars['String'];
};

export type DuplicatePlayers = ExpectedError & {
  __typename?: 'DuplicatePlayers';
  message: Scalars['String'];
};

export type DuplicateStartSide = ExpectedError & {
  __typename?: 'DuplicateStartSide';
  message: Scalars['String'];
};

export type ExpectedError = {
  message: Scalars['String'];
};

export type FilenameTooLong = ExpectedError & {
  __typename?: 'FilenameTooLong';
  message: Scalars['String'];
};

export type LoggedInUser = Node & {
  __typename?: 'LoggedInUser';
  avatarUrl: Scalars['String'];
  id: Scalars['ID'];
  role: Role;
  roles: Array<Role>;
  steamUsername: Scalars['String'];
  username: Scalars['String'];
};

export type Map = Node & {
  __typename?: 'Map';
  activeDuty: Scalars['Boolean'];
  filename: Scalars['String'];
  id: Scalars['ID'];
  mapName: Scalars['String'];
  removed: Scalars['Boolean'];
};

export type MapNameTooLong = ExpectedError & {
  __typename?: 'MapNameTooLong';
  message: Scalars['String'];
};

export type MapNotFound = ExpectedError & {
  __typename?: 'MapNotFound';
  message: Scalars['String'];
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

export type MatchPlayer = Node & {
  __typename?: 'MatchPlayer';
  adr?: Maybe<Scalars['Int']>;
  assists: Scalars['Int'];
  avatar: AvatarUrl;
  deaths: Scalars['Int'];
  id: Scalars['ID'];
  kills: Scalars['Int'];
  mvps?: Maybe<Scalars['Int']>;
  playerId: Scalars['Int'];
  score?: Maybe<Scalars['Int']>;
  steamUsername: Scalars['String'];
};

export type MatchTeam = Node & {
  __typename?: 'MatchTeam';
  captainId?: Maybe<Scalars['Int']>;
  id: Scalars['ID'];
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
  addMap: AddMapPayload;
  addMatch: AddMatchPayload;
  addPlayer: Player;
  logout?: Maybe<Scalars['Void']>;
  removeMatch: Scalars['Boolean'];
  updateMap: UpdateMapPayload;
  updatePlayer: Player;
  updateUsername: Player;
};


export type MutationAddMapArgs = {
  mapData: AddMapInput;
};


export type MutationAddMatchArgs = {
  matchData: AddMatchInput;
};


export type MutationAddPlayerArgs = {
  steamId: Scalars['String'];
};


export type MutationRemoveMatchArgs = {
  matchId: Scalars['Int'];
};


export type MutationUpdateMapArgs = {
  mapData: UpdateMapInput;
};


export type MutationUpdatePlayerArgs = {
  playerData: UpdatePlayerInput;
};


export type MutationUpdateUsernameArgs = {
  username: Scalars['String'];
};

export type Node = {
  id: Scalars['ID'];
};

export type OnlyOneCaptainSet = ExpectedError & {
  __typename?: 'OnlyOneCaptainSet';
  message: Scalars['String'];
};

export enum Outcome {
  Lost = 'LOST',
  Tied = 'TIED',
  Won = 'WON'
}

export type Player = Node & PlayerAggregates & TeamAggregates & {
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
  username: Scalars['String'];
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

export type PlayerNotFound = ExpectedError & {
  __typename?: 'PlayerNotFound';
  message: Scalars['String'];
};

export type Query = {
  __typename?: 'Query';
  currentUser?: Maybe<LoggedInUser>;
  /** Get a list of all maps. (Incl. removed maps) */
  maps: Array<Map>;
  match?: Maybe<Match>;
  matches: Array<Match>;
  /** Get a list of all playable maps. */
  playableMaps: Array<Map>;
  /** Get a single player by their SteamID. */
  player: Player;
  /** Get a list of all players. */
  players: Array<Player>;
  recentMatch?: Maybe<Match>;
  /** Get a list of all users. */
  users: Array<Player>;
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
  Removed = 'REMOVED',
  User = 'USER'
}

export type ScoreRulesInvalid = ExpectedError & {
  __typename?: 'ScoreRulesInvalid';
  message: Scalars['String'];
};

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

export type UpdateMapErrors = FilenameTooLong | MapNameTooLong;

export type UpdateMapInput = {
  activeDuty: Scalars['Boolean'];
  filename: Scalars['String'];
  id: Scalars['ID'];
  mapName: Scalars['String'];
  removed: Scalars['Boolean'];
};

export type UpdateMapPayload = {
  __typename?: 'UpdateMapPayload';
  errors: Array<UpdateMapErrors>;
  map?: Maybe<Map>;
};

export type UpdatePlayerInput = {
  playerId: Scalars['Int'];
  role: UpdatePlayerInputRole;
  username: Scalars['String'];
};

export enum UpdatePlayerInputRole {
  Mod = 'MOD',
  Ref = 'REF',
  Removed = 'REMOVED',
  User = 'USER'
}

export type GetLoggedInUserQueryVariables = Exact<{ [key: string]: never; }>;


export type GetLoggedInUserQuery = { __typename?: 'Query', currentUser?: { __typename?: 'LoggedInUser', id: string, role: Role, steamUsername: string, username: string, avatarUrl: string, roles: Array<Role> } | null };

export type LogoutMutationVariables = Exact<{ [key: string]: never; }>;


export type LogoutMutation = { __typename?: 'Mutation', logout?: any | null };

export type GetMatchListQueryVariables = Exact<{ [key: string]: never; }>;


export type GetMatchListQuery = { __typename?: 'Query', matches: Array<{ __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', id: string, mapName: string }, teams: Array<{ __typename?: 'MatchTeam', id: string, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, playerId: number, avatar: { __typename?: 'AvatarUrl', mediumAvatarUrl: string } }> }> }> };

export type GetRecentMatchQueryVariables = Exact<{ [key: string]: never; }>;


export type GetRecentMatchQuery = { __typename?: 'Query', recentMatch?: { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', id: string, mapName: string }, teams: Array<{ __typename?: 'MatchTeam', id: string, captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> } | null };

export type RecentMatchFragment = { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', id: string, mapName: string }, teams: Array<{ __typename?: 'MatchTeam', id: string, captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> };

export type RecentMatchTeamFragment = { __typename?: 'MatchTeam', id: string, captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> };

export type MatchListFragment = { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', id: string, mapName: string }, teams: Array<{ __typename?: 'MatchTeam', id: string, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, playerId: number, avatar: { __typename?: 'AvatarUrl', mediumAvatarUrl: string } }> }> };

export type GetPlayerListQueryVariables = Exact<{ [key: string]: never; }>;


export type GetPlayerListQuery = { __typename?: 'Query', players: Array<{ __typename?: 'Player', id: string, username: string, lastSeen: any, avatar: { __typename?: 'AvatarUrl', mediumAvatarUrl: string } }> };

export type PlayerListFragment = { __typename?: 'Player', id: string, username: string, lastSeen: any, avatar: { __typename?: 'AvatarUrl', mediumAvatarUrl: string } };

export type GetAllMapsQueryVariables = Exact<{ [key: string]: never; }>;


export type GetAllMapsQuery = { __typename?: 'Query', maps: Array<{ __typename?: 'Map', activeDuty: boolean, mapName: string, id: string, filename: string, removed: boolean }> };

export type AddMapMutationVariables = Exact<{
  mapData: AddMapInput;
}>;


export type AddMapMutation = { __typename?: 'Mutation', addMap: { __typename?: 'AddMapPayload', errors: Array<{ __typename?: 'FilenameTooLong', message: string } | { __typename?: 'MapNameTooLong', message: string }>, map?: { __typename?: 'Map', activeDuty: boolean, mapName: string, id: string, filename: string, removed: boolean } | null } };

export type UpdateMapMutationVariables = Exact<{
  mapData: UpdateMapInput;
}>;


export type UpdateMapMutation = { __typename?: 'Mutation', updateMap: { __typename?: 'UpdateMapPayload', errors: Array<{ __typename?: 'FilenameTooLong', message: string } | { __typename?: 'MapNameTooLong', message: string }>, map?: { __typename?: 'Map', activeDuty: boolean, mapName: string, id: string, filename: string, removed: boolean } | null } };

export type ManageMapsFragment = { __typename?: 'Map', activeDuty: boolean, mapName: string, id: string, filename: string, removed: boolean };

export type GetAllUsersQueryVariables = Exact<{ [key: string]: never; }>;


export type GetAllUsersQuery = { __typename?: 'Query', users: Array<{ __typename?: 'Player', gamesPlayed: number, username: string, steamUsername: string, role: Role, id: string, steamId: any, avatar: { __typename?: 'AvatarUrl', mediumAvatarUrl: string } }> };

export type UpdateUserMutationVariables = Exact<{
  playerData: UpdatePlayerInput;
}>;


export type UpdateUserMutation = { __typename?: 'Mutation', updatePlayer: { __typename?: 'Player', id: string, role: Role, username: string } };

export type WhitelistPlayerMutationVariables = Exact<{
  steamId: Scalars['String'];
}>;


export type WhitelistPlayerMutation = { __typename?: 'Mutation', addPlayer: { __typename?: 'Player', steamId: any, id: string, steamUsername: string, username: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } } };

export type ManageUsersFragment = { __typename?: 'Player', gamesPlayed: number, username: string, steamUsername: string, role: Role, id: string, steamId: any, avatar: { __typename?: 'AvatarUrl', mediumAvatarUrl: string } };

export type AddMatchSelectsQueryVariables = Exact<{ [key: string]: never; }>;


export type AddMatchSelectsQuery = { __typename?: 'Query', playableMaps: Array<{ __typename?: 'Map', mapName: string, id: string }>, players: Array<{ __typename?: 'Player', username: string, steamUsername: string, id: string }> };

export type AddMatchMutationVariables = Exact<{
  matchData: AddMatchInput;
}>;


export type AddMatchMutation = { __typename?: 'Mutation', addMatch: { __typename?: 'AddMatchPayload', match?: { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', mapName: string }, teams: Array<{ __typename?: 'MatchTeam', captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> } | null, errors: Array<{ __typename: 'CaptainNotOnTeam', message: string } | { __typename: 'DuplicatePlayers', message: string } | { __typename: 'DuplicateStartSide', message: string } | { __typename: 'MapNotFound', message: string } | { __typename: 'OnlyOneCaptainSet', message: string } | { __typename: 'PlayerNotFound', message: string } | { __typename: 'ScoreRulesInvalid', message: string }> } };

export type GetMatchQueryVariables = Exact<{
  matchId: Scalars['Int'];
}>;


export type GetMatchQuery = { __typename?: 'Query', match?: { __typename?: 'Match', datePlayed: any, id: string, score: string, map: { __typename?: 'Map', id: string, mapName: string }, teams: Array<{ __typename?: 'MatchTeam', id: string, captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> }> } | null };

export type MatchTeamFragment = { __typename?: 'MatchTeam', id: string, captainId?: number | null, outcome: Outcome, roundsWon: number, startSide: TeamSide, teamId: number, matchPlayers: Array<{ __typename?: 'MatchPlayer', id: string, deaths: number, kills: number, playerId: number, assists: number, steamUsername: string, avatar: { __typename?: 'AvatarUrl', smallAvatarUrl: string } }> };

export const RecentMatchTeamFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"recentMatchTeam"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"MatchTeam"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"captainId"}},{"kind":"Field","name":{"kind":"Name","value":"outcome"}},{"kind":"Field","name":{"kind":"Name","value":"roundsWon"}},{"kind":"Field","name":{"kind":"Name","value":"startSide"}},{"kind":"Field","name":{"kind":"Name","value":"teamId"}},{"kind":"Field","name":{"kind":"Name","value":"matchPlayers"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"deaths"}},{"kind":"Field","name":{"kind":"Name","value":"kills"}},{"kind":"Field","name":{"kind":"Name","value":"playerId"}},{"kind":"Field","name":{"kind":"Name","value":"assists"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"smallAvatarUrl"}}]}}]}}]}}]} as unknown as DocumentNode<RecentMatchTeamFragment, unknown>;
export const RecentMatchFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"recentMatch"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Match"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"datePlayed"}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"score"}},{"kind":"Field","name":{"kind":"Name","value":"map"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"mapName"}}]}},{"kind":"Field","name":{"kind":"Name","value":"teams"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"recentMatchTeam"}}]}}]}},...RecentMatchTeamFragmentDoc.definitions]} as unknown as DocumentNode<RecentMatchFragment, unknown>;
export const MatchListFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"matchList"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Match"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"datePlayed"}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"score"}},{"kind":"Field","name":{"kind":"Name","value":"map"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"mapName"}}]}},{"kind":"Field","name":{"kind":"Name","value":"teams"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"matchPlayers"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"playerId"}},{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"mediumAvatarUrl"}}]}}]}}]}}]}}]} as unknown as DocumentNode<MatchListFragment, unknown>;
export const PlayerListFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"playerList"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Player"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"mediumAvatarUrl"}}]}},{"kind":"Field","name":{"kind":"Name","value":"lastSeen"}}]}}]} as unknown as DocumentNode<PlayerListFragment, unknown>;
export const ManageMapsFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"manageMaps"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Map"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"activeDuty"}},{"kind":"Field","name":{"kind":"Name","value":"mapName"}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"filename"}},{"kind":"Field","name":{"kind":"Name","value":"removed"}}]}}]} as unknown as DocumentNode<ManageMapsFragment, unknown>;
export const ManageUsersFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"manageUsers"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Player"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"mediumAvatarUrl"}}]}},{"kind":"Field","name":{"kind":"Name","value":"gamesPlayed"}},{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"role"}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"steamId"}}]}}]} as unknown as DocumentNode<ManageUsersFragment, unknown>;
export const MatchTeamFragmentDoc = {"kind":"Document","definitions":[{"kind":"FragmentDefinition","name":{"kind":"Name","value":"matchTeam"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"MatchTeam"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"captainId"}},{"kind":"Field","name":{"kind":"Name","value":"outcome"}},{"kind":"Field","name":{"kind":"Name","value":"roundsWon"}},{"kind":"Field","name":{"kind":"Name","value":"startSide"}},{"kind":"Field","name":{"kind":"Name","value":"teamId"}},{"kind":"Field","name":{"kind":"Name","value":"matchPlayers"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"deaths"}},{"kind":"Field","name":{"kind":"Name","value":"kills"}},{"kind":"Field","name":{"kind":"Name","value":"playerId"}},{"kind":"Field","name":{"kind":"Name","value":"assists"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"smallAvatarUrl"}}]}}]}}]}}]} as unknown as DocumentNode<MatchTeamFragment, unknown>;
export const GetLoggedInUserDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetLoggedInUser"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"currentUser"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"role"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"Field","name":{"kind":"Name","value":"avatarUrl"}},{"kind":"Field","name":{"kind":"Name","value":"roles"}}]}}]}}]} as unknown as DocumentNode<GetLoggedInUserQuery, GetLoggedInUserQueryVariables>;
export const LogoutDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"Logout"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"logout"}}]}}]} as unknown as DocumentNode<LogoutMutation, LogoutMutationVariables>;
export const GetMatchListDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetMatchList"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"matches"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"matchList"}}]}}]}},...MatchListFragmentDoc.definitions]} as unknown as DocumentNode<GetMatchListQuery, GetMatchListQueryVariables>;
export const GetRecentMatchDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetRecentMatch"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"recentMatch"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"recentMatch"}}]}}]}},...RecentMatchFragmentDoc.definitions]} as unknown as DocumentNode<GetRecentMatchQuery, GetRecentMatchQueryVariables>;
export const GetPlayerListDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetPlayerList"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"players"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"playerList"}}]}}]}},...PlayerListFragmentDoc.definitions]} as unknown as DocumentNode<GetPlayerListQuery, GetPlayerListQueryVariables>;
export const GetAllMapsDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetAllMaps"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"maps"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"manageMaps"}}]}}]}},...ManageMapsFragmentDoc.definitions]} as unknown as DocumentNode<GetAllMapsQuery, GetAllMapsQueryVariables>;
export const AddMapDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"AddMap"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"mapData"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"AddMapInput"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"addMap"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"mapData"},"value":{"kind":"Variable","name":{"kind":"Name","value":"mapData"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"errors"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"InlineFragment","typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"ExpectedError"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"message"}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"map"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"manageMaps"}}]}}]}}]}},...ManageMapsFragmentDoc.definitions]} as unknown as DocumentNode<AddMapMutation, AddMapMutationVariables>;
export const UpdateMapDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"UpdateMap"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"mapData"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"UpdateMapInput"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"updateMap"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"mapData"},"value":{"kind":"Variable","name":{"kind":"Name","value":"mapData"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"errors"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"InlineFragment","typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"ExpectedError"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"message"}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"map"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"manageMaps"}}]}}]}}]}},...ManageMapsFragmentDoc.definitions]} as unknown as DocumentNode<UpdateMapMutation, UpdateMapMutationVariables>;
export const GetAllUsersDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetAllUsers"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"users"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"manageUsers"}}]}}]}},...ManageUsersFragmentDoc.definitions]} as unknown as DocumentNode<GetAllUsersQuery, GetAllUsersQueryVariables>;
export const UpdateUserDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"UpdateUser"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"playerData"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"UpdatePlayerInput"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"updatePlayer"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"playerData"},"value":{"kind":"Variable","name":{"kind":"Name","value":"playerData"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"role"}},{"kind":"Field","name":{"kind":"Name","value":"username"}}]}}]}}]} as unknown as DocumentNode<UpdateUserMutation, UpdateUserMutationVariables>;
export const WhitelistPlayerDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"WhitelistPlayer"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"steamId"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"addPlayer"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"steamId"},"value":{"kind":"Variable","name":{"kind":"Name","value":"steamId"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"steamId"}},{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"smallAvatarUrl"}}]}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"username"}}]}}]}}]} as unknown as DocumentNode<WhitelistPlayerMutation, WhitelistPlayerMutationVariables>;
export const AddMatchSelectsDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"AddMatchSelects"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"playableMaps"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"mapName"}},{"kind":"Field","name":{"kind":"Name","value":"id"}}]}},{"kind":"Field","name":{"kind":"Name","value":"players"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"id"}}]}}]}}]} as unknown as DocumentNode<AddMatchSelectsQuery, AddMatchSelectsQueryVariables>;
export const AddMatchDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"AddMatch"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"matchData"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"AddMatchInput"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"addMatch"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"matchData"},"value":{"kind":"Variable","name":{"kind":"Name","value":"matchData"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"match"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"datePlayed"}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"score"}},{"kind":"Field","name":{"kind":"Name","value":"map"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"mapName"}}]}},{"kind":"Field","name":{"kind":"Name","value":"teams"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"captainId"}},{"kind":"Field","name":{"kind":"Name","value":"outcome"}},{"kind":"Field","name":{"kind":"Name","value":"roundsWon"}},{"kind":"Field","name":{"kind":"Name","value":"startSide"}},{"kind":"Field","name":{"kind":"Name","value":"teamId"}},{"kind":"Field","name":{"kind":"Name","value":"matchPlayers"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"deaths"}},{"kind":"Field","name":{"kind":"Name","value":"kills"}},{"kind":"Field","name":{"kind":"Name","value":"playerId"}},{"kind":"Field","name":{"kind":"Name","value":"assists"}},{"kind":"Field","name":{"kind":"Name","value":"steamUsername"}},{"kind":"Field","name":{"kind":"Name","value":"avatar"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"smallAvatarUrl"}}]}}]}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"errors"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"__typename"}},{"kind":"InlineFragment","typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"ExpectedError"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"message"}}]}}]}}]}}]}}]} as unknown as DocumentNode<AddMatchMutation, AddMatchMutationVariables>;
export const GetMatchDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetMatch"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"matchId"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Int"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"match"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"matchId"},"value":{"kind":"Variable","name":{"kind":"Name","value":"matchId"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"datePlayed"}},{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"score"}},{"kind":"Field","name":{"kind":"Name","value":"map"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"mapName"}}]}},{"kind":"Field","name":{"kind":"Name","value":"teams"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"matchTeam"}}]}}]}}]}},...MatchTeamFragmentDoc.definitions]} as unknown as DocumentNode<GetMatchQuery, GetMatchQueryVariables>;