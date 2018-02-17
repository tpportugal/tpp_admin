import csv
import os
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from api.apps.geographical.districts.models import District
from api.apps.geographical.counties.models import County
from api.apps.geographical.places.models import Place

from django.conf import settings


class Command(BaseCommand):
    help = "Importa todas localidades do ficheiro (vendors/tpp-data/localidades.csv) para o modelo (Place)"

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
                                 "localidades.csv")

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
            "county__id": {
                "pos": 1,
                "type": str
            },
            "id": {
                "pos": 2,
                "type": int
            },
            "name": {
                "pos": 3,
                "type": str
            }
        }

        """
        Remover os dados do modelo Place
        """
        Place.objects.all().delete()

        """
        Iteração sobre os dados do CSV
        """
        with open(os.path.join(os.path.sep, file_path), "r") as f:
            next(f)  # Ignore first line (header)
            reader = csv.reader(f)
            count = 0
            _places = {}
            for row in list(reader):
                # Identificação dos dados
                district__id = row[regulators["district__id"]["pos"]]
                county__id = row[regulators["county__id"]["pos"]]
                id = row[regulators["id"]["pos"]]
                name = row[regulators["name"]["pos"]]
                # Conversão dos dados
                district__id = regulators["district__id"]["type"](district__id)
                county__id = regulators["county__id"]["type"](county__id)
                id = regulators["id"]["type"](id)
                name = regulators["name"]["type"](name)
                # Concatenação do district_id com o county__id para gerar um id único
                county__id = int(str(district__id) + str(county__id))
                _places[id] = [district__id, county__id, id, name]

            for k, row in _places.items():
                # Identificação dos dados
                district__id = row[regulators["district__id"]["pos"]]
                county__id = row[regulators["county__id"]["pos"]]
                id = row[regulators["id"]["pos"]]
                name = row[regulators["name"]["pos"]]
                place = Place()
                place.id = id
                place.slug = slugify(name)
                place.name = name
                place.county = County.objects.get(id=county__id)
                place.save()
                count += 1
            print("A importação das localidades foi realizada com sucesso: {0} localidades importados".format(count))
