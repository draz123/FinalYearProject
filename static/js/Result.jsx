import React from 'react';

class Result extends React.Component {
	render() {
		return (
			<div>
				<h3>{this.props.tweetID}</h3>
				{this.props.text}
			</div>
		);
	}
}

export default Result;