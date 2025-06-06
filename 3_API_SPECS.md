# API Endpoints Used in Project

1. Create Dashboard

Will first validate request fields, then generate a unique dashboard ID, store dashboard in DB, and return JSON with dashboard ID info.

# /POST/v1/dashboards/create

Body:

{
  "title": string,
  "metrics": {
    "headcount": int,
    "payrollCost": decimal,
    "overtimeHours": int
  }
}


Example Response 200:

{
  "dashboardId": "1",
  "message": "Dashboard created successfully."
}


2. View Dashboard

Will verify if requestor is authorized, check if it can find dashboard using ID, then return dashboard inforomation to user
# /GET/v1/dashboards/{dashboard_id}


Example Response 200:

{
  "dashboardId": "1",
  "title": "HR Metrics",
  "ownerId": "1",
  "metrics": {
    "headcount": 50,
    "payrollCost": 200000,
    "overtimeHours": 85
  }
}


3. Share Dashboard

Allows HR Practitioner to share dashboard with list of managers

# /POST/v1/dashboards/{dashboard_id}/share

{
  "managerUserIds": [
    "1",
    "2",
    "3"...
  ]
}

Example Response 200:

{
  "shared_with": ["1","2","3"..]
  "message": "Dashboard shared successfully."
}



