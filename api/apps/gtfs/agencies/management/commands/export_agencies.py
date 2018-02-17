import csv
import os
import time
from django.core.management.base import BaseCommand

from django.conf import settings

from api.apps.gtfs.agencies.models import Agency


class Command(BaseCommand):
    help = "Exporta as operadoras de transportes públicos de portugal para um CSV"

    def handle(self, *args, **options):
        """
        file_path é a variável do caminho do ficheiro CSV
        BASE_DIR é a pasta da raíz do projeto
        """
        file_path = os.path.join(os.path.sep,
                                 settings.BASE_DIR,
                                 "export_agencies_{0}.csv".format(time.strftime("%Y%m%d-%H%M%S")))

        """
        Criação do ficheiro CSV
        """
        with open(file_path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow([
                "agency_id",
                "slug",
                "name",
                "url",
                "timezone",
            ])

            """
            Iteração sobre os dados do modelo Agency
            """
            for agency in Agency.objects.all():
                writer.writerow([
                    agency.id,
                    agency.slug,
                    agency.name,
                    agency.url,
                    agency.timezone
                ])

        print("A exportação das operadoras de transportes públicos de portugal foi realizada com sucesso.")
        print("Localização do ficheiro: {0}".format(file_path))
