# azurecloudresume


To create a service principle, run the Azure CLI command below. Note that an error occurred and I needed to set the MSYS_NO_PATHCONV=1 environmental variable before the cli command.  

```bash
MSYS_NO_PATHCONV=1 az ad sp create-for-rbac --name azurecloudresume --role contributor --scopes /subscriptions/7e3199f3-4a4e-4c82-88a9-89e0e6e14868/resourceGroups/front_end --sdk-auth
```
