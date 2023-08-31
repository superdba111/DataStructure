Step-by-Step Guide: Neo4j Monitoring with Prometheus and Grafana

Step 1: Install and Configure Neo4j

Install and configure Neo4j as you normally would.
Step 2: Set Up Prometheus

Install Docker if you haven't already.

Create a directory for Prometheus configuration: mkdir prometheus

Create a prometheus.yml configuration file in the prometheus directory with the following content:

global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'neo4j'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['<NEO4J_HOST>:<NEO4J_PORT>']

Replace <NEO4J_HOST> with the IP or hostname of your Neo4j server and <NEO4J_PORT> with the port where Neo4j's metrics are exposed (default is usually 7474).

Run Prometheus using Docker:docker run -p 9090:9090 -v /path/to/prometheus/:/etc/prometheus/ prom/prometheus

Step 3: Set Up Grafana

Install Docker if you haven't already.

Run Grafana using Docker:docker run -d -p 3000:3000 --name=grafana grafana/grafana
Access Grafana in your web browser at http://localhost:3000. Log in using the default credentials (username: admin, password: admin).

Add a Prometheus data source:

Click on the gear icon (⚙️) on the left sidebar.
Choose "Data Sources."
Click on "Add data source."
Select "Prometheus."
Configure the URL to your Prometheus server (e.g., http://localhost:9090).
Click "Save & Test."
Step 4: Import Neo4j Monitoring Dashboard

In Grafana, click on the "+" icon on the left sidebar and choose "Import."

Enter the ID of a Neo4j monitoring dashboard. You can find various Neo4j monitoring dashboards on Grafana's official website or on GitHub.

Configure the Prometheus data source you added earlier.

Click "Import."

Step 5: Monitor Neo4j with Grafana

Open the imported dashboard to start monitoring your Neo4j instance.

You'll be able to see metrics related to Neo4j's performance, queries, cache usage, and more.
