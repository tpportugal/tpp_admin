import csv
import os
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from api.apps.geographical.districts.models import District
from api.apps.geographical.counties.models import County

from django.conf import settings


class Command(BaseCommand):
    help = "Importa todos os concelhos do ficheiro (vendors/tpp-data/concelhos.csv) para o modelo (County)"

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
                                 "concelhos.csv")

        """
        Os reguladoras servem para identificar tipo de dados num conjunto de dados e 
        converterem os dados no formato desejado.
        A identificação é feita pela posição da coluna
        """
        regulators = {
            "district__id": {
                "pos": 0,
                "type": int
            },
            "id": {
                "pos": 1,
                "type": str
            },
            "name": {
                "pos": 2,
                "type": str
            }
        }

        """
        Remover os dados do modelo County
        """
        County.objects.all().delete()

        """
        Iteração sobre os dados do CSV
        """
        with open(os.path.join(os.path.sep, file_path), "r") as f:
            next(f)  # Ignore first line (header)
            reader = csv.reader(f)
            count = 0
            for row in list(reader):
                # Identificação dos dados
                district__id = row[regulators["district__id"]["pos"]]
                id = row[regulators["id"]["pos"]]
                name = row[regulators["name"]["pos"]]
                # Conversão dos dados
                district__id = regulators["district__id"]["type"](district__id)
                id = regulators["id"]["type"](id)
                name = regulators["name"]["type"](name)
                # Concatenação do district_id com o id para gerar um id único
                id = int(str(district__id) + str(id))
                county = County()
                county.id = id
                county.slug = slugify(name)
                county.name = name
                county.district = District.objects.get(id=district__id)
                county.save()
                count += 1
            print("A importação dos concelhos foi realizada com sucesso: {0} concelhos importados".format(count))
