# Invitation issue

Local reproduction confirmed expired invitations still work because expiry is compared against created_at, not the current time. Diagnosis is complete. No fix is authorized and no TDD policy is selected. A fix would need to reject expired invitations while preserving accepted accounts.
