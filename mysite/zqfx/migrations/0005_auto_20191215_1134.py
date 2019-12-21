# Generated by Django 2.1.3 on 2019-12-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zqfx', '0004_zqfx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='win007',
            name='detail',
            field=models.TextField(null=True, verbose_name='详细情况'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='full_result',
            field=models.CharField(max_length=10, null=True, verbose_name='比分'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='g_odd',
            field=models.CharField(max_length=10, null=True, verbose_name='客胜赔率'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='guest_team',
            field=models.CharField(max_length=20, null=True, verbose_name='客队'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='h_odd',
            field=models.CharField(max_length=10, null=True, verbose_name='主胜赔率'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='home_team',
            field=models.CharField(max_length=20, null=True, verbose_name='主队'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right1',
            field=models.CharField(max_length=20, null=True, verbose_name='足球大贏家'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right2',
            field=models.CharField(max_length=20, null=True, verbose_name='足彩大富翁'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right3',
            field=models.CharField(max_length=20, null=True, verbose_name='明報'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right4',
            field=models.CharField(max_length=20, null=True, verbose_name='太 陽 報'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right5',
            field=models.CharField(max_length=20, null=True, verbose_name='東方日報'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right6',
            field=models.CharField(max_length=20, null=True, verbose_name='蘋果日報'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='mar_right60',
            field=models.CharField(max_length=20, null=True, verbose_name='推介'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='match_time',
            field=models.CharField(max_length=20, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='odds_14_f_result',
            field=models.CharField(max_length=30, null=True, verbose_name='韦德初盘(亚)'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='odds_14_l_result',
            field=models.CharField(max_length=30, null=True, verbose_name='韦德即时(亚)'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='odds_3_f_result',
            field=models.CharField(max_length=30, null=True, verbose_name='Crown初盘(亚)'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='odds_3_l_result',
            field=models.CharField(max_length=30, null=True, verbose_name='Crown即时(亚)'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='odds_8_f_result',
            field=models.CharField(max_length=30, null=True, verbose_name='Bet365初盘(亚)'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='odds_8_l_result',
            field=models.CharField(max_length=30, null=True, verbose_name='Bet365即时(亚)'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='oddstr_115_f_result',
            field=models.CharField(max_length=30, null=True, verbose_name='威廉希尔初盘'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='oddstr_115_l_result',
            field=models.CharField(max_length=30, null=True, verbose_name='威廉希尔即时'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='oddstr_281_f_result',
            field=models.CharField(max_length=30, null=True, verbose_name='bet365初盘'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='oddstr_281_l_result',
            field=models.CharField(max_length=30, null=True, verbose_name='bet365即时'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='oddstr_82_f_result',
            field=models.CharField(max_length=30, null=True, verbose_name='立博初盘'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='oddstr_82_l_result',
            field=models.CharField(max_length=30, null=True, verbose_name='立博即时'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='pk_odd',
            field=models.CharField(max_length=10, null=True, verbose_name='打平赔率'),
        ),
        migrations.AlterField(
            model_name='win007',
            name='url',
            field=models.CharField(max_length=50, null=True, verbose_name='相关链接'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_02_c01',
            field=models.CharField(max_length=50, null=True, verbose_name='彩种1'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_02_c01y',
            field=models.CharField(max_length=50, null=True, verbose_name='彩种2'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_02_c01yg',
            field=models.CharField(max_length=50, null=True, verbose_name='概率2'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_02_c01yp',
            field=models.CharField(max_length=50, null=True, verbose_name='盘口2'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_02_c01yt',
            field=models.CharField(max_length=50, null=True, verbose_name='推荐2'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_02_c03',
            field=models.CharField(max_length=50, null=True, verbose_name='推荐1'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_2_03_gailus1',
            field=models.CharField(max_length=50, null=True, verbose_name='概率1'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_leauge',
            field=models.CharField(max_length=50, null=True, verbose_name='联赛'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_leauge_name0',
            field=models.CharField(max_length=50, null=True, verbose_name='主队'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='fxs_leauge_name1',
            field=models.CharField(max_length=50, null=True, verbose_name='客队'),
        ),
        migrations.AlterField(
            model_name='zqfx',
            name='predictc',
            field=models.CharField(max_length=50, null=True, verbose_name='百分比'),
        ),
    ]