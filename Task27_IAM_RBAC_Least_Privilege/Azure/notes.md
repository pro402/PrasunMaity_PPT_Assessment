# Azure RBAC — Notes

## Users
| User | UPN | Role |
|------|-----|------|
| Prasun Maity | prasunm2003@outlook.com | Owner |
| Developer | developer@prasunm2003outlook.onmicrosoft.com | Reader (RG) + Contributor (VM) |

## Role Assignments
| Scope | Role | Effect |
|-------|------|--------|
| `task3-rg` (Resource Group) | Reader | View all resources — no modify/delete |
| `task3-rg-vm` (VM only) | Contributor | Full control on that VM only |

## Test Results
| Action | User | Result |
|--------|------|--------|
| View resources in `task3-rg` | Developer | ✅ Allowed — Reader |
| Create VM in `task3-rg` | Developer | ✅ Allowed — Contributor on VM |
| Delete VM `task3-rg-vm` | Developer | ❌ Denied — no delete under Reader |

## Error Observed
The client 'developer@prasunm2003outlook.onmicrosoft.com'
with object id '9ee92ccb...' does not have authorization
to perform action 'Microsoft.Compute/virtualMachines/delete'

## Key Takeaway
- Azure RBAC is **scope-based** — Reader at RG sets the default, Contributor at VM elevates only that resource
- Contributor does **not** grant delete at RG level — Owner role is required for that
- Always assign roles at the **narrowest possible scope** for least privilege
