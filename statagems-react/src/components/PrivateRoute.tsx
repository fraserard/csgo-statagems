import { ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { useUser } from "~/contexts/UserContext";
import { Role } from "~/graphql";

export default function PrivateRoute({ minRole, page }: { minRole: Role, page: JSX.Element }): JSX.Element {
  const { user } = useUser();

  if (user?.roles.includes(minRole)) {
    return page;
  } else {
    return <Navigate to="/" />;
  }
}
