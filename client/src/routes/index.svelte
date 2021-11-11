<script>
	import SearchBar from '../lib/SearchBar.svelte';
	import SearchResults from '../lib/SearchResults.svelte';
</script>

<div class="content">
	<h1 class="title">Title Search</h1>
	<SearchBar />
	<SearchResults />
</div>

<style>
	*:focus {
		outline: none;
		border: none;
		text-decoration: none;
	}
	.content {
		min-height: 70vh;
		min-width: 60vw;
		max-width: 60vw;
		display: flex;
		flex-direction: column;
	}

	.title {
		text-align: center;
		color: #ced4da;
	}
</style>
