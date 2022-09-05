import { ActionIcon, Group } from "@mantine/core";
import { UseFormReturnType } from "@mantine/form";
import { IconDeviceFloppy, IconPencil, IconX } from "@tabler/icons";
import { useState } from "react";

export default function useToggleFormButtons(
  form: UseFormReturnType<any>,
  startLocked: boolean = true
): [boolean, () => void, JSX.Element] {
  const [locked, setLocked] = useState(startLocked);

  const formButtons = (
    <>
      <Group position="right">
        <ActionIcon hidden={!locked} onClick={() => setLocked(false)}>
          <IconPencil />
        </ActionIcon>

        <ActionIcon disabled={!form.isDirty()} hidden={locked} type="submit">
          <IconDeviceFloppy />
        </ActionIcon>
        <ActionIcon
          hidden={locked}
          onClick={() => {
            setLocked(true);
            form.reset();
          }}
        >
          <IconX />
        </ActionIcon>
      </Group>
    </>
  );

  const toggleLock = () => setLocked((locked) => (locked === true ? false : true));
  const isLocked = locked;
  return [isLocked, toggleLock, formButtons];
}
