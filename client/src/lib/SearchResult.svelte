<script>
	export let name = 'PLACEHOLDER TEXT';
	export let codename = 'MORE PLACEHOLDER TEXT';
	export let value = 42;
	export let key = 0;
	import { active_result } from './store';

	const onSelection = () => {
		active_result.set(key);
	};
</script>

<li class="result" on:click={onSelection}>
	<p class="item-field">{name}</p>
	<p class="item-field">{codename}</p>
	<p class="item-field">{value}</p>
</li>

<style>
	.result {
		background-color: #ced4da;
		padding: 10px;
		margin: 1px;
		outline: none;
		max-height: 5vh;
		flex-grow: 1;
		display: flex;
		justify-content: space-evenly;
		align-items: center;
		align-content: flex-start;
	}

	.item-field {
		flex-grow: 1;
		text-align: center;
	}
	.item-field:last-child {
		text-align: right;
	}

	.item-field:first-child {
		text-align: left;
	}

	.result:hover {
		background-color: var(--mint-cream);
	}
</style>
