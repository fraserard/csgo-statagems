import {
  Avatar,
  Center,
  createStyles,
  Group,
  Menu,
  Navbar as MantineNavbar,
  Paper,
  ScrollArea,
  Text,
} from "@mantine/core";
import { IconGauge, IconHome, IconSettings, IconUser } from "@tabler/icons";
import { useNavigate } from "react-router-dom";
import { NavLink } from "~/components/NavLink";
import { useUser } from "~/contexts/UserContext";
import useLogout from "~/features/auth/logout";
import { Role } from "~/graphql";
import { NavLinkGroup } from "../components/NavLinkGroup";
import steamLoginButton from "./login_steam_large.png";

const useStyles = createStyles((theme) => ({
  navbar: {
    backgroundColor: theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.white,
    paddingBottom: theme.spacing.xl,
  },

  links: {
    marginLeft: -theme.spacing.md,
    marginRight: -theme.spacing.md,
  },

  linksInner: {
    paddingTop: theme.spacing.md,
    paddingBottom: theme.spacing.xl,
  },

  footer: {
    // marginLeft: -theme.spacing.md,
    // marginRight: -theme.spacing.md,
    // paddingBottom: theme.spacing.md,
    paddingTop: theme.spacing.md,
    borderTop: `1px solid ${theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]}`,
  },
}));

interface NavbarProps {
  opened: boolean;
}

export function Navbar({ opened }: NavbarProps) {
  const { classes } = useStyles();
  const { user } = useUser();
  const navigate = useNavigate();
  const { logout } = useLogout();
  const links = (
    <>
      <NavLink label="Home" icon={IconHome} link="/" />
      <NavLink label="Add Match" icon={IconGauge} link="/match/add" minRole={Role.Ref} />
      <NavLink label="Your Profile" icon={IconUser} link={`/player/${user?.id}`} minRole={Role.User} />
    </>
  );

  const settings = (
    <NavLinkGroup
      label="Settings"
      icon={IconSettings}
      minRole={Role.Ref}
      links={[
        { label: "Change username", link: "/", minRole: Role.User },
        { label: "Manage players", link: "/manage/players", minRole: Role.Mod },
        { label: "Manage maps", link: "/manage/maps", minRole: Role.Mod },
      ]}
    />
  );

  return (
    <MantineNavbar
      p="md"
      hiddenBreakpoint="sm"
      hidden={!opened}
      width={{ sm: 250, lg: 350 }}
      className={classes.navbar}
    >
      <MantineNavbar.Section grow className={classes.links} component={ScrollArea}>
        <div className={classes.linksInner}>{links}</div>
      </MantineNavbar.Section>
      <MantineNavbar.Section className={classes.links} pb="md">
        {settings}
      </MantineNavbar.Section>
      <MantineNavbar.Section className={classes.footer}>
        <Center>
          {user?.roles.includes(Role.User) ? (
            <Menu shadow="md" position="top">
              <Menu.Target>
                <Paper
                  style={{ cursor: "pointer" }}
                  p="xs"
                  pr="xl"
                  pl="xl"
                  withBorder
                  radius="md"
                  shadow="lg"
                >
                  <Group>
                    <Avatar src={user.avatarUrl} size="md" radius="md" />
                    <Text>{user.steamUsername}</Text>
                  </Group>
                </Paper>
              </Menu.Target>
              <Menu.Dropdown>
                <Menu.Item onClick={() => navigate(`/player/${user.id}`)}>Your Profile</Menu.Item>
                <Menu.Item onClick={logout}>Logout</Menu.Item>
              </Menu.Dropdown>
            </Menu>
          ) : (
            <a href="/auth/login">
              <img src={steamLoginButton} />
            </a>
          )}
        </Center>
      </MantineNavbar.Section>
    </MantineNavbar>
  );
}
