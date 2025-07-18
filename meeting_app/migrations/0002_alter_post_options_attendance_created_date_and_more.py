# Generated by Django 5.2.1 on 2025-06-11 16:08

import datetime
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-is_pinned', '-writeDate'], 'verbose_name': '게시글', 'verbose_name_plural': '게시글들'},
        ),
        migrations.AddField(
            model_name='attendance',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='기록일시'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일시'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='description',
            field=models.TextField(blank=True, verbose_name='클래스 설명'),
        ),
        migrations.AddField(
            model_name='class',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='활성 상태'),
        ),
        migrations.AddField(
            model_name='class',
            name='max_members',
            field=models.PositiveIntegerField(default=20, help_text='최대 참여 가능 인원', verbose_name='최대 인원'),
        ),
        migrations.AddField(
            model_name='interests',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interests',
            name='description',
            field=models.TextField(blank=True, verbose_name='설명'),
        ),
        migrations.AddField(
            model_name='interests',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='활성 상태'),
        ),
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='활성 상태'),
        ),
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='마지막 로그인'),
        ),
        migrations.AddField(
            model_name='memberinterests',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='등록일시'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_pinned',
            field=models.BooleanField(db_index=True, default=False, verbose_name='상단 고정'),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='조회수'),
        ),
        migrations.AddField(
            model_name='sugang',
            name='status',
            field=models.CharField(choices=[('pending', '대기중'), ('approved', '승인됨'), ('cancelled', '취소됨')], db_index=True, default='approved', max_length=20, verbose_name='신청상태'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendDate',
            field=models.DateField(db_index=True, verbose_name='출석일'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendanceStatus',
            field=models.CharField(choices=[('present', '출석'), ('absent', '결석'), ('late', '지각')], db_index=True, default='present', max_length=20, verbose_name='출석상태'),
        ),
        migrations.AlterField(
            model_name='class',
            name='classEndDate',
            field=models.DateField(db_index=True, help_text='YYYY-MM-DD 형식', verbose_name='종료일'),
        ),
        migrations.AlterField(
            model_name='class',
            name='className',
            field=models.CharField(db_index=True, max_length=150, validators=[django.core.validators.MinLengthValidator(2, message='클래스명은 2자 이상이어야 합니다.')], verbose_name='클래스명'),
        ),
        migrations.AlterField(
            model_name='class',
            name='classStartDate',
            field=models.DateField(db_index=True, help_text='YYYY-MM-DD 형식', verbose_name='시작일'),
        ),
        migrations.AlterField(
            model_name='interests',
            name='interestName',
            field=models.CharField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='관심사명에는 한글, 영문, 숫자, 공백, /만 사용할 수 있습니다.', regex='^[가-힣a-zA-Z0-9\\s/]+$')], verbose_name='관심사명'),
        ),
        migrations.AlterField(
            model_name='member',
            name='accountID',
            field=models.CharField(help_text='4-50자의 영문, 숫자 조합', max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(4, message='계정ID는 4자 이상이어야 합니다.'), django.core.validators.RegexValidator(message='계정ID는 영문과 숫자만 사용할 수 있습니다.', regex='^[a-zA-Z0-9]+$')], verbose_name='계정ID'),
        ),
        migrations.AlterField(
            model_name='member',
            name='accountType',
            field=models.CharField(choices=[('student', '학생'), ('instructor', '강사'), ('admin', '관리자')], db_index=True, default='student', max_length=20, verbose_name='계정타입'),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth',
            field=models.DateField(help_text='YYYY-MM-DD 형식', verbose_name='생년월일'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator(message='올바른 이메일 형식이 아닙니다.')], verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='member',
            name='joinDate',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='가입일'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(db_index=True, max_length=45, validators=[django.core.validators.RegexValidator(message='이름은 한글, 영문만 사용할 수 있습니다.', regex='^[가-힣a-zA-Z\\s]+$')], verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8, message='비밀번호는 8자 이상이어야 합니다.')], verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phoneNum',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(message='전화번호 형식이 올바르지 않습니다. (예: 010-1234-5678)', regex='^01[0-9]-\\d{4}-\\d{4}$')], verbose_name='전화번호'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('notice', '공지'), ('review', '후기'), ('general', '일반')], db_index=True, default='general', max_length=50, verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, message='내용은 10자 이상이어야 합니다.')], verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=200, validators=[django.core.validators.MinLengthValidator(2, message='제목은 2자 이상이어야 합니다.')], verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='post',
            name='writeDate',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='sugang',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='신청일시'),
        ),
        migrations.AddIndex(
            model_name='attendance',
            index=models.Index(fields=['attendDate', 'attendanceStatus'], name='attendance_attendD_d642c0_idx'),
        ),
        migrations.AddIndex(
            model_name='attendance',
            index=models.Index(fields=['sugang_sugangID', 'attendDate'], name='attendance_sugang__b812bc_idx'),
        ),
        migrations.AddIndex(
            model_name='attendance',
            index=models.Index(fields=['-attendDate'], name='attendance_attendD_d20fc4_idx'),
        ),
        migrations.AddIndex(
            model_name='class',
            index=models.Index(fields=['interestID', 'classStartDate'], name='class_interes_bbb365_idx'),
        ),
        migrations.AddIndex(
            model_name='class',
            index=models.Index(fields=['is_active', '-classID'], name='class_is_acti_114a81_idx'),
        ),
        migrations.AddIndex(
            model_name='class',
            index=models.Index(fields=['classStartDate', 'classEndDate'], name='class_classSt_30fbf5_idx'),
        ),
        migrations.AddIndex(
            model_name='class',
            index=models.Index(fields=['-created_date'], name='class_created_021e72_idx'),
        ),
        migrations.AddIndex(
            model_name='interests',
            index=models.Index(fields=['interestName'], name='interests_interes_81d693_idx'),
        ),
        migrations.AddIndex(
            model_name='interests',
            index=models.Index(fields=['is_active', 'interestName'], name='interests_is_acti_76368b_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['accountType', 'joinDate'], name='member_account_f6782b_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['name'], name='member_name_726852_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['-joinDate'], name='member_joinDat_345884_idx'),
        ),
        migrations.AddIndex(
            model_name='memberinterests',
            index=models.Index(fields=['member', 'interests'], name='memberInter_member__476bdb_idx'),
        ),
        migrations.AddIndex(
            model_name='memberinterests',
            index=models.Index(fields=['interests'], name='memberInter_interes_da24ff_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['class_classID', 'category', '-writeDate'], name='post_class_c_7b5f36_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['author', '-writeDate'], name='post_author__14079b_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-writeDate'], name='post_writeDa_3c374f_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['category'], name='post_categor_e3adb5_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-is_pinned', '-writeDate'], name='post_is_pinn_cf3958_idx'),
        ),
        migrations.AddIndex(
            model_name='sugang',
            index=models.Index(fields=['class_classID', 'status'], name='sugang_class_c_d53abe_idx'),
        ),
        migrations.AddIndex(
            model_name='sugang',
            index=models.Index(fields=['member_accountID', '-registration_date'], name='sugang_member__4e22e3_idx'),
        ),
        migrations.AddIndex(
            model_name='sugang',
            index=models.Index(fields=['-registration_date'], name='sugang_registr_d5d628_idx'),
        ),
        migrations.AddConstraint(
            model_name='class',
            constraint=models.CheckConstraint(condition=models.Q(('classEndDate__gt', models.F('classStartDate'))), name='valid_class_dates'),
        ),
        migrations.AddConstraint(
            model_name='class',
            constraint=models.CheckConstraint(condition=models.Q(('max_members__gt', 0)), name='positive_max_members'),
        ),
        migrations.AddConstraint(
            model_name='member',
            constraint=models.CheckConstraint(condition=models.Q(('birth__lte', datetime.date(2025, 6, 12))), name='valid_birth_date'),
        ),
    ]
