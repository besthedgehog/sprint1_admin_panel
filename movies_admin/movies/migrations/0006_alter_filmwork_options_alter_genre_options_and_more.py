# Generated by Django 4.2.11 on 2024-07-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_filmwork_certificate_filmwork_file_path"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="filmwork",
            options={"verbose_name": "Filmwork", "verbose_name_plural": "Filmworks"},
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"verbose_name": "Genre", "verbose_name_plural": "Genres"},
        ),
        migrations.AlterModelOptions(
            name="person",
            options={"verbose_name": "Person", "verbose_name_plural": "People"},
        ),
        migrations.AddField(
            model_name="person",
            name="name",
            field=models.CharField(default="name", max_length=255, verbose_name="name"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created"),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="type",
            field=models.CharField(
                choices=[
                    ("MOV", "movie"),
                    ("TV", "tv_show"),
                    ("<class 'movies.models.Filmwork.Type.Meta'>", "Meta"),
                ],
                default="MOV",
                max_length=50,
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created"),
        ),
    ]
