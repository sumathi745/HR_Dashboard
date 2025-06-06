# API Endpoints Used in Project

# 1. Create Dashboard

### /POST/v1/dashboards/create

Example Body:

```json

{
  "dashboard_title": "test", 
  "owner_id": "123",          
  "metrics": {
    "headcount": 50,          
    "payrollCost": 1700000.52,  
    "overtimeHours": 90        
  }
}


Example Response 200:


{
    "created_at": "Fri, 05 Jun 2025 02:18:48 GMT",
    "id": 3,
    "metrics": {
        "headcount": 50,
        "overtimeHours": 90,
        "payrollCost": 1700000.52
    },
    "owner_id": "123",
    "title": "test"
}

# 2. View Dashboard

### /GET/v1/dashboards/{dashboard_id}


Example Response 200:


{
  "dashboard_title": "test",
  "owner_id": "123",
  "metrics": {
    "headcount": 50,
    "payrollCost": 1700000.52,
    "overtimeHours": 90
  }
}


# 3. Share Dashboard

### /POST/v1/dashboards/{dashboard_id}/share

Example Body:


{
  "managerIds": ["1","2","3"]
}

Example Response 200:


{
    "message": "Dashboard 3 is now shared successfully",
    "shared_with": "Manager Ids: ['1', '2', '3']"
}



