import React, { useReducer, useContext, useEffect } from 'react';
import authContext from '../contexts/auth';
import authReducer from '../reducers/auth';

const AuthProvider = props => {
    const initialState = useContext(authContext);
    const [state, dispatch] = useReducer(authReducer, initialState);

    useEffect(() => {
        const user = JSON.parse(localStorage.getItem('user'));
        const token = localStorage.getItem('token');

        if (user && token) {
            user.token = token;
            dispatch({
                type: 'LOGIN_SUCCESS',
                payload: user
            });
        }
    }, []);

    return (
        <authContext.Provider value={{ state, dispatch }}>
            {props.children}
        </authContext.Provider>
    );
};

export default AuthProvider;
