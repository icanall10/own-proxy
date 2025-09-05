import requests
import json

def book_schedule():
    url = "https://api-dasher.doordash.com/v1/dashes/?expand=vehicle.vehicle_type&expand=starting_point&expand=vehicle&extra=vehicle&extra=num_preassigned_deliveries&extra=allowed_ma_seconds&extra=remaining_ma_seconds&extra=auto_assign&extra=can_extend_until&extra=current_manual_assign_interval&extra=is_on_dynamic_pay_model&extra=starting_point&extra=starting_point.submarket&extra=is_waiting_for_expected_assignment&extra=commute_state&extra=commute_expire_time&extra=commute_preference"

    body = {
        "is_impromptu_dash": False,
        "ignore_min_shift_duration": False,
        "dasher": "32691131",
        "scheduled_start_time": "2025-09-02T03:00:00Z",
        "scheduled_end_time": "2025-09-02T03:30:00Z",
        "starting_point": "5069",
        "vehicle": "51410832"
    }

    headers = {
        "host": "api-dasher.doordash.com",
        "dd-app-subvariant": "dasher",
        "dd-ids": '{"dd_device_id":"60F881F7-4246-434B-84FF-4E25CBF98545"}',
        "accept": "application/json",
        "x-session-id": "32F3CACE-71D5-4C2E-A549-4E9417DB8104-dx-ios",
        "x-correlation-id": "11B287AF-8938-44E3-ABDB-E2581A574282-dx-ios",
        "baggage": "dd-instrumentation.priority=1.0",
        "x-att-session-id": "629EA08B-8A72-476C-9A9E-CE955D594B8B",
        "client-version": "ios v2.382.0 b295155",
        "accept-language": "en-US",
        "accept-encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "x-client-request-id": "DE26AB14-6437-4A58-8358-046CF8C58D86-dx-ios",
        "user-agent": "DoorDashDriver/2.382.0 (iPhone; iOS 18.2.1; Scale/3.0)",
        "dd_device_id": "dx_60F881F7-4246-434B-84FF-4E25CBF98545",
        "connection": "keep-alive",
        "traceparent": "00-1648567d445d7000414a1f1edfdf9dd9-efa7b5a75c68dae9-01",
        "authorization": "JWT eyJhbGciOiJIUzI1NiJ9.eyJvcmlnX2lhdCI6MTc1Njc3ODM0NCwicGVkcmVnYWwiOnsiaWQiOiJhMzM4YWUwMC02Y2U3LTRjNjItODU3MS0xODVlY2U2MGQ1YWUifSwiZXhwIjoxNzU3MDM3NTQ0LCJ1c2VyIjp7ImF1dGhfdmVyc2lvbiI6NCwiaXNfc3RhZmYiOmZhbHNlLCJpZCI6MTc2MDQ2MTc4NiwiZW1haWwiOiJhbWFya2hhbm92YTE2QGdtYWlsLmNvbSJ9LCJjaWQiOjE2NDk0OTI4MTIxNjIzNjEzNjZ9.FMpibGeIP4acFG6eqPnU64CVZqVfdLsxuZx6JnkFdr8"
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        print("HTTP Status:", response.status_code)
    except requests.RequestException as e:
        print("Ошибка:", str(e))

if __name__ == "__main__":
    book_schedule()