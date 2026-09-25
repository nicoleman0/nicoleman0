# Profile updates

`Update profile` refreshes all public merged PRs authored by `nicoleman0`, excluding
repositories owned by that account. It paginates the full PR connection rather
than using GitHub search's result limit. A failed fetch leaves the README untouched.

For Metrics, add a classic personal access token with no scopes as the repository
secret `METRICS_TOKEN`. The workflow uses its separate `GITHUB_TOKEN` to commit.
See https://github.com/lowlighter/metrics/blob/master/.github/readme/partials/documentation/setup/action.md.

After merging, run `Update profile` from Actions. It also runs daily at 06:23 UTC.
The Metrics image is embedded only after it has been generated successfully.
The notable-contributions panel can include opened PRs; the Markdown list counts
only merged PRs. GitHub stats do not include private Forgejo activity.

To refresh the contribution list locally with an authenticated GitHub CLI:

```sh
python3 scripts/update_contributions.py
```
