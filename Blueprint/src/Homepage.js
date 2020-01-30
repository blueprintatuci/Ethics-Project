import React, {Component} from "react";
import bpData from "./bpData";
import './Homepage.css';

export default class Homepage extends React.Component {
    render() {
        // const bodyContentComponents = 
        return (
            <div className="Homepage-content">
                <NavBar/>
                <Context/>
                <BodyContent/>
            </div>
        )
    }
}

class NavBar extends Component {
    render() {
        return (
            <ul className = "nav">
                <li><a class="active" href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        )
    }
}

class Context extends Component {
    render() {
        return (
            <div className="banner-container">
                <div className = "banner-content">
                    <h1>Post Picker</h1>
                    <a href="#" id="visit">Visit</a>
                </div>
            </div>
        )
    }
}

class BodyContent extends Component {
    render() {
        const bodyComponents = bpData.map(data => <BodyComponent key={data.id} title={data.title} img={data.img} context={data.context}/>)
        return (
            <div className="body-content">
                {bodyComponents}
            </div>
        )
    }
}

class BodyComponent extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="article-list">
                <div className="title">
                    {this.props.title}
                </div>
                <img className = "article-img" src={this.props.img}/>
                <div className = "description">
                    {this.props.context}
                </div>
                <button className = "visit-article" >Visit Article</button>
                <button className = "add" style={{marginTop: 10}}>Add To Blog</button>
            </div>
        )
    }
}