import { AppShell, Aside, Center, Footer, MediaQuery } from "@mantine/core";
import { ReactNode, useState } from "react";
import { Header } from "./Header";
import { Navbar } from "./Navbar";

interface PageProps {
  children: ReactNode;
  title: string;
}

export default function Page({ children, title }: PageProps) {
  const [opened, setOpened] = useState(false);

  return (
    <AppShell
      padding="md"
      navbarOffsetBreakpoint="sm"
   
      navbar={<Navbar opened={opened} />}
      header={<Header pageTitle={title} opened={opened} setOpened={setOpened} />}
      footer={
        <Footer height={60} p="md">
          <Center>Statagems. Fraser Ard.</Center>
        </Footer>
      }
      aside={
        <MediaQuery smallerThan="xl" styles={{ display: "none" }}>
          <Aside hiddenBreakpoint="xl" width={{ xl: 200 }}>

          </Aside>
        </MediaQuery>
      }
    >
      {/* <Container></Container> */}
      {children}
    </AppShell>
  );
}
