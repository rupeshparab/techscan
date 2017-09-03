import React from 'react';
import TechnologyCard from 'components/TechnologyCard';
import TechnologyStats from 'components/TechnologyStats';
import axios from 'axios';

/* You also get this warning in v1.x if you write your root component as
   stateless plain function instead of using React.Component. This problem
   is already solved completely in the upcoming v3.x.
   https://github.com/gaearon/react-hot-loader/blob/4978bffbb82a2508cf5d4ef2eee8b9b9101284ad/docs/Troubleshooting.md */
// eslint-disable-next-line react/prefer-stateless-function
export default class HomePageContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      technologies: [],
      meta: null
    };
  }

  componentDidMount() {
    axios.get('/api/technology/')
      .then(res => {
        const technologies = res.data.objects;
        const meta = res.data.meta;
        this.setState({ technologies, meta });
      });
  }

  render() {
    // const technologies = [
    //   {
    //     name: 'JavaScript',
    //     url: 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
    //     count: 8396
    //   },
    //   {
    //     name: 'Java',
    //     url: 'http://logodatabases.com/wp-content/uploads/2012/03/java-logo-large.png',
    //     count: 9761
    //   },
    //   {
    //     name: 'Python',
    //     url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/480px-Python.svg.png',
    //     count: 9894
    //   }
    // ];

    return (
      <div className="row">
        <div className="col-8">
        {this.state.technologies.map((tech, i) =>
          <TechnologyCard key={i} name={tech.name} imgUrl={tech.image_url} />
        )}
        </div>
        <div className="col-4">
          <div className="card stat">
            <h3>Languages</h3>
            { this.state.technologies.map((tech, i) =>
                <TechnologyStats key={i} name={tech.name} count={tech.repo_count} />
            )}
          </div>
        </div>
      </div>
    );
  }
}
