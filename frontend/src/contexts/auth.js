import { createContext } from "react";

const authContext = createContext({
    currentUser: null,
    isAuth: false
});

export default authContext;
