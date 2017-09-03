import React from 'react';
import PropTypes from 'prop-types';
import TimeAgo from '../utils/helpers';

const ResultRepository = ({ name, url, desc, tags, lastUpdated }) => {

  return (
    <div className="result-item">
      <span className="heading">
        <a href={"/author/"+url}>
          <h2>{name}</h2>
        </a>
        <span className="repo-meta">
          <span className="oi oi-star"></span>
          57.1k
        </span>
        <span className="repo-meta">
          <span className="oi oi-media-record"></span>
          JavaScript
        </span>
      </span>
      <span>
        {desc}
      </span>
      {tags &&
        <div className="tags">
          {tags.split(",").map((tag, i) =>
            <span key={i}><a href={"/repo/"+tag}>{tag}</a></span>
          )}
        </div>
      }

      <span className="last-updated">Updated {TimeAgo(lastUpdated)}</span>
    </div>
  );
};

ResultRepository.propTypes = {
  name: PropTypes.string.isRequired,
  url: PropTypes.string.isRequired,
};

export default ResultRepository;
