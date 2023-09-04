Here's a step-by-step guide on how to deploy a Neo4j cluster using Helm:

### Step 1: Add the Neo4j Helm Chart Repository

Before deploying Neo4j, you need to add the official Neo4j Helm chart repository to your Helm configuration. You can do this using the following command:

helm repo add neo4j https://neo4j.com/docs/operations-manual/current/helm/repository/

### Step 2: Update Helm Repositories

After adding the repository, update your Helm repositories to ensure you can access the Neo4j Helm chart:
helm repo update

### Step 3: Customize the Values

Create a values.yaml file or use Helm's --set flag to customize the Neo4j deployment according to your requirements. Here's an example values.yaml file with some common configurations:
neo4j:
  core:
    numberOfServers: 3
  rbac:
    enabled: true
  acceptLicenseAgreement: "yes"

his example sets the number of Neo4j core servers to 3, enables RBAC (Role-Based Access Control), and accepts the license agreement. Adjust these settings and others as needed for your cluster.

### Step 4: Deploy Neo4j

Install the Neo4j chart with your customized values using the helm install command. Be sure to specify a release name (e.g., neo4j-cluster) and the chart repository:

helm status neo4j-cluster

To upgrade the Neo4j cluster with new configurations or versions:
helm upgrade neo4j-cluster neo4j/neo4j -f updated-values.yaml

Ref: https://github.com/neo4j-contrib/neo4j-helm <br>
https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/#neo4j-admin-introduction
