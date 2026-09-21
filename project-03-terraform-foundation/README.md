AWS Region
                        │
              ┌─────────▼─────────┐
              │        VPC        │
              │    10.0.0.0/16    │
              └─────────┬─────────┘
                        │
          ┌─────────────┴─────────────┐
          │                           │
    ┌─────▼─────┐               ┌─────▼─────┐
    │ Public    │               │ Public    │
    │ Subnet 1  │               │ Subnet 2  │
    │   AZ 1    │               │   AZ 2    │
    └─────┬─────┘               └─────┬─────┘
          │                           │
          └─────────────┬─────────────┘
                        │
                 Public Route Table
                        │
                 Internet Gateway


              S3 Artifact Bucket
                     │
          ┌──────────┼──────────┐
          │          │          │
       Private    Versioning  Encryption


              S3 State Bucket
                     │
          ┌──────────┼──────────┐
          │          │          │
       Private    Versioning   Locking

| AWS resource       | Why it exists                                   | Main cost risk                                             |
| ------------------ | ----------------------------------------------- | ---------------------------------------------------------- |
| VPC                | Network boundary for the environment            | VPC itself normally has no hourly charge                   |
| 2 public subnets   | Provide network segments across two AZs         | No direct subnet hourly charge                             |
| Internet Gateway   | Provides an internet route for public resources | Data-transfer/use costs may apply                          |
| Route table        | Controls subnet routing                         | No direct route-table hourly charge                        |
| Security group     | Controls network traffic                        | No direct security-group hourly charge                     |
| S3 artifact bucket | Stores build/application artifacts              | Storage, requests and data transfer                        |
| S3 versioning      | Preserves previous artifact versions            | Old versions consume storage                               |
| S3 encryption      | Protects stored objects                         | SSE-S3 has no separate KMS-key charge                      |
| S3 state bucket    | Stores Terraform remote state                   | S3 storage/request costs; normally very small for this lab |
