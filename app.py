from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

DASHBOARDS = {}
SHARES = {}
dashboard_counter = 1
share_counter = 1

@app.route("/")
def index():
    return {"message": "API is running..."}


@app.route("/dashboards/create", methods=["POST"])
def create_dashboard():
    """
    Create dashboard: This function will first validate input request fields and metrics,
    then generate a unique dashboard ID and dashboard information in JSON.
    It will then store the dashboard in DB (in this case memory), and then return JSON with 
    dashboard information to the user.
    """
    global dashboard_counter
    input_data = request.get_json()

    required_fields = ["dashboard_title", "owner_id", "metrics"]
    # Validate required fields of dashboard
    for field in required_fields:
        if field not in input_data:
            return {"error": f"'{field}' is required"}, 400

    HCM_metrics = ["headcount", "payrollCost", "overtimeHours"]
    # Validate metrics needed to create dashboard
    if set(input_data["metrics"].keys()) != set(HCM_metrics):
        return {
            "error": f"Metrics must include exactly: {HCM_metrics}"
        }, 400

    dashboard = {
        "id": dashboard_counter,
        "created_at": datetime.now(),
        "title": input_data["dashboard_title"],
        "owner_id": input_data["owner_id"],
        "metrics": input_data["metrics"]
    }

    DASHBOARDS[dashboard_counter] = dashboard
    dashboard_counter += 1

    return jsonify(dashboard), 201


@app.route("/dashboards/<int:dashboard_id>", methods=["GET"])
def get_dashboard(dashboard_id):

    """
    Get Dashboard by ID: This function will check if it can find the dashboard using ID
    If it can find it, it returns dashboard information to the user.
    """
    dashboard = DASHBOARDS.get(dashboard_id)

    if not dashboard:
        return {"error": "Dashboard with ID: {dashboard_id} was not found"}, 404
    return jsonify(dashboard)


@app.route("/dashboards/<int:dashboard_id>/share", methods=["POST"])
def share_dashboard(dashboard_id):

    """
    Share dashboard: Check if dashboard information can be found in DB (in this case memory),
    using dashboard ID. If it is found, allows the user to share dashboard with 
    list of managers.
    """
    global share_counter

    if dashboard_id not in DASHBOARDS:
        return {"error": "Dashboard with ID: {dashboard_id} was not found"}, 404

    input_data = request.get_json()
    manager_ids = input_data.get("manager_ids")

    # Check if managers ID field is not empty and it is a list type
    if manager_ids == [] or not isinstance(manager_ids, list):
        return {"error": "'manager_ids' must be a list with one or more ids"}, 400

    SHARES[share_counter] = {
        "share_id": share_counter,
        "dashboard_id": dashboard_id,
        "shared_at": datetime.now(),
        "manager_ids": manager_ids
    }
    share_counter += 1

    # Send emails to manager notifying them dashboard has been shared.

    # For below loop, the get_manager_email function and send_email function are not shown 
    # in this code, but I indicated a summary of each function below.
    # get_manager_email: I would would retreive that manager's email from the DB.
    # send_email: I would use SMTP library to trigger a email notification with server, port, address, etc.

    # for id in manager_ids:
    #     email = get_manager_email(id)
    #     subject = f"Dashboard {dashboard_id} Shared With You"
    #     body = f"Hello, \n Dashboard {dashboard_id} has been shared with you."
    #     send_email(email, subject, body)

    # Notify user in return statement that dashboard is now being shared with list of manager IDs.
    return {
    "shared_with": f"Manager Ids: {manager_ids}",
    "message": f"Dashboard {dashboard_id} is now shared successfully"}, 200

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)