<script lang="ts">
	// Imports
	import ThemeSwitch from "./ThemeSwitch.svelte"
	import { Github } from "lucide-svelte"
</script>

<nav>
	<div class="header">
		<img
			src="favicon.png"
			alt="Conducta logo"
			class="logo"
		/>
		<span class="title">Conducta</span>
		<div class="v-div"></div>
		<span class="docs">Docs</span>
		<ThemeSwitch />
	</div>
	<div class="h-div"></div>
	<div class="h-div"></div>
	<div class="footer">
		<span class="copy">&copy; {new Date().getFullYear()} Drew Worden</span>
		<a
			href="https://github.com/drew-worden/conducta"
			target="_blank"
		>
			<Github size={16} />
		</a>
	</div>
</nav>

<style>
	nav {
		border-right: 1px solid var(--border);
		display: grid;
		grid-template-rows: auto 1fr auto;
	}

	.header,
	.footer {
		padding: 20px;
		display: flex;
		align-items: center;
	}

	.logo {
		height: 16px;
		width: 16px;
		margin-right: 6px;
	}

	.title {
		font-family: var(--font-sans);
		line-height: 16px;
	}

	.v-div {
		margin-inline: 10px;
		height: 16px;
		width: 1px;
		background-color: var(--border);
	}

	.docs {
		font-family: var(--font-sans);
		font-size: 14px;
		line-height: 16px;
		color: #86888b;
		margin-right: auto;
	}

	.h-div {
		height: 1px;
		width: 100%;
		background-color: var(--border);
	}

	.copy {
		font-family: var(--font-sans);
		font-size: 14px;
		line-height: 16px;
		color: #86888b;
		margin-right: auto;
	}

	.footer {
		border-radius: 100000px;
	}
</style>
