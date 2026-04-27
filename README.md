# dagster-plus-nomad-test

Smoke-test Dagster project that deploys to the **hooli / data-env-dev**
Dagster+ deployment and is reconciled by the local Nomad agent listening
on the `testing-nomad` queue.

## What's here

- `src/dagster_plus_nomad_test/defs/hello_world.py` — three trivial assets
  that build a "hello, nomad!" string.
- `dagster_cloud.yaml` — pins this code location to the `testing-nomad`
  agent queue.
- `.github/workflows/dagster-cloud-deploy.yml` — builds the user-code
  image, pushes to GHCR, and updates the Dagster+ code location.
- `Dockerfile` — minimal user-code image (Python 3.12 + this project).

## Running locally

```sh
uv sync
uv run dagster dev
```

## Deploying

Push to `main`. The GitHub Action will:
1. Build & push `ghcr.io/<owner>/dagster-plus-nomad-test:<sha>`.
2. Tell Dagster+ to reconcile this code location with the new image.
3. The local Nomad agent (running via `~/nomad-agent-dev/docker-compose.yml`)
   picks up the change from the `testing-nomad` queue and spins up a
   Nomad job for the code server.

## Secrets

- `DAGSTER_CLOUD_API_TOKEN` — Dagster+ user/CI token with deploy
  permission on the `data-env-dev` deployment. Set via
  `gh secret set DAGSTER_CLOUD_API_TOKEN`.
