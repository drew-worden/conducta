<p align="center">
      <img src="https://github.com/drew-worden/conducta/blob/main/assets/logo.png?raw=true" height="96">
    <h1 align="center">Conducta</h1>
</p>

A model orchestration library for the modern AI era with a focus on excellent developer experience.

<p>
  <a aria-label="GitHub Release" href="(https://github.com/drew-worden/conducta/releases"><img alt="" src="https://img.shields.io/github/release/drew-worden/conducta?style=for-the-badge&color=grey&labelColor=black"></a>
  <a aria-label="License" href="https://github.com/drew-worden/conducta/blob/main/LICENSE"><img alt="" src="https://img.shields.io/github/license/drew-worden/conducta?style=for-the-badge&color=grey&labelColor=black"></a>
  <a aria-label="GitHub Stars" href="https://github.com/drew-worden/conducta"><img alt="" src="https://img.shields.io/github/stars/drew-worden/conducta?style=for-the-badge&color=grey&labelColor=black"></a>
  <a aria-label="PyPI Version" href="https://pypi.org/project/conducta/"><img alt="" src="https://img.shields.io/pypi/v/conducta?style=for-the-badge&color=grey&labelColor=black"></a>
  <a aria-label="PyPI Downloads" href="https://pypi.org/project/conducta/"><img alt="" src="https://img.shields.io/pypi/dm/conducta?style=for-the-badge&color=grey&labelColor=black"></a>
</p>

## What is Conducta

Conducta is an orchestration library with a focus on large generative models of the modern AI era, focusing on excellant developer experience. It handles integration with providers, loading credentials, making model calls, storing data, loading data of various formats, managing conversation context, querying vector and traditional databases, tracking usage, and so much more...

## How is Conducta Different from Tools like LangChain and LlamaIndex

Both LangChain and LlamaIndex are great tools, but their ecosystems are growing at a rapid pace, both now backed by companies that are trying to sell products. Conducta's goal is to provide a simpler, more friendly API with sensible defaults, better developer experience, all within a slimmer footprint. Conducta prides itself on its readablity, low-overhead, and making the orchestration process as simple and concise as possible. Here are some differentiating features:

- **No Dependecies**

  Conducta does not rely on any dependencies and only requires Python v12 or greater. This means that the package is significantly smaller and doesn't rely on provider developed Python packages. Conducta hooks into the provider's REST or native APIs directly.

- **Credential Loading**

  Conducta will automatically search your environment for provider credentials and let you know will sensible error messages if any are missing and how to add them.

- **Logging, Usage, & Tracibility**

  Conducta with keep you updated on every action it is performing by default with well-formatted logs and tracebacks. It also includes tracer and tracking features, that track and collect information, on token usage, network requests, errors, etc...

- **Declaritive Syntax**

  Conducta moves away from the chain-based approach and let's you explicitly declare how prompts should interact with more fine-grained control.

- **Out-of-the-Box Agents**

  Conducta provides support for AI agents and constructing agent pipelines by default. There is no need to install another package.

- **Single Package**

  Conducta is the only package you will need to install to use supported providers. Everything is baked into the library and doesn't require plugins, community extensions, etc. Everything is imported from `conducta`, simplifying the developer experience.
