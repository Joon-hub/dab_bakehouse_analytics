# Dab Bakehouse Analytics (Tutorial Demo)

> **Note**: This repository is a step-by-step implementation of the tutorial **"Data Engineering From Data to Dashboards with DABs: Crunching the Cookies Dataset"**.

## 🎓 About This Project
This project is a hands-on demo replicating the workflow presented in the [Databricks YouTube tutorial](https://www.youtube.com/watch?v=kmxfxC7JwQQ). It demonstrates how to build **production-ready data applications** using **Databricks Asset Bundles (DABs)**.

The tutorial focuses on the **Bakehouse Analytics** solution, utilizing the **Cookies dataset** from the Data+AI Summit 2024 Marketplace to create a real-time analytics system.

## 🚀 Key Features Implemented
- **Streaming Data Pipelines**: Built using **Delta Live Tables (DLT)**.
- **Real-Time Analytics**: Optimizing retail location strategies with live data streams.
- **Generative AI Integration**: Leveraging AI for deeper insights into retail data.
- **CI/CD Practices**: Automated deployment workflows using **Databricks Asset Bundles** and **GitHub Actions**.
- **VS Code Integration**: Seamless development environment setup.

## 📺 Source Material
- **Video Title**: Data Engineering From Data to Dashboards with DABs: Crunching the Cookies Dataset
- **Provider**: Databricks
- **Link**: [Watch the Tutorial on YouTube](https://www.youtube.com/watch?v=kmxfxC7JwQQ)
- **Dataset**: Cookies dataset (available on the Databricks Marketplace) [1]

## 📂 Project Structure
```text
dab_bakehouse_analytics/
├── bakehouse_analytics/      # Main analysis directory containing DLT pipelines
│   ├── nyc_taxi_analysis.ipynb # (Optional/Placeholder) Initial analysis file
│   └── ... DAB configuration files ...
├── .github/                  # GitHub Actions workflows for CI/CD
├── databricks.yml            # Databricks Asset Bundle configuration
└── README.md