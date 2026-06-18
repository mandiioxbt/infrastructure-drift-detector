# Infrastructure Drift Detector

Infrastructure drift detection: compare actual vs declared state.

## How It Works
1. Read Terraform state / CloudFormation templates
2. Query actual cloud resources via API
3. Diff and report discrepancies
4. Auto-remediate or alert

## Supported Providers
AWS, GCP, Azure, Kubernetes

## License
MIT
