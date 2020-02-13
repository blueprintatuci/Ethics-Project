import React, { Component } from "react";
import bpData from "./bpData";
import "./Homepage.css";

import axios from 'axios';

export default class Homepage extends React.Component {
  render() {
    return (
      <div className="Homepage-content">
        <NavBar />
        <Context />
        <BodyContent />
        <ApiTest />
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

export class ApiTest extends Component {
    state = {
      error: null,
      isLoaded: false,
      items: []
    };
  
    componentDidMount() {
      axios.get("https://ethic-blueprint.herokuapp.com/").then(
        result => {
          this.setState({
            isLoaded: true,
            items: result.data
          });
        },
        error => {
          this.setState({
            isLoaded: true,
            error
          });
        }
        );
    }
  
    render() {
      const { error, isLoaded, items } = this.state;
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
          <div className = "usernames">
            {/* {items.map(item => (
              <div key={item.username}>
                {item.username}: {item.name}
              </div>
            ))} */}
            <div>{items}</div>
          </div>
        );
      }
    }
}

class BodyContent extends Component {
  render() {
    const bodyComponents = bpData.map(data => (
      <BodyComponent
        key={data.id}
        title={data.title}
        img={data.img}
        context={data.context}
        url={data.url}
        author={data.author}
      />
    ));
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
        <div className="description">{this.props.context}</div>
        <button className="visit-article" onClick={() => window.open(this.props.url)}>Visit Article</button>
        <button className="add" onClick={() => window.open(this.props.url)} style={{ marginTop: 10 }}>
          Add To Blog
        </button>
      </div>
    );
  }
}

