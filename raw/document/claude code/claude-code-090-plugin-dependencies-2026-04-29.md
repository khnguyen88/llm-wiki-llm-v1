<!--
url: https://code.claude.com/docs/en/plugin-dependencies
download_date: 2026-04-29
website: claude-code
webpage: plugin-dependencies
-->

# Plugin Dependencies

[Skip to main content](https://code.claude.com/docs/en/plugin-dependencies#content-area)
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)
English
Search...
⌘KAsk AI
  * [Claude Developer Platform](https://platform.claude.com/)
  * [Claude Code on the Web](https://claude.ai/code)
  * [Claude Code on the Web](https://claude.ai/code)


Search...
Navigation
Plugin distribution
Constrain plugin dependency versions
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Setup and access
  * [Administration overview](https://code.claude.com/docs/en/admin-setup)
  * [Advanced setup](https://code.claude.com/docs/en/setup)
  * [Authentication](https://code.claude.com/docs/en/authentication)
  * [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings)
  * [Auto mode](https://code.claude.com/docs/en/auto-mode-config)


##### Deployment
  * [Overview](https://code.claude.com/docs/en/third-party-integrations)
  * [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock)
  * [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai)
  * [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry)
  * [Network configuration](https://code.claude.com/docs/en/network-config)
  * [LLM gateway](https://code.claude.com/docs/en/llm-gateway)
  * [Development containers](https://code.claude.com/docs/en/devcontainer)


##### Usage and costs
  * [Monitoring](https://code.claude.com/docs/en/monitoring-usage)
  * [Costs](https://code.claude.com/docs/en/costs)
  * [Track team usage with analytics](https://code.claude.com/docs/en/analytics)


##### Plugin distribution
  * [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
  * [Plugin dependency versions](https://code.claude.com/docs/en/plugin-dependencies)


##### Security and data
  * [Security](https://code.claude.com/docs/en/security)
  * [Data usage](https://code.claude.com/docs/en/data-usage)
  * [Zero data retention](https://code.claude.com/docs/en/zero-data-retention)


##### Adoption
  * [Communications kit](https://code.claude.com/docs/en/communications-kit)
  * [Champion kit](https://code.claude.com/docs/en/champion-kit)


On this page
  * [Why constrain dependency versions](https://code.claude.com/docs/en/plugin-dependencies#why-constrain-dependency-versions)
  * [Declare a dependency with a version constraint](https://code.claude.com/docs/en/plugin-dependencies#declare-a-dependency-with-a-version-constraint)
  * [Depend on a plugin from another marketplace](https://code.claude.com/docs/en/plugin-dependencies#depend-on-a-plugin-from-another-marketplace)
  * [Tag plugin releases for version resolution](https://code.claude.com/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution)
  * [How constraints interact](https://code.claude.com/docs/en/plugin-dependencies#how-constraints-interact)
  * [Remove orphaned auto-installed dependencies](https://code.claude.com/docs/en/plugin-dependencies#remove-orphaned-auto-installed-dependencies)
  * [Resolve dependency errors](https://code.claude.com/docs/en/plugin-dependencies#resolve-dependency-errors)
  * [See also](https://code.claude.com/docs/en/plugin-dependencies#see-also)


Plugin distribution
# Constrain plugin dependency versions
Copy page
Declare version constraints on plugin dependencies so your plugin keeps working when an upstream plugin ships a breaking change.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
A plugin can depend on other plugins by listing them in `plugin.json` or in its marketplace entry. By default, a dependency tracks the latest available version, so an upstream release can change the dependency under your plugin without warning. Version constraints let you hold a dependency at a tested version range until you choose to move. When you install a plugin that declares dependencies, Claude Code resolves and installs them automatically and lists which dependencies were added at the end of the install output. If a dependency later goes missing, `/reload-plugins` and the background plugin auto-update reinstall it, provided its marketplace is already in your configured marketplaces. Re-running `claude plugin install` on the dependent plugin, or adding a marketplace with `claude plugin marketplace add`, also resolves any outstanding missing dependencies. Dependencies from a marketplace you have not added are left unresolved. This guide is for plugin authors who declare dependencies in `plugin.json` and for marketplace maintainers who tag releases. To install plugins that have dependencies, see [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins). For the full manifest schema, see the [Plugins reference](https://code.claude.com/docs/en/plugins-reference).
Dependency version constraints require Claude Code v2.1.110 or later.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#why-constrain-dependency-versions)
Why constrain dependency versions
Consider an internal marketplace where two teams publish plugins. The platform team maintains `secrets-vault`, an MCP server that wraps a secrets backend. The deploy team maintains `deploy-kit`, which calls `secrets-vault` to fetch credentials during deploys. `deploy-kit` is tested against `secrets-vault` v2.1.0. Without a version constraint, the next time the platform team tags a release that renames an MCP tool, auto-update moves every engineer’s `secrets-vault` to the new version and `deploy-kit` breaks. With a version constraint, `deploy-kit` declares that it needs `secrets-vault` in the `~2.1.0` range. Engineers with `deploy-kit` installed stay on the highest matching `2.1.x` patch. The deploy team upgrades on their own schedule by publishing a new `deploy-kit` version with a wider constraint.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#declare-a-dependency-with-a-version-constraint)
Declare a dependency with a version constraint
List dependencies in the `dependencies` array of your plugin’s `.claude-plugin/plugin.json`. Each entry is either a plugin name or an object with a version constraint. The following manifest declares one unversioned dependency and one constrained dependency:
.claude-plugin/plugin.json

```
{
  "name": "deploy-kit",
  "version": "3.1.0",
  "dependencies": [
    "audit-logger",
    { "name": "secrets-vault", "version": "~2.1.0" }
  ]
}

```

An entry can be a bare string with only the plugin name, like `"audit-logger"` in the example above, which depends on whatever version that plugin’s marketplace provides. For more control, use an object with these fields:  
| Field  | Type  | Description  |  
| --- | --- | --- |  
| `name`  | string  | Plugin name. Resolves within the same marketplace as the declaring plugin. Required.  |  
| `version`  | string  | A [semver range](https://github.com/npm/node-semver#ranges) such as `~2.1.0`, `^2.0`, `>=1.4`, or `=2.1.0`. The dependency is fetched at the highest tagged version that satisfies this range.  |  
| `marketplace`  | string  | A different marketplace to resolve `name` in. Cross-marketplace dependencies are blocked unless the target marketplace is listed in [`allowCrossMarketplaceDependenciesOn`](https://code.claude.com/docs/en/plugin-dependencies#depend-on-a-plugin-from-another-marketplace) in the root marketplace’s `marketplace.json`.  |  
The `version` field accepts any expression supported by Node’s `semver` package, including caret, tilde, hyphen, and comparator ranges. Pre-release versions such as `2.0.0-beta.1` are excluded unless your range opts in with a pre-release suffix like `^2.0.0-0`.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#depend-on-a-plugin-from-another-marketplace)
Depend on a plugin from another marketplace
By default, Claude Code refuses to auto-install a dependency that lives in a different marketplace than the plugin declaring it. This prevents one marketplace from silently pulling in plugins from a source you have not reviewed. To allow it, the maintainer of the root marketplace adds the target marketplace name to `allowCrossMarketplaceDependenciesOn` in `marketplace.json`. The root marketplace is the one that hosts the plugin the user is installing; only its allowlist is consulted, so trust does not chain through intermediate marketplaces. The following `marketplace.json` allows `deploy-kit` to depend on a plugin from `acme-shared`:
.claude-plugin/marketplace.json

```
{
  "name": "acme-tools",
  "owner": { "name": "Acme" },
  "allowCrossMarketplaceDependenciesOn": ["acme-shared"],
  "plugins": [
    {
      "name": "deploy-kit",
      "source": "./deploy-kit",
      "dependencies": [
        { "name": "audit-logger", "marketplace": "acme-shared" }
      ]
    }
  ]
}

```

If the field is missing or does not include the target marketplace, install fails with a `cross-marketplace` error naming the field to set. Users can still install the dependency manually first, which satisfies the constraint without changing the allowlist.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution)
Tag plugin releases for version resolution
Version constraints resolve against git tags on the marketplace repository. For Claude Code to find a dependency’s available versions, the upstream plugin’s releases must be tagged using a specific naming convention. Tag each release as `{plugin-name}--v{version}`, where `{version}` matches the `version` field in that commit’s `plugin.json`. From the plugin directory, run:

```
claude plugin tag --push

```

The `claude plugin tag` command derives the tag name from the plugin’s manifest and the enclosing marketplace entry. Before creating the tag, it validates the plugin contents, checks that `plugin.json` and the marketplace entry agree on the version, requires a clean working tree under the plugin directory, and refuses if the tag already exists. Add `--dry-run` to see what would be tagged without creating it. Running `git tag secrets-vault--v2.1.0` directly is equivalent if you keep `plugin.json` and the marketplace entry in sync yourself. The plugin name prefix lets one marketplace repository host multiple plugins with independent version lines. The `--v` separator is parsed as a prefix match on the full plugin name, so plugin names that contain hyphens are handled correctly. When you install a plugin that declares `{ "name": "secrets-vault", "version": "~2.1.0" }`, Claude Code lists the marketplace’s tags, filters to those starting with `secrets-vault--v`, and fetches the highest version satisfying `~2.1.0`. If no matching tag exists, the dependent plugin is disabled with an error listing the available versions. The resolved tag’s semver is recorded separately from `plugin.json`’s `version`, so constraint checks use the tag that was actually fetched even if `plugin.json` at that commit has a stale value. The cache directory name for a tag-resolved install includes a 12-character commit-SHA suffix, so if a maintainer force-moves a tag to a different commit, the next install gets a fresh cache directory instead of reusing stale content.
For `npm` marketplace sources, the constraint does not control which version is fetched, since tag-based resolution applies only to git-backed sources. The constraint is still checked at load time, and the dependent plugin is disabled with `dependency-version-unsatisfied` if the installed version does not satisfy it.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#how-constraints-interact)
How constraints interact
When several installed plugins constrain the same dependency, Claude Code intersects their ranges and resolves the dependency to the highest version that satisfies all of them. The table below shows how common combinations resolve.  
| Plugin A requires  | Plugin B requires  | Result  |  
| --- | --- | --- |  
| `^2.0`  | `>=2.1`  | One install at the highest `2.x` tag at or above `2.1.0`. Both plugins load.  |  
| `~2.1`  | `~3.0`  | Install of plugin B fails with `range-conflict`. Plugin A and the dependency stay as they were.  |  
| `=2.1.0`  | none  | The dependency stays at `2.1.0`. Auto-update skips newer versions while plugin A is installed.  |  
Auto-update fetches a constrained dependency at the highest git tag that satisfies every installed plugin’s range, rather than at the marketplace’s latest version, so the dependency continues to receive updates within its allowed range. If no tag satisfies all ranges, the update is skipped and the skip appears in `/doctor` and the `/plugin` Errors tab, naming the constraining plugin. When you uninstall the last plugin that constrains a dependency, the dependency is no longer held and resumes tracking its marketplace entry on the next update.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#remove-orphaned-auto-installed-dependencies)
Remove orphaned auto-installed dependencies
Auto-installed dependencies stay on disk after the plugins that installed them are uninstalled, in case you reinstall a dependent plugin or want to keep using the dependency directly. To clean them up, run `claude plugin prune` to list the auto-installed dependencies that no longer have any installed plugin requiring them and remove them after a confirmation prompt. This requires Claude Code v2.1.121 or later.

```
claude plugin prune

```

By default, prune operates at user scope. Use `--scope project` or `--scope local` to target a different scope. Pass `--dry-run` to list what would be removed without changing anything. Pass `-y` to skip the confirmation prompt. When stdin or stdout is not a terminal, prune lists the orphans and exits without removing them unless `-y` is passed. To prune as part of an uninstall, pass `--prune` to `claude plugin uninstall`. After removing the named plugin, Claude Code scans for and removes any auto-installed dependencies that are now orphaned. Plugins you installed yourself are never pruned, only those installed automatically through another plugin’s `dependencies` array. For example, to uninstall `deploy-kit` and clean up the dependencies it leaves behind:

```
claude plugin uninstall deploy-kit --prune

```

## 
[​](https://code.claude.com/docs/en/plugin-dependencies#resolve-dependency-errors)
Resolve dependency errors
Dependency problems surface in `claude plugin list`, in the `/plugin` interface, and in `/doctor`. The affected plugin is disabled until you resolve the error. The most common errors and their fixes are listed below.  
| Error  | Meaning  | How to resolve  |  
| --- | --- | --- |  
| `dependency-unsatisfied`  | A declared dependency is not installed, or it is installed but disabled.  | Run the `claude plugin install` command shown in the error message. If the dependency’s marketplace is not yet configured, add it with `claude plugin marketplace add` and Claude Code resolves the dependency automatically. If the dependency is disabled, enable it.  |  
| `range-conflict`  | The version requirements for a dependency cannot be combined. The error message names the cause: no version satisfies all of the ranges, a range is not valid semver syntax, or the combined ranges are too complex to intersect.  | Uninstall or update one of the conflicting plugins, fix any invalid `version` string, simplify long `||` chains, or ask the upstream author to widen its constraint.  |  
| `dependency-version-unsatisfied`  | The installed dependency’s version is outside this plugin’s declared range.  | Run `claude plugin install <dependency>@<marketplace>` to re-resolve the dependency against all current constraints.  |  
| `no-matching-tag`  | The dependency’s repository has no `{name}--v*` tag satisfying the range.  | Check that the upstream has tagged releases using the convention above, or relax your range.  |  
To check for these errors programmatically, run `claude plugin list --json` and read the `errors` field on each plugin.
## 
[​](https://code.claude.com/docs/en/plugin-dependencies#see-also)
See also
  * [Create plugins](https://code.claude.com/docs/en/plugins): build plugins with skills, agents, and hooks
  * [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces): host plugins for your team
  * [Plugins reference](https://code.claude.com/docs/en/plugins-reference#plugin-manifest-schema): the full `plugin.json` schema
  * [Version management](https://code.claude.com/docs/en/plugins-reference#version-management): how a plugin’s own version is resolved and used as the cache key


Was this page helpful?
YesNo
[Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)[Security](https://code.claude.com/docs/en/security)
⌘I
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
Company
[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)
Help and security
[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)
Learn
[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)
Terms and policies
[Privacy choices](https://code.claude.com/docs/en/plugin-dependencies)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
