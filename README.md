# Infrastructure Drift Detector

Infrastructure drift detection: compare actual vs declared state with auto-remediation.

## Supported Providers
- AWS (CloudFormation, IAM)
- GCP (Deployment Manager)
- Azure (ARM templates)
- Kubernetes (kubectl diff)

## Workflow
1. Read Terraform state or CloudFormation templates
2. Query actual cloud resources via API
3. Diff and report discrepancies
4. Auto-remediate or alert

## License: MIT
