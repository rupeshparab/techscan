import React from 'react';
import TechnologyCard from 'components/TechnologyCard';
import TechnologyStats from 'components/TechnologyStats';
import ResultRepository from 'components/ResultRepository';
import axios from 'axios';
import Pluralize from 'pluralize';
import numeral from 'numeral';

/* You also get this warning in v1.x if you write your root component as
   stateless plain function instead of using React.Component. This problem
   is already solved completely in the upcoming v3.x.
   https://github.com/gaearon/react-hot-loader/blob/4978bffbb82a2508cf5d4ef2eee8b9b9101284ad/docs/Troubleshooting.md */
// eslint-disable-next-line react/prefer-stateless-function
export default class ResultPageContainer extends React.Component {
  getData() {
    let query = "";
    if (this.state.search) {
      query = '?query=' + this.state.search;
    }
    axios.get('/api/repository/' + query)
      .then(res => {
        const result = res.data.objects;
        const meta = res.data.meta;
        this.setState({ result, meta });
      });
  }

  constructor(props) {
    super(props);
    this.state = {
      technologies: [],
      result: [],
      meta: {},
      search: window.location.pathname.replace('/repo/', ''),
    };

    axios.get('/api/technology/?order_by=-repo_count')
      .then(res => {
        const technologies = res.data.objects;
        this.setState({ technologies });
      });

  }

  componentDidMount() {
    this.getData()
  }

  render() {

    return (
      <div>
        <div className="row">
          <div className="col-3 pl-0">
            <input type="text" className="form-control input-lg search-repositories" id="search" defaultValue={this.state.search} onKeyPress={this._handleKeyPress.bind(this)} onChange={(e) => {this.setState({search: e.target.value})}}/>
          </div>
          <div className="col-9 align-self-center search-desc">
            <div className="desc-item">
              <span className="desc-name">Repositories</span>
              <span className="desc-count">{numeral(this.state.meta.total_count).format('0a')}</span>
            </div>
          </div>
        </div>
        <div className="row result-container">
          <div className="col-8">
            <div>
              <h3>{this.state.meta.total_count} repository {Pluralize("result", this.state.meta.total_count)}</h3>
            </div>
            {this.state.result.map((repo, i) =>
              <ResultRepository key={i} name={repo.name} url={repo.author.username} desc={repo.desc} tags={repo.tags} lastUpdated={repo.updated_at} />
            )}
          </div>
          <div className="col-4">
            <div className="card stat">
              <h2>Languages</h2>
              {this.state.technologies.map((tech, i) =>
                <div>
                  <span>{tech.name}</span>
                  <span className="count">{tech.repo_count}</span>
                </div>
              )}

            </div>
          </div>
        </div>
      </div>
    );
  }
  getSearchVal() {
    return window.location.pathname.replace('/repo/', '');
  }
  _handleKeyPress(e) {
    let self = this;
    console.log(this);
    if (e.key === 'Enter') {
      console.log(window.location.origin + self.state.search);
      window.history.pushState({}, null, window.location.origin + "/repo/" + self.state.search);
      self.getData();
    }
  }

}
