from django.db import models
from users.models import User

class MgiCandles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signal = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    trade_signal = models.CharField(
        max_length=4, 
        choices=(("buy", "Buy"), ("sell", "Sell")), 
        null=True, blank=True
    )
    is_active = models.BooleanField(default=False, null=True, blank=True)

    # Candle Images
    idea_candle = models.ImageField(upload_to='idea_candles/', null=True, blank=True)
    line_graph_candle = models.ImageField(upload_to='line_graph_candles/', null=True, blank=True)
    signal_candle = models.ImageField(upload_to='signal_candles/', null=True, blank=True)
   
    def __str__(self):
        return f"{self.signal} by {self.user.email}"
