import React from 'react';
import UserProvider from './user';
import AuthProvider from './auth';

const RootContextProvider = ({ children }) => (
    <AuthProvider>
        <UserProvider>
            {children}
        </UserProvider>
    </AuthProvider>
);

export default RootContextProvider;