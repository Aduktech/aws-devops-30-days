flowchart LR
    U[Engineer] --> SSO[IAM Identity Center]
    SSO --> CLI[AWS CLI]
    CLI --> S3[(Private S3 Bucket)]

flowchart LR
    D[Developer] --> G[GitHub]
    G --> CI[GitHub Actions]
    CI --> T[Tests & Security Scans]
    D --> Docker[Docker Image]
    Docker --> K[Kind / Kubernetes]
    K --> DEP[Deployment]
    DEP --> P[FastAPI Pods]
    SVC[ClusterIP Service] --> P
    H[Helm Chart] --> K

flowchart LR
    G[Git Repository] --> TF[Terraform]
    TF --> VPC[AWS VPC]
    VPC --> S1[Public Subnet AZ-1]
    VPC --> S2[Public Subnet AZ-2]
    VPC --> IGW[Internet Gateway]
    TF --> S3[Encrypted S3 Bucket]
    TF --> STATE[(Remote Terraform State)]

flowchart LR
    C[Fictional Client] --> API[API Gateway]
    API --> L[Lambda]
    L --> D[(DynamoDB)]
    L -->|High severity| SNS[SNS]
    SNS --> E[Test Email]
    L --> CW[CloudWatch Logs]
    CW --> A[CloudWatch Alarm]
