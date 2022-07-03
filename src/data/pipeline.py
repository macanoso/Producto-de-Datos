"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import Task, LocalTarget
import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices


class ingest_data_pipeline(Task):
    def output(self):
        return LocalTarget("data_lake/landing/result.txt")

    def run(self):
        with self.output().open("w") as outfile:
            ingest_data.ingest_data()


class transform_data_pipeline(Task):
    def requires(self):
        return ingest_data_pipeline()

    def output(self):
        return LocalTarget("data_lake/raw/result.txt")

    def run(self):
        with self.output().open("w") as outfile:
            transform_data.transform_data()


class clean_data_pipeline(Task):
    def requires(self):
        return transform_data_pipeline()

    def output(self):
        return LocalTarget("data_lake/cleansed/results3.txt")

    def run(self):
        with self.output().open("w") as outfile:
            clean_data.clean_data()


class daily_reports_pipeline(Task):
    def requires(self):
        return clean_data_pipeline()

    def output(self):
        return LocalTarget("data_lake/business/precios-dia.csv")

    def run(self):
        with self.output().open("w") as outfile:
            compute_daily_prices.compute_daily_prices()


class monthly_reports_pipeline(Task):
    def requires(self):
        return clean_data_pipeline()

    def output(self):
        return LocalTarget("data_lake/business/precios-mes.csv")

    def run(self):
        with self.output().open("w") as outfile:
            compute_monthly_prices.compute_monthly_prices()


class reports_prices(Task):
    def requires(self):
        return [daily_reports_pipeline(), monthly_reports_pipeline()]


if __name__ == "__main__":
    import doctest

    luigi.run(["reports_prices", "--local-scheduler"])
    doctest.testmod()
