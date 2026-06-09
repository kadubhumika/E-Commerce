from core.celery_app import celery_app

@celery_app.task
def send_order_confirmation(order_id):

    print(
        f"Order confirmation sent for order {order_id}"
    )