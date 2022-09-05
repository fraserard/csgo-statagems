import { Loader, Space } from "@mantine/core";
import { useEffect, useState } from "react";
import { useQuery } from "urql";
import Error from "~/components/Error";
import Page from "~/layouts/Page";
import UsersTable from "~/features/management/UsersTable";
import WhitelistPlayerForm from "~/features/management/WhitelistPlayerForm";
import { GetAllUsersDocument, GetAllUsersQuery, Role, UpdatePlayerInput } from "~/graphql";

export default function ManagePlayersPage() {
  const [{ data, fetching, error }] =  useQuery<GetAllUsersQuery>({
    query: GetAllUsersDocument,
  });

  const [users, setUsers] = useState(data?.users);

  useEffect(() => {
    setUsers(data?.users);
  }, [data]);

  const addUser = (user: GetAllUsersQuery["users"][0]) => {
    setUsers((users) => users!.splice(0, 0, user));
  };

  const editUser = (user: UpdatePlayerInput) => {
    setUsers((users) =>
      users?.map((u) => {
        if (u.id === user.playerId.toString()) {
          return { ...u, username: user.username, role: user.role as unknown as Role };
        }
        return u;
      })
    );
  };

  return (
    <Page title="Manage Players">
      {fetching && <Loader />}
      {error && <Error message={error.message} />}
      {users && (
        <>
          <WhitelistPlayerForm addUser={addUser} />
          <Space h="lg"/>
          <UsersTable users={users!} editUser={editUser} />
        </>
      )}
    </Page>
  );
}
