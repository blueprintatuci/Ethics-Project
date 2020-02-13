import React, { Component } from "react";
import "./Homepage.css";

import axios from 'axios';

export default class Homepage extends React.Component {
  render() {
    return (
      <div className="Homepage-content">
        <NavBar />
        <Context />
        <BodyContent />
        {/* <ApiTest /> */}
      </div>
    );
  }
}

class NavBar extends Component {
  render() {
    return (
      <ul className="nav">
        <li>
          <a className="active" href="#home">
            Home
          </a>
        </li>
        <li>
          <a href="#about">About</a>
        </li>
      </ul>
    );
  }
}

class Context extends Component {
  render() {
    return (
      <div className="banner-container">
        <div className="banner-content">
          <h1>Post Picker</h1>
          <a href="#" id="visit">
            Visit
          </a>
        </div>
      </div>
    );
  }
}


class BodyContent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      data: [""]
    }
  }

  componentDidMount() {
    axios.get('http://ethic-blueprint.herokuapp.com/articles')
    .then (result => this.setState(() => ({data: result.data['articles']})))
    .catch(error => console.log(error))
  }

  render() {
    
    const bodyComponents = this.state.data.map((d, id) => {return(
    <BodyComponent
      key={id}
      title={d.title}
      img={d.image_url}
      content={d.content}
      url={d.image_url}
      author={d.author}
      publish_date={d.publish_date}
    />)})

    return (
        <div className="body-content">
            {bodyComponents}
        </div>
    );
  }
}

class BodyComponent extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    console.log(this.props.url)
    return (
      <div className="article-list">
        <div className="title">{this.props.title}</div>
        <div className="author">{this.props.author}</div>
        <img className="article-img" src={this.props.img} />
        <div className="description">{this.props.content}</div>
        <button className="visit-article" onClick={() => window.open(this.props.url)}>Visit Article</button>
        <button className="add" onClick={() => window.open(this.props.url)} style={{ marginTop: 10 }}>
          Add To Blog
        </button>
      </div>
    );
  }
}

