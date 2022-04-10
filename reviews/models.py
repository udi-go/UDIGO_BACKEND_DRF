from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonModel
from places.models import TourPlace, KakaoPlace


class Review(CommonModel):
    place_type = models.CharField(max_length=50, verbose_name=_("장소 유형"))
    place_tour = models.ForeignKey(
        TourPlace, null=True, on_delete=models.CASCADE, verbose_name=_("투어")
    )
    place_kakao = models.ForeignKey(
        KakaoPlace, null=True, on_delete=models.CASCADE, verbose_name=_("카카오")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("회원"))
    grade = models.PositiveSmallIntegerField(verbose_name=_("평점"))
    text = models.TextField(blank=True, verbose_name=_("리뷰"))

    class Meta:
        db_table = "reviews"