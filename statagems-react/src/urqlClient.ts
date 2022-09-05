import { devtoolsExchange } from "@urql/devtools";
import { cacheExchange } from "@urql/exchange-graphcache";
import { getCookie } from "typescript-cookie";
import { createClient, dedupExchange, errorExchange, fetchExchange } from "urql";
import logout from "~/features/auth/logout";

const client = createClient({
  url: "/graphql",
  exchanges: [
    devtoolsExchange,
    dedupExchange,
    cacheExchange({
      keys: {
        AvatarUrl: () => null,
      },
    }),
    errorExchange({
      onError: (error) => {
        const isAuthError = error.message === "[GraphQL] Not permitted.";
        if (isAuthError) {
          logout();
        }
      },
    }),
    fetchExchange,
  ],
  fetchOptions: () => {
    const csrfCookie = getCookie("statagems_csrf");
    return {
      headers: { "X-CSRF-TOKEN": csrfCookie ? csrfCookie : "" },
    }; // auth headers
  },
});

export { client };
