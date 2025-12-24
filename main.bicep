
resource appstoragebgget 'Microsoft.Storage/storageAccounts@2025-01-01' = {
  name: 'deletemejpaytest'
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
}


