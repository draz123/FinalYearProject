import React from 'react';
import ResultsList from './ResultsList.jsx';
import CategorizationForm from './CategorizationForm.jsx';


class CategorizationBox extends React.Component {
	render() {
		return (
			<div>
				<CategorizationForm url={this.props.url} />
				<ResultsList results={this.props.results} />
			</div>
		);
	}
}

export default CategorizationBox;