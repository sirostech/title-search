<script>
	import { search_results } from '../lib/store';
	import { active_result } from '../lib/store';
	let sr_value;
	let a_value;

	search_results.subscribe((value) => {
		sr_value = value;
	});

	active_result.subscribe((value) => {
		a_value = value;
	});
	import SearchResultPage from './SearchResultPage.svelte';
	import SearchResult from './SearchResult.svelte';
</script>

<div class="searchresults">
	<div class="inner">
		{#if a_value >= 0}
			<SearchResultPage {...sr_value[a_value]} />
		{:else}
			<ul class="results">
				{#each sr_value as result, idx}
					<SearchResult {...result} key={idx} />
				{/each}
			</ul>
		{/if}
	</div>
</div>

<style>
	.searchresults {
		flex-grow: 8;
		margin: 10px;
		margin-top: 0;
		background-color: #ced4da;
		padding: 5px;
		display: flex;
	}

	.inner {
		background-color: var(--oxford-blue);
		flex-grow: 1;
		padding: 3px;
	}

	.results {
		list-style-type: none;
		outline: none;
		display: flex;
		flex-direction: column;
	}
</style>
