import csv
import os
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from api.apps.geographical.districts.models import District
from django.conf import settings


class Command(BaseCommand):
    help = "Importa todos os distritos do ficheiro (vendors/tpp-data/distritos.csv) para o modelo (Districts)"

    def handle(self, *args, **options):
        """
        file_path é a variável onte contém o caminho do ficheiro CSV
        BASE_DIR é a pasta da raíz do projeto
        """
        file_path = os.path.join(os.path.sep,
                                 settings.BASE_DIR,
                                 "api",
                                 "vendors",
                                 "tpp-data",
                                 "distritos.csv")

        """
        Os reguladoras servem para identificar tipo de dados num conjunto de dados e 
        converterem os dados no formato desejado.
        A identificação é feita pela posição da coluna
        """
        regulators = {
            "id": {
                "pos": 0,
                "type": int
            },
            "name": {
                "pos": 1,
                "type": str
            }
        }

        """
        Remover os dados do modelo District
        """
        District.objects.all().delete()

        """
        Iteração sobre os dados do CSV
        """
        with open(os.path.join(os.path.sep, file_path), "r") as f:
            next(f)  # Ignore first line (header)
            reader = csv.reader(f)
            count = 0
            for row in list(reader):
                # Identificação dos dados
                id = row[regulators["id"]["pos"]]
                name = row[regulators["name"]["pos"]]
                # Conversão dos dados
                id = regulators["id"]["type"](id)
                name = regulators["name"]["type"](name)
                district = District()
                district.id = id
                district.slug = slugify(name)
                district.name = name
                district.save()
                count += 1
            print("A importação dos distritos foi realizada com sucesso: {0} distritos importados".format(count))
