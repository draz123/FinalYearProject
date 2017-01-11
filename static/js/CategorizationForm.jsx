import React from 'react';

class CategorizationForm extends React.Component {
	render() {
		return (
			<form method="post" action={this.props.url}>
				<div className="form-group">
					<label>
						Tweet's ID:
						<input name="tweetID" type="text" className="form-control" placeholder="..." />
					</label>
					<br></br>
					<label>
					Categorization method: <br></br>
                        <input type="radio" name="categorizationMethod" value="R" style={{marginLeft: 1 + 'em'}} checked/> Random
                        <input type="radio" name="categorizationMethod" value="KW" style={{marginLeft: 1 + 'em'}}/> Key words
                        <input type="radio" name="categorizationMethod" value="NB" style={{marginLeft: 1 + 'em'}}/> Naive bayes classifier
                        <input type="radio" name="categorizationMethod" value="SGD" style={{marginLeft: 1 + 'em'}}/> Stochastic gradient descent classifier
                        <input type="radio" name="categorizationMethod" value="NC" style={{marginLeft: 1 + 'em'}}/> Nearest Centroid classifier
                        <input type="radio" name="categorizationMethod" value="MLP" style={{marginLeft: 1 + 'em'}}/> Multilayer perception classifier
					</label>
				</div>
				<div className="text-right">
					<button type="reset" className="btn btn-default">Reset</button>
					<button type="submit" className="btn btn-primary">Categorize</button>
				</div>
			</form>
		);
	}
}

export default CategorizationForm;