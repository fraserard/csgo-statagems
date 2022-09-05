import { Avatar, Select, TextInput } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useContext, useMemo } from "react";
import { useMutation } from "urql";
import useToggleFormButtons from "~/components/useToggleFormButtons";
import {
  Role,
  UpdatePlayerInput,
  UpdatePlayerInputRole,
  UpdateUserDocument,
  UpdateUserMutation,
  UpdateUserMutationVariables,
} from "~/graphql";
import { useUser } from "~/contexts/UserContext";

interface UsersTableRowProps {
  id: string;
  username: string;
  avatarUrl: string;
  role: Role;
  steamUsername: string;
  steamId: string;
  gamesPlayed: number;
  editUser: (user: UpdatePlayerInput) => void;
}

export default function UsersTableRow({
  id,
  username,
  avatarUrl,
  role,
  steamUsername,
  steamId,
  gamesPlayed,
  editUser,
}: UsersTableRowProps) {
  const form = useForm({
    initialValues: {
      id: id,
      username: username,
      role: role,
    },

    validate: {
      username: (value) =>
        value.length < 2 || value.length > 32 ? "Username must be between 2-32 characters" : null,
    },
  });
  type FormValues = typeof form.values;

  const [, updateUser] = useMutation<UpdateUserMutation, UpdateUserMutationVariables>(
    UpdateUserDocument
  );

  const submitForm = async (values: FormValues) => {
    console.log(values);
    const playerData: UpdatePlayerInput = {
      playerId: parseInt(values.id),
      role: values.role as unknown as UpdatePlayerInputRole,
      username: values.username!,
    };
    await updateUser({ playerData }).then((result) => {
      if (result.data?.updatePlayer) {
        const player = result.data!.updatePlayer;
        editUser({
          playerId: parseInt(player.id),
          role: player.role as unknown as UpdatePlayerInputRole,
          username: player.username,
        });
        toggleLock();
        form.resetDirty();
      }
    });
  };

  const { user } = useUser();

  const roleOptions = useMemo(
    () =>
      Object.values(Role).map((r) => ({
        value: r,
        label: r,
        disabled: r === Role.Admin || r === user!.role,
      })),
    []
  );

  const [locked, toggleLock, buttons] = useToggleFormButtons(form);
  const canEdit = (user?.role !== role && user?.role !== Role.Admin) || user?.role === Role.Admin;
  return (
    <tr>
      <td>
        <Avatar src={avatarUrl} />
      </td>
      <td>
        <TextInput disabled={locked} {...form.getInputProps("username")} />
      </td>
      <td>
        <Select
          disabled={locked || role === Role.Admin || user!.id === id}
          data={roleOptions}
          {...form.getInputProps("role")}
        />
      </td>
      <td>{steamUsername}</td>
      <td>{steamId}</td>
      <td>{gamesPlayed}</td>
      <td>
        <form onSubmit={form.onSubmit((values) => submitForm(values))}>{canEdit && buttons}</form>
      </td>
    </tr>
  );
}
