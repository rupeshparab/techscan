import React from 'react';
import PropTypes from 'prop-types';

const TechnologyCard = ({ name, imgUrl }) => {

  const getUrl = () => {
    return '/repo/' + name;
  }

  return (
    <div className="card tech-card">
      <img height='100' src={imgUrl}></img>
      <a href={getUrl()}><span><h2>{name}</h2></span></a>
    </div>
  );
};

TechnologyCard.propTypes = {
  name: PropTypes.string.isRequired,
};

export default TechnologyCard;
