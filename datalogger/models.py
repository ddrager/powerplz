from django.db import models


class DataPoint(models.Model):
    """
    DataPoint Model
    Logs various data points
    """
    UNKNOWN = "UNKNOWN"
    WATTS = "WATTS"
    KILOWATTHRS = "KILOWATTHRS"

    DATA_TYPES = (
        (UNKNOWN, 'Unknown'),
        (WATTS, 'Watts'),
        (KILOWATTHRS, 'KWH'),
    )

    type = models.CharField(max_length=12,choices=DATA_TYPES, default=UNKNOWN)
    value = models.DecimalField(
        help_text="Value",
        default=0,
        decimal_places=8,
        max_digits=16,
        # validators=[MinValueValidator(Decimal('0.00'))] to enforce positive
    )
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
