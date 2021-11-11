<main class="main">
	<slot />
</main>

<style>
	:root {
		--aqua: #38fffcff;
		--mint-cream: #f4fffdff;
		--oxford-blue: #011936ff;
		--black-coral: #465362ff;
	}

	.main {
		width: 100vw;
		height: 100vh;
		background-color: var(--oxford-blue);
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		border-radius: 0px;
	}
</style>
