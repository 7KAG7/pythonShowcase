

class FillBag:

    def fill_bibag(self, requested_volume, bibag_volume, bibag_pressure, bibag_pressure_limit):
        if bibag_pressure < bibag_pressure_limit:
            return bibag_volume + requested_volume
        else:
            return bibag_volume