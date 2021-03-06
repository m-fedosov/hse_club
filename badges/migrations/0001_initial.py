# Generated by Django 3.2.5 on 2021-10-20 10:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0022_alter_user_secret_hash'),
        ('comments', '0008_auto_20210911_0827'),
        ('posts', '0024_postsubscription_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256, null=True)),
                ('price_days', models.IntegerField(default=10)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'badges',
            },
        ),
        migrations.CreateModel(
            name='UserBadge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(null=True)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_badges', to='badges.badge')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_badges', to='comments.comment')),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_badges', to='users.user')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_badges', to='posts.post')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_badges', to='users.user')),
            ],
            options={
                'db_table': 'user_badges',
                'unique_together': {('from_user', 'to_user', 'badge', 'comment_id'), ('from_user', 'to_user', 'badge', 'post_id')},
            },
        ),
    ]
