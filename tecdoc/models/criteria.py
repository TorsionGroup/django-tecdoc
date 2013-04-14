# -*- coding: utf-8 -

from base import TecdocModel, TecdocManager

class Criteria(TecdocModel):
    id = models.AutoField(u'��', primary_key=True,
                          db_column='CRI_ID')

    designation = models.ForeignKey(Designation,
                                    verbose_name=u'������祭��',
                                    db_column='CRI_DES_ID')

    short_designation = models.ForeignKey(Designation,
                                          verbose_name=u'��⪮� ������祭��',
                                          db_column='CRI_SHORT_DES_ID',
                                          related_name='+')

    unit = models.ForeignKey(Designation,
                             verbose_name=u'��������',
                             db_column='CRI_UNIT_DES_ID')

    type = models.CharField(u'���', max_length=1,
                            db_column='CRI_TYPE')

    is_interval = models.BooleanField(u'���ࢠ���',
                                      db_column='CRI_IS_INTERVAL')

    child = models.ForeignKey(u'��ன ���਩',
                              db_column='CRI_SUCCESSOR',
                              related_name='parents')

    objects = TecdocManagerWithDes()

    class Meta:
        db_table = 'CRITERIA'


class PartCriteria(TecdocModel):
    part = models.ForeignKey(Part, verbose_name=u'�������',
                             db_column='ACR_ART_ID')

    group = models.ForeignKey(Group, verbose_name=u'��㯯� �����⥩',
                              db_column='ACR_GA_ID')

    criteria = models.ForeignKey(Criteria, verbose_name=u'�������',
                                 db_column='ACR_CRI_ID')

    value = models.CharField(u'���祭��', max_length=60,
                             db_column='ACR_VALUE')

    description = models.ForeignKey(Designation,
                                    verbose_name=u'���ᠭ��',
                                    db_column='ACR_KV_DES_ID')

    sorting = models.IntegerField(u'���冷�', db_column='ACR_SORT')

    class Meta:
        db_table = 'ARTICLE_CRITERIA'

    def get_value(self):
        return self.value or self.description
