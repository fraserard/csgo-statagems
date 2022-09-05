import {
  ActionIcon,
  Burger,
  Group,
  Header as MantineHeader,
  MediaQuery,
  Title,
  useMantineColorScheme,
  useMantineTheme,
} from "@mantine/core";
import { IconMoonStars, IconSun } from "@tabler/icons";
import { Link } from "react-router-dom";

interface HeaderProps {
  pageTitle: string;
  opened: boolean;
  setOpened: React.Dispatch<React.SetStateAction<boolean>>;
}

export function Header({ pageTitle, opened, setOpened }: HeaderProps) {
  const { colorScheme, toggleColorScheme } = useMantineColorScheme();
  const theme = useMantineTheme();
  return (
    <MantineHeader height={70} p="md">
      <Group position="apart">
        <MediaQuery largerThan="sm" styles={{ display: "none" }}>
          <Burger
            opened={opened}
            onClick={() => setOpened((o) => !o)}
            size="sm"
            color={theme.colors.gray[6]}
            mr="xl"
          />
        </MediaQuery>
        <Link to="/">
          <Title order={1}>STATAGEMS!</Title>
        </Link>
        <Title order={2}>{pageTitle}</Title>
        <ActionIcon variant="default" onClick={() => toggleColorScheme()} size={30}>
          {colorScheme === "dark" ? <IconSun size={16} /> : <IconMoonStars size={16} />}
        </ActionIcon>
      </Group>
    </MantineHeader>
  );
}
