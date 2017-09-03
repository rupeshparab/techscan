import React from 'react';
import PropTypes from 'prop-types';

const TechnologyStats = ({ name, count }) => {

  return (
    <div>
      <span>{name}</span>
      <span className="count">{count.toLocaleString('en-IN')}</span>
    </div>
  );
};

TechnologyStats.propTypes = {
  name: PropTypes.string.isRequired,
  count: PropTypes.number.isRequired,
};

export default TechnologyStats;
