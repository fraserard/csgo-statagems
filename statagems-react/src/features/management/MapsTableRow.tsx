import { Checkbox, TextInput } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useMutation } from "urql";
import useToggleFormButtons from "~/components/useToggleFormButtons";
import {
  ManageMapsFragment,
  UpdateMapDocument,
  UpdateMapMutation,
  UpdateMapMutationVariables,
} from "~/graphql";

interface MapsTableRowProps {
  map: ManageMapsFragment;
  editMap: (map: ManageMapsFragment) => void;
}

export default function MapsTableRow({ map, editMap }: MapsTableRowProps) {
  const form = useForm({
    initialValues: {
      id: map.id,
      filename: map.filename,
      mapName: map.mapName,
      activeDuty: map.activeDuty,
      removed: map.removed,
    },

    validate: {
      mapName: (value) =>
        value.length < 2 || value.length > 32 ? "Map name must be between 2-32 characters" : null,
        filename: (value) =>
        value.length < 2 || value.length > 32 ? "Filename must be between 2-32 characters" : null,
    },
  });
  type FormValues = typeof form.values;

  const [locked, toggleLock, buttons] = useToggleFormButtons(form);

  const [, updateMap] = useMutation<UpdateMapMutation, UpdateMapMutationVariables>(
    UpdateMapDocument
  );

  const submitForm = async (values: FormValues) => {
    await updateMap({ mapData: values }).then((result) => {
      if (result.data?.updateMap.map!) {
        const map = result.data?.updateMap.map;
        editMap({ ...map });
        toggleLock();
        form.resetDirty();
      }
    });
  };

  return (
    <tr>
      <td>
        <TextInput disabled={locked} {...form.getInputProps("filename")} />
      </td>
      <td>
        <TextInput disabled={locked} {...form.getInputProps("mapName")} />
      </td>
      <td>
        <Checkbox disabled={locked} {...form.getInputProps("activeDuty", { type: "checkbox" })} />
      </td>
      <td>
        <Checkbox disabled={locked} {...form.getInputProps("removed", { type: "checkbox" })} />
      </td>
      <td>
        <form onSubmit={form.onSubmit((values) => submitForm(values))}>{buttons}</form>
      </td>
    </tr>
  );
}
