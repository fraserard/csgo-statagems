import { useNavigate } from "react-router-dom";
import { useMutation } from "urql";
import { useUser } from "~/contexts/UserContext";
import { LogoutDocument } from "~/graphql";

export default function useLogout() {
  const navigate = useNavigate();
  const { user, setUser } = useUser();

  const [_, logoutUser] = useMutation(LogoutDocument);

  const logout = () => {
    logoutUser().then(() => {
      setUser(null);
      navigate("/");
      window.location.reload();
    });
  };

  return {logout};
}
