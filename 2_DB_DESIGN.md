# Logical DB Design

# Users Table

Stores information about HR Practitioners and Managers.

|  Column  | DataType |   Description                             |
|----------|-----------|------------------------------------------|
| user_id  | int      | Unique ID for the user                    | (primary key)
| name     | string   | Full name                                 |
| email    | string   | Unique email address                      |
| role     | enum     | User role: 'HR_Practitioner' or 'Manager' |

# Dashboards Table

|  Column        | DataType |   Description                   |
|----------|-----------|--------------------------------------|
| dashboard_id   | int      | Unique ID for the dashboard     | (primary key)
| owner_id       | int      | Users.user_id                   | (foreign key)
| created_at     | datetime | Timestamp dashboard was created |
| title          | string   | Dashboard Title                 |
| headcount      | int      | Headcount Value                 |
| payroll_cost   | decimal  | Payroll Cost Value              |
| total_overtime | int      | Overtime Hours Value            | 

# Shared Dashboards Table

|  Column        | DataType |   Description                                 |
|----------|-----------|----------------------------------------------------|
| share_id     | int             | Unique ID for shared dashboard           | (primary key)
| dashboard_id | int             | Dashboards.dashboard_id                  | (foreign key)
| shared_at    | datetime        | Timestamp when dashboard was last shared |




