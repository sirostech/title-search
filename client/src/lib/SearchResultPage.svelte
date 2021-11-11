<script>
	import { active_result } from './store';

	export let name = 'John Doe';
	export let codename = 'ruffles';

	// search_results.subscribe(() => {
	// 	result = search_results[active_result];
	// });
	const onClick = () => {
		active_result.set(-1);
	};
</script>

<div class="result-page">
	<div class="result-title">
		<div class="rp-button" on:click={onClick}>BACK</div>
		<div class="space" />
		<h2>{`${name}: ${codename}`}</h2>
		<div class="space" />
	</div>
	<div class="result-information">
		<h3>Info 1</h3>
		<p>
			Lorem ipsum dolor sit amet consectetur, adipisicing elit. Maxime molestiae velit eligendi
			exercitationem illum voluptate provident! Quis architecto blanditiis et odio voluptas unde
			dolores ab officiis, in at aspernatur quidem aperiam est accusamus non corporis quisquam? Quod
			facere, alias voluptate voluptates animi rerum. Alias corporis quam illo voluptas laboriosam
			sed.
		</p>
		<h3>Info 2</h3>
		<p>
			Lorem ipsum dolor sit amet consectetur, adipisicing elit. Maxime molestiae velit eligendi
			exercitationem illum voluptate provident! Quis architecto blanditiis et odio voluptas unde
			dolores ab officiis, in at aspernatur quidem aperiam est accusamus non corporis quisquam? Quod
			facere, alias voluptate voluptates animi rerum. Alias corporis quam illo voluptas laboriosam
			sed.
		</p>
		<h3>Info 3</h3>
		<p>
			Lorem ipsum dolor sit amet consectetur, adipisicing elit. Maxime molestiae velit eligendi
			exercitationem illum voluptate provident! Quis architecto blanditiis et odio voluptas unde
			dolores ab officiis, in at aspernatur quidem aperiam est accusamus non corporis quisquam? Quod
			facere, alias voluptate voluptates animi rerum. Alias corporis quam illo voluptas laboriosam
			sed.
		</p>
	</div>
</div>

<style>
	.result-page {
		flex-grow: 1;
		background-color: var(--mint-cream);
		height: 100%;
		display: flex;
		flex-direction: column;
	}
	.result-title {
		flex-grow: 1;
		background-color: var(--black-coral);
		border-bottom-left-radius: 0px;
		border-bottom-right-radius: 0px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		color: var(--mint-cream);
		max-height: 7%;
	}

	.result-title h2 {
		flex-grow: 3;
	}
	.space {
		flex-grow: 8;
	}
	p {
		margin: 5px;
	}

	.result-information {
		flex-grow: 5;
		padding: 10px;
	}
	.rp-button {
		color: var(--oxford-blue);
		outline: 3px solid var(--oxford-blue);
		padding: 5px;
		background-color: var(--mint-cream);
		margin-left: 10px;
	}

	.rp-button:hover {
		color: var(--aqua);
		outline-color: var(--aqua);
		cursor: pointer;
	}
</style>
