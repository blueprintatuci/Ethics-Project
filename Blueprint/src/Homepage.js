import React, {Component} from "react";
import bpData from "./bpData";

export default class Homepage extends React.Component {
    render() {
        // const bodyContentComponents = 
        return (
            <div className="Homepage-content">
                <Context/>
                <BodyContent/>
            </div>
        )
    }
}

class Context extends Component {
    render() {
        return (
            <div className="context-content">
                <h1>
                    This is a CTA heading.
                </h1>
                <p>
                    This section uses a container element to ensure the content looks right on every device. It’s centered with the class "Centered Container.”
                </p>
                <button>
                    Button Text
                </button>
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
            <div className="body-component">
                <div>
                    {this.props.title}
                </div>
                <img src={this.props.img}/>
                <div>
                    {this.props.context}
                </div>
                <button style={{marginTop: 10}}>Button Text</button>
            </div>
        )
    }
}