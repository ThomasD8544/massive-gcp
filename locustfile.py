from locust import HttpUser, task


class TimelineUser(HttpUser):
    user_index = 1
    host = "https://projet-cloud-494614.ew.r.appspot.com"

    def on_start(self):
        self.user_id = TimelineUser.user_index
        TimelineUser.user_index += 1

    @task
    def get_timeline(self):
        self.client.get(f"/api/timeline?user=user{self.user_id}&limit=20")
