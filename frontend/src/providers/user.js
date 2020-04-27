import React, { useReducer, useContext } from "react";
import userContext from "../contexts/user";
import userReducer from "../reducers/user";

const UserProvider = props => {
    const initialState = useContext(userContext);
    const [state, dispatch] = useReducer(userReducer, initialState);

    return (
        <userContext.Provider value={{ state, dispatch }}>
            {props.children}
        </userContext.Provider>
    );
};

export default UserProvider;
