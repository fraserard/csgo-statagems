import { Table } from "@mantine/core";
import { GetAllUsersQuery, Role, UpdatePlayerInput } from "~/graphql";
import UsersTableRow from "./UsersTableRow";

interface UsersTableProps {
  users: GetAllUsersQuery["users"];
  editUser: (user: UpdatePlayerInput) => void;
}

export default function UsersTable({ users, editUser }: UsersTableProps) {
  const rows = users.map((user) => (
    <UsersTableRow
      key={user.id}
      id={user.id}
      username={user.username}
      role={user.role}
      steamUsername={user.steamUsername}
      steamId={user.steamId}
      gamesPlayed={user.gamesPlayed}
      avatarUrl={user.avatar.mediumAvatarUrl}
      editUser={editUser}
    />
  ));
  return (
    <Table>
      <thead>
        <tr>
          <th></th>
          <th>Username</th>
          <th>Role</th>
          <th>Steam Name</th>
          <th>Steam ID</th>
          <th>Games Played</th>
          <th></th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </Table>
  );
}
