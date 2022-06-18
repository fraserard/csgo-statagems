import React, { ReactNode } from "react";
import styles from "./Page.module.css";
import Titlebar from "./Titlebar/Titlebar";


export function Page({ children }: { children: ReactNode | ReactNode[] }) {
  return (
    <div className={styles.container}>
      <div className={styles.page}>
        <div>
          <Titlebar/>
          {/* <Navigation /> */}
          <div className={styles.content}>{children}</div>
        </div>
        {/* <Footer /> */}
      </div>
    </div>
  );
}