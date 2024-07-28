// Imports
import adapter from "@sveltejs/adapter-vercel"
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte"
import { mdsvex, escapeSvelte } from "mdsvex"
import { createHighlighter } from "shiki"

// Svelte configuration
const svelteConfig = {
	extensions: [".svelte", ".svx", ".md"],
	preprocess: [
		vitePreprocess(),
		mdsvex({
			extensions: [".md", ".svx"],
			highlight: {
				highlighter: async (code, lang = "text") => {
					const highlighter = await createHighlighter({
						themes: ["dark-plus"],
						langs: ["javascript", "typescript", "python"]
					})
					await highlighter.loadLanguage("javascript", "typescript", "python")
					const html = escapeSvelte(
						highlighter.codeToHtml(code, { lang, theme: "dark-plus" })
					)
					return `{@html \`${html}\` }`
				}
			}
		})
	],
	kit: {
		adapter: adapter()
	}
}

// Exports
export default svelteConfig
