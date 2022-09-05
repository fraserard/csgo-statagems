import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { getCookie } from "typescript-cookie";
import { useQuery } from "urql";
import { GetLoggedInUserDocument, GetLoggedInUserQuery, LoggedInUser } from "~/graphql";

type User = {
  user: LoggedInUser | null;
  setUser: React.Dispatch<React.SetStateAction<LoggedInUser | null>>;
};

const UserContext = createContext<User>({} as User);

export default function UserProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<LoggedInUser | null>(null);
  const userValue = useMemo(() => ({ user, setUser }), [user, setUser]);

  const [result] = useQuery<GetLoggedInUserQuery>({
    query: GetLoggedInUserDocument,
    context: useMemo(
      () => ({
        fetchOptions: () => {
          const csrfCookie = getCookie("statagems_csrf");
          return {
            headers: { "X-CSRF-TOKEN": csrfCookie ? csrfCookie : "" },
          };
        },
      }),
      []
    ),
  });

  const { data, fetching, error } = result;

  useEffect(() => {
    if (data?.currentUser) {
      setUser(data.currentUser);
    } else {
      setUser(null);
    }
  }, [data?.currentUser]);

  return <UserContext.Provider value={userValue}>{children}</UserContext.Provider>;
}

export function useUser() {
  return useContext(UserContext);
}
