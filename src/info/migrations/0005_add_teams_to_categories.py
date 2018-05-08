# Generated by Django 2.0.4 on 2018-05-08 07:42

from django.db import migrations


def add_teams_to_categories(apps, schema_editor):
    InfoCategory = apps.get_model("info", "InfoCategory")
    Team = apps.get_model("teams", "Team")
    Camp = apps.get_model("camps", "Camp")

    # 2016 - Everything is orga team
    camp2016 = Camp.objects.filter(slug="bornhack-2016")
    orga2016 = Team.objects.filter(camp=camp2016, name="Orga")
    InfoCategory.objects.filter(camp=camp2016).update(team=orga2016)

    # 2017 - Everything is orga team
    camp2017 = Camp.objects.filter(slug="bornhack-2017")
    orga2017 = Team.objects.filter(camp=camp2017, name="Orga")
    InfoCategory.objects.filter(camp=camp2017).update(team=orga2017)

    # 2018 - Map categories to teams
    camp2018 = Camp.objects.filter(slug="bornhack-2018")
    team2018 = Team.objects.filter(camp=camp2018)
    infocategories2018 = InfoCategory.objects.filter(camp=camp2018)

    # Info team
    infoteam = team2018.filter(name="Info")
    info_anchors = [
        "what",
        "when",
        "travel",
        "where",
        "sleep",
        "bicycles",
        "infodesk-and-cert",
        "shower-and-toilets",
        "venue-map",
        "villages",
    ]
    infocategories2018.filter(anchor__in=info_anchors).update(team=infoteam)

    # Food team
    food = team2018.filter(name="Food")
    infocategories2018.filter(anchor_in=["food-and-groceries"]).update(team=food)

    # NOC team
    noc = team2018.filter(name="NOC")
    infocategories2018.filter(anchor__in=["network"]).update(team=noc)

    # Power team
    power = team2018.filter(name="Power")
    infocategories2018.filter(anchor__in=["power"]).update(team=power)

    # Shuttle bus
    shuttle_bus = team2018.filter(name="Shuttle Bus")
    infocategories2018.filter(anchor__in=["shuttle-bus"]).update(team=shuttle_bus)

    # Bar
    bar = team2018.filter(name="Bar")
    infocategories2018.filter(anchor__in=["bar"]).update(team=bar)


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_infocategory_team'),
    ]

    operations = [
        migrations.RunPyton(add_teams_to_categories)
    ]
