# Accelerator catalog

A teammate starts in the accelerator repository. This catalog is the lookup for which shared workflow that repository will use.

Only rows with a config file have a running pipeline. The other rows are the assigned workflow. Their `config.yml` is added when that repository is ready to build. Runtime stays blank until the repository is opened and the language is confirmed.

| Accelerator | Workflow | Runtime | Config |
| --- | --- | --- | --- |
| jktech-api-framework-python | library | Python 3.12 | [config.yml](accelerators/jktech-api-framework-python/config.yml) |
| jktech-api-framework | library | .NET 8 | Not created yet |
| jktech-microservice-starter-kit | library | | Not created yet |
| jktech-logging-framework | library | | Not created yet |
| jktech-config-management | library | | Not created yet |
| jktech-scheduler-framework | library | | Not created yet |
| jktech-distributed-cache | library | | Not created yet |
| jktech-service-health-checks | library | | Not created yet |
| jktech-feature-flag-framework | library | | Not created yet |
| jktech-workflow-engine | library | | Not created yet |
| jktech-integration-adapter-framework | library | | Not created yet |
| jktech-multi-tenant-framework | library | | Not created yet |
| jktech-rate-limiting-middleware | library | | Not created yet |
| jktech-session-management | library | | Not created yet |
| jktech-plugin-architecture-framework | library | | Not created yet |
| jktech-integration-event-framework | library | | Not created yet |
| jktech-message-queue-framework | library | | Not created yet |
| jktech-object-storage-connector | library | | Not created yet |
| jktech-enterprise-chatbot-framework | library | | Not created yet |
| jktech-genai-guardrails | library | | Not created yet |
| jktech-model-routing | library | | Not created yet |
| jktech-agent-orchestration | library | | Not created yet |
| jktech-llm-gateway | service | | Not created yet |
| jktech-email-assistant | service | | Not created yet |
| jktech-ticket-routing-ai | service | | Not created yet |
| jktech-ai-decision-engine | service | | Not created yet |
| jktech-notification-service | service | | Not created yet |
| jktech-file-upload-service | service | | Not created yet |
| jktech-data-export-service | service | | Not created yet |
| jktech-configuration-sync-service | service | | Not created yet |
| jktech-search-platform | service | | Not created yet |
| jktech-ad-integration-platform | service | | Not created yet |
| jktech-ui-component-library | web | | Not created yet |
| jktech-observability-dashboard | web | | Not created yet |
| jktech-etl-processing-framework | data-pipeline | | Not created yet |
| jktech-document-processing | data-pipeline | | Not created yet |
| jktech-data-ingestion-pipeline | data-pipeline | | Not created yet |
| jktech-data-quality-framework | data-pipeline | | Not created yet |
| jktech-data-pipeline-monitoring | data-pipeline | | Not created yet |
| jktech-databricks-job-orchestration | data-pipeline | | Not created yet |
| jktech-code-quality-scanner | tool | | Not created yet |
| jktech-api-documentation-generator | tool | | Not created yet |
| jktech-release-automation | tool | | Not created yet |
| jktech-ci-cd-pipeline-template | none | | Documents pipeline choice. Workflows stay in this repo. |
| jktech-accelerators-deploy | none | | This repository. |

## What each workflow means

| Workflow | What the teammate gets |
| --- | --- |
| library | Lint and test. No container build. |
| service | Library steps, plus an image build. |
| web | Install, lint, test, and a frontend build. |
| data-pipeline | Lint and test the job. No API host. |
| tool | Lint and test a small CLI. |
| none | No product pipeline. |
