import {
    createClient,
    dedupExchange,
    cacheExchange,
    fetchExchange,
} from "urql";
import { devtoolsExchange } from '@urql/devtools';


const client = createClient({
    url: "http://127.0.0.1:5000/graphql",
    exchanges: [
        devtoolsExchange,
        dedupExchange, 
        cacheExchange, 
        fetchExchange,
    ],
    // fetchOptions: () => {
    //     return { 
    //         method: 'post',
    //         credentials: 'same-origin',
    //         headers: { 'X-CSRF-TOKEN': Cookies.get("csrf_access_token"),
    //     }, }; // auth headers
    // },
});

export { client };