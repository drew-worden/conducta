<script lang="ts">
	import { fly } from "svelte/transition"
	import { Moon, Sun } from "lucide-svelte"
	import { theme, toggleTheme } from "$lib/stores/ThemeStore"
</script>

<button
	class="container surface-4"
	on:click={toggleTheme}
	aria-label="Toggle theme"
>
	{#if $theme === "light"}
		<div in:fly={{ y: 10 }}>
			<Sun size="16" />
		</div>
	{:else}
		<div in:fly={{ y: -10 }}>
			<Moon size="16" />
		</div>
	{/if}
</button>

<style>
	.container {
		display: flex;
		padding: 4px;
		border-radius: 100000px;
		gap: 6px;
		box-shadow: none;
		overflow: hidden;
	}
</style>
