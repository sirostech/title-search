<script>
	import axios from 'axios';
	import { search_results } from './store';
	const onInputChange = async (event) => {
		// console.log(event.target.value);
		if (event.target.value === '') {
			search_results.set([]);
		} else {
			const response = await axios.get(`http://localhost:5000/search?name=${event.target.value}`);
			// console.log(response.data);
			search_results.set(response.data);
		}
	};
</script>

<div class="searchbar" on:input={onInputChange}>
	<input class="inp" type="text" placeholder="title search" />
</div>

<style>
	*:focus {
		outline: none;
		border: none;
		text-decoration: none;
	}

	.searchbar {
		flex-grow: 0.5;
		margin: 10px;
		/* margin-top: 0; */
		background-color: #ced4da;
		padding: 5px;
		display: flex;
		max-height: 4vh;
		min-height: 4vh;
	}

	.searchbar:active {
		background-color: var(--mint-cream);
		transition: background-color 150ms ease-out;
	}
	::placeholder {
		color: var(--black-coral);
		font-size: inherit;
	}
	.inp {
		border: none;
		outline: none;
		flex-grow: 5;
		background-color: var(--oxford-blue);
		padding-left: 10px;
		font-size: 1.25em;
		color: #ced4da;
	}
	.btn {
		flex-grow: 1;
		border: none;
		outline: none;
		background-color: #ced4da;
		margin: 5px;
		margin-left: 10px;
		font-size: 1em;
	}

	.btn:hover {
		outline: 5px solid var(--aqua);
		color: var(--aqua);

		background-color: var(--mint-cream);
	}

	.btn:active {
		background-color: var(--black-coral);
	}
</style>
