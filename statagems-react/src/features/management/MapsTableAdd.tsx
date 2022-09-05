import { ActionIcon, Checkbox, Group, TextInput } from "@mantine/core";
import { useForm } from "@mantine/form";
import { IconPlus } from "@tabler/icons";
import { useMutation } from "urql";
import { AddMapDocument, AddMapMutation, AddMapMutationVariables, ManageMapsFragment } from "~/graphql";

interface MapsTableAddProps {
  addMap: (map: ManageMapsFragment) => void;
}

export default function MapsTableAdd({ addMap }: MapsTableAddProps) {
  const form = useForm({
    initialValues: {
      filename: "",
      mapName: "",
      activeDuty: false,
      removed: false,
    },

    validate: {
      mapName: (value) =>
        value.length < 2 || value.length > 32 ? "Map name must be between 2-32 characters" : null,
      filename: (value) =>
        value.length < 2 || value.length > 32 ? "Filename must be between 2-32 characters" : null,
    },
  });
  type FormValues = typeof form.values;

  const [, addMapMutation] = useMutation<AddMapMutation, AddMapMutationVariables>(AddMapDocument);

  const submitForm = async (values: FormValues) => {
    await addMapMutation({ mapData: values }).then((result) => {
      if (result.data?.addMap.map) {
        const map = result.data?.addMap.map;
        addMap({ ...map });
        form.reset();
      }
    });
  };

  return (
    <tr>
      <td>
        <TextInput placeholder="de_newmap" {...form.getInputProps("filename")} />
      </td>
      <td>
        <TextInput placeholder="New Map" {...form.getInputProps("mapName")} />
      </td>
      <td>
        <Checkbox {...form.getInputProps("activeDuty", { type: "checkbox" })} />
      </td>
      <td>
        <Checkbox {...form.getInputProps("removed", { type: "checkbox" })} />
      </td>
      <td>
        <form onSubmit={form.onSubmit((values) => submitForm(values))}>
          <Group position="right">
            <ActionIcon disabled={!form.isDirty()} type="submit">
              <IconPlus />
            </ActionIcon>
          </Group>
        </form>
      </td>
    </tr>
  );
}
