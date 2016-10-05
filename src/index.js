import React from 'react';
import { render } from 'react-dom';
import { Router, Route, IndexRoute, browserHistory } from 'react-router';
import 電視 from './電視/電視';
import './App/App.css';

import Debug from 'debug';
Debug.enable('lo5ik8:*');

const root = document.getElementById('app');

let history = browserHistory;
render(
  <Router history={history}>
      <Route path='*' component={電視} />
  </Router>,
  root
);
