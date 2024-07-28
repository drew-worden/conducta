<script lang="ts">
	// Imports
	import Nav from "$lib/components/Nav.svelte"
	import "open-props/style"
	import "open-props/normalize"
	import "open-props/buttons"
	import "$lib/styles/global.css"

	// Prerender
	export const prerender = true
</script>

<div class="layout">
	<Nav />
	<main>
		<slot />
	</main>
</div>

<style>
	.layout {
		width: 100%;
		display: grid;
		grid-template-columns: 279px auto;
		height: 100%;
	}

	main {
		padding: 64px;
	}
</style>
