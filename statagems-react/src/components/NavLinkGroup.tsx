import { Box, Collapse, createStyles, Group, Text, ThemeIcon, UnstyledButton } from "@mantine/core";
import { IconChevronLeft, IconChevronRight, TablerIcon } from "@tabler/icons";
import { useState } from "react";
import { NavLink } from "react-router-dom";
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

  link: {
    fontWeight: 500,
    display: "block",
    textDecoration: "none",
    padding: `${theme.spacing.xs}px ${theme.spacing.md}px`,
    paddingLeft: 31,
    marginLeft: 30,
    fontSize: theme.fontSizes.sm,
    color: theme.colorScheme === "dark" ? theme.colors.dark[0] : theme.colors.gray[7],
    borderLeft: `1px solid ${theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[3]}`,

    "&:hover": {
      backgroundColor: theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.colors.gray[0],
      color: theme.colorScheme === "dark" ? theme.white : theme.black,
    },
  },

  chevron: {
    transition: "transform 200ms ease",
  },
}));

interface NavLinksGroupProps {
  icon: TablerIcon;
  label: string;
  initiallyOpened?: boolean;
  links: { label: string; link: string; minRole?: Role }[];
  minRole?: Role;
}

export function NavLinkGroup({ icon: Icon, label, initiallyOpened, links, minRole }: NavLinksGroupProps) {
  const { classes, theme } = useStyles();
  const { user } = useUser();

  const hasLinks = Array.isArray(links);
  const [opened, setOpened] = useState(initiallyOpened || false);

  const ChevronIcon = theme.dir === "ltr" ? IconChevronRight : IconChevronLeft;

  if (minRole && !user?.roles.includes(minRole)) {
    return <></>;
  }

  const items = (hasLinks ? links : []).map((link) => {
    if (link.minRole && !user?.roles.includes(link.minRole)) {
      return <></>;
    }

    return (
      <Text<typeof NavLink> component={NavLink} className={classes.link} to={link.link} key={link.label}>
        {link.label}
      </Text>
    );
  });

  return (
    <>
      <UnstyledButton onClick={() => setOpened((o) => !o)} className={classes.control}>
        <Group position="apart" spacing={0}>
          <Box sx={{ display: "flex", alignItems: "center" }}>
            <ThemeIcon variant="light" size={30}>
              <Icon size={18} />
            </ThemeIcon>
            <Box ml="md">{label}</Box>
          </Box>
          {hasLinks && (
            <ChevronIcon
              className={classes.chevron}
              size={14}
              stroke={1.5}
              style={{
                transform: opened ? `rotate(${theme.dir === "rtl" ? -90 : 90}deg)` : "none",
              }}
            />
          )}
        </Group>
      </UnstyledButton>
      {hasLinks ? <Collapse in={opened}>{items}</Collapse> : null}
    </>
  );
}
