import React from 'react';
import Signin from '../components/signin';
import Signup from '../components/signup';
import { Route } from 'react-router-dom';

const AuthLayout = ({match}) => (
    <>
        <Route path={`${match.path}/signin`} component={Signin} />
        <Route path={`${match.path}/signup`} component={Signup} />
    </>
)

export default AuthLayout;
