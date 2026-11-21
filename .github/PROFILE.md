# Profile updates

`Update profile` regenerates `github-metrics.svg` with
[lowlighter/metrics](https://github.com/lowlighter/metrics) and commits it.
`README.md` embeds that image. It runs daily at 06:23 UTC and on demand from Actions.

It needs the repository secret `METRICS_TOKEN`: a classic personal access token
with no scopes. See https://github.com/lowlighter/metrics/blob/master/.github/readme/partials/documentation/setup/action.md.
GitHub stats do not include private Forgejo activity.
