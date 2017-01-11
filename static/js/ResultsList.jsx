import React from 'react';
import Result from './Result.jsx';

class ResultsList extends React.Component {
	render() {
		if (!this.props.results.length) {
			return null;
		}
		var resultsNodes = this.props.results.map((results, index) => {
			return <Result tweetID={results.tweetID} text={results.text} key={index} />;
		});
		return (
			<div>
				<h2>Results:</h2>
				{resultsNodes}
			</div>
		);
	}
}

export default ResultsList;