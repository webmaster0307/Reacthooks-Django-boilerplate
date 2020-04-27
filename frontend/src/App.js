import React from 'react';
import {
  Route
} from "react-router-dom";

import Header from './components/header'
import AuthLayout from './pages/authLayout';

function App() {
  return (
    <>
      <Header />
      {/* <switch> */}
        <Route path='/auth' component={AuthLayout} />
        {/* <Route exact path='/' component={AuthLayout} /> */}
      {/* </switch> */}
    </>
  );
}

export default App;
