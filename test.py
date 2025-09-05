import requests
import json

def book_schedule():
    url = "https://api-dasher.doordash.com/v1/dashes/?expand=vehicle.vehicle_type&expand=starting_point&expand=vehicle&extra=vehicle&extra=num_preassigned_deliveries&extra=allowed_ma_seconds&extra=remaining_ma_seconds&extra=auto_assign&extra=can_extend_until&extra=current_manual_assign_interval&extra=is_on_dynamic_pay_model&extra=starting_point&extra=starting_point.submarket&extra=is_waiting_for_expected_assignment&extra=commute_state&extra=commute_expire_time&extra=commute_preference"

    body = {
        "is_impromptu_dash": False,
        "ignore_min_shift_duration": False,
        "dasher": "29310437",
        "scheduled_start_time": "2025-09-05T20:30:00Z",
        "scheduled_end_time": "2025-09-05T21:00:00Z",
        "starting_point": "5105",
        "vehicle": "31289279"
    }

    headers = {
        "host": "api-dasher.doordash.com",
        "dd-app-subvariant": "dasher",
        "dd-ids": '{"dd_device_id":"60F881F7-4246-434B-84FF-4E25CBF98545"}',
        "accept": "application/json",
        "x-session-id": "0d263a19-cd0f-45fa-b012-07b3009c070e-dx-ios",
        "x-correlation-id": "f7a23a98-d01c-49db-b0c3-44412736223d-dx-ios",
        "baggage": "dd-instrumentation.priority=1.0",
        "x-att-session-id": "BC33B89E-DEFB-4397-9065-118A39BD0C77",
        "client-version": "ios v2.382.0 b295155",
        "accept-language": "en-US",
        "accept-encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "x-client-request-id": "e145f220-ca22-4b00-9747-745c2c979d1c-dx-ios",
        "user-agent": "DoorDashDriver/2.368.0 (iPhone; iOS 18.2.1; Scale/3.0)",
        "dd_device_id": "dx_60F881F7-4246-434B-84FF-4E25CBF98545",
        "connection": "keep-alive",
        "traceparent": "00-3a0fe2a7924b83a44a9dde14968dae72-549367b08e63015d-01",
        "authorization": "JWT eyJhbGciOiJIUzI1NiJ9.eyJvcmlnX2lhdCI6MTc1NzA5NDY1NiwicGVkcmVnYWwiOnsiaWQiOiJjZmQ5YzU5YS04MDhjLTRhNWMtOGQ2Ni0wN2Q5ZGI5N2RjN2YifSwiZXhwIjoxNzU3MzUzODU2LCJ1c2VyIjp7ImF1dGhfdmVyc2lvbiI6MiwiaXNfc3RhZmYiOmZhbHNlLCJpZCI6MTYwNzI3MDkxOCwiZW1haWwiOiJraXJzYW4ubWFuZHpoaWV2QGdtYWlsLmNvbSJ9LCJjaWQiOjE2NDk0OTI4MTIxNjIzNjEzNjZ9.hFA4YrOEJzI9y3NfvmDVP1KRUkb1kOwKm1BsFBtMaXY"
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        print("HTTP Status:", response.status_code)
    except requests.RequestException as e:
        print("Ошибка:", str(e))

if __name__ == "__main__":
    book_schedule()