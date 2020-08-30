class Helper:

    @staticmethod
    def normalizer_request(data):
        try:
            data._mutable = True
            result = data.dict()
        except:
            result = data

        return result
