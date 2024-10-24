#!/bin/bash
echo "Deploying to Azure App Service..."
az webapp up --name your-app-name --resource-group your-resource-group --sku F1 --location your-location --plan your-app-plan
echo "Deployment complete."
