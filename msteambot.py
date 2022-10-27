import logging
import pymsteams
import datetime

class HermesBot:
    hook_url: str = None
    client: pymsteams.connectorcard

    def __init__(self):
        self.hook_url = "https://vngms.webhook.office.com/webhookb2/vjndskvds/mvlxcvmlxcv"
        self.client = pymsteams.connectorcard(self.hook_url)

    def sent_message(self, message: str):
        self.client.text(message)
        self.client.send()

    def sent_alert_logging(self, message, generated_id, type_test, project_error, dataset_error, table_error, status):
        current_time = datetime.datetime.now()
        message = f""" 
        Status: {status}
        Project_id: {project_error}
        Dataset_id: {dataset_error}
        Table_id: {table_error}
        {message} {type_test}
        Datetime: {current_time}
        """
        try:
            action_card = pymsteams.connectorcard(hookurl=self.hook_url, http_timeout=30)
            action_card.color("#4e9164")
            action_card.title(generated_id)
            action_card.text(message)
            url = 'https://www.goodreads.com/'
            action_card.addLinkButton(buttontext="Rollback table", buttonurl=url)
            action_card.send()
        except TimeoutError as e:
            logging.error(e)
            print('cannot send message')
