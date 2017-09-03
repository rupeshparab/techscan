import React from 'react';
import ReactDOM from 'react-dom';
import HomePageContainer from 'containers/HomePageContainer';
import ResultPageContainer from 'containers/ResultPageContainer';


console.log(window);
if (window.location.pathname.startsWith("/repo/")) {
  ReactDOM.render(<ResultPageContainer />, document.getElementById('react-app'));
} else {
  ReactDOM.render(<HomePageContainer />, document.getElementById('react-app'));
}
