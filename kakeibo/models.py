from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)  # 項目名
    amount = models.IntegerField()           # 金額（支出はマイナス）
    recorded_at = models.DateTimeField(auto_now_add=True)  # 記録日時

    def __str__(self):
        return f"{self.name} - {self.amount}円"
