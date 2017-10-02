# pylint: disable=too-many-ancestors
""" View Set for Raid Item Serializer """
from rest_framework import viewsets, permissions
from app.models.raid_item import RaidItem
from app.serializers.raid_item import RaidItemSerializer


class RaidItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Raid Item Serializer
    """

    queryset = RaidItem.objects.all().order_by('end_date')
    serializer_class = RaidItemSerializer
    permission_classes = [permissions.AllowAny]
