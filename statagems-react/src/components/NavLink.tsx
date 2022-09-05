import { Box, createStyles, Group, ThemeIcon, UnstyledButton } from "@mantine/core";
import { TablerIcon } from "@tabler/icons";
import { Link, NavLink as ReactRouterNavLink } from "react-router-dom";
import { useUser } from "~/contexts/UserContext";
import { Role } from "~/graphql";

const useStyles = createStyles((theme) => ({
  control: {
    fontWeight: 500,
    display: "block",
    width: "100%",
    padding: `${theme.spacing.xs}px ${theme.spacing.md}px`,
    color: theme.colorScheme === "dark" ? theme.colors.dark[0] : theme.black,
    fontSize: theme.fontSizes.sm,

    "&:hover": {
      backgroundColor: theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.colors.gray[0],
      color: theme.colorScheme === "dark" ? theme.white : theme.black,
    },
  },
}));

interface NavLinkProps {
  icon: TablerIcon;
  label: string;
  link: string;
  minRole?: Role;
}

export function NavLink({ icon: Icon, label, link, minRole }: NavLinkProps) {
  const { classes, theme } = useStyles();
  const { user } = useUser();

  if (minRole && !user?.roles.includes(minRole)) {
    return <></>;
  }

  return (
    <>
      <UnstyledButton<typeof Link>
        component={Link}
        to={link}
        className={classes.control}
      >
        <Group position="apart" spacing={0}>
          <Box sx={{ display: "flex", alignItems: "center" }}>
            <ThemeIcon variant="light" size={30}>
              <Icon size={18} />
            </ThemeIcon>
            <Box ml="md">{label}</Box>
          </Box>
        </Group>
      </UnstyledButton>
    </>
  );
}
