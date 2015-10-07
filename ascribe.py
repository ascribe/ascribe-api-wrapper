import requests

class AscribeWrapper:

    def __init__(self, token):
        self.token = token
        self.base = 'https://www.ascribe.io'
        self.headers = {"Authorization": self.token, "User-Agent": "ascribe-api-wrapper v0.01", "Content-Type": "application/json"}

    def _get_data(self, path, payload={}):
        rq = requests.get(self.base + path, headers=self.headers, params=payload)
        if rq.status_code == 200:
            return rq.json()
        else:
            raise Exception("Request failed!")

    def _post_data(self, path, data):
        rq = requests.post(self.base + path, data=json.dumps(data), headers=self.headers)
        if rq.status_code == 201:
            return rq.json()
        else:
            raise Exception("Request failed!")

    def _delete_data(self, path, data={}):
        rq = requests.delete(self.base + path, headers=self.headers, data=data)
        if rq.status_code == 200:
            return rq.json()
        else:
            raise Exception("Request failed!")

    def list_pieces(self):
        path = "/api/pieces/"
        return self._get_data(path)

    def create_piece(self, piece):
        path = "/api/pieces/"
        return self._post_data(path, piece)

    def retrieve_piece(self, piece_id):
        path = "/api/pieces/piece_id"
        return self._get_data(path)

    def delete_piece(self):
        path = "/api/pieces/piece_id"
        return self._delete_data(path)

    def retrieve_all_editions_of_piece(self, piece_id):
        path = "/api/pieces/{}/editions/".format(piece_id)
        return self._get_data(path)

    def list_editions(self):
        path = "/api/editions/"
        return self._get_data(path)

    def create_editions(self, piece_id, num_editions=None):
        """
        attributes:
        piece_id - number
        num_editions - number
        """
        path = "/api/editions/"
        data = {"piece_id": piece_id}
        if num_editions:
            data["num_editions"] = num_editions
        return self._post_data(path, data)

    def retrieve_edition(self, edition_id):
        """
        attrs:
        edition_id - The bitcoin id of the edition
        """
        path = "/api/editions/{}/".format(edition_id)

        return self._get_data(path)

    def delete_edition(self, edition_id):
        path = "/api/editions/{}/".format(edition_id)
        return self._delete_data(path)

    def list_registrations(self):
        path = "/api/ownership/registrations/"
        return self._get_data(path)

    def retrieve_registration(self, registration_id):
        path = "/api/ownership/registrations/{}/".format(registration_id)
        return self._get_data(path)

    def list_all_transfers(self):
        """
        page    (optional) <int> The pagination number
        page_size   (optional) <int> Number of results per page
        """
        path = "/api/ownership/transfers/"
        return self._get_data(path)

    def create_transfer(self, transfer):
        """
        bitcoin_id  <string> The ID as the registration address of the edition
        transferee  <email> The email of the new owner
        password    <string> Your ascribe password
        transfer_message    (optional) <string> Additional message
        """
        path = "/api/ownership/transfers/"
        return self._post_data(path, transfer)

    def retrieve_transfer(self, transfer_id):
        path = "/api/ownership/transfers/{}/".format(transfer_id)
        return self._get_data(path)

    def consign_edition(self):
        pass

    def list_consignments(self):
        pass

    def confirm_consignment(self):
        pass

    def deny_consignment(self):
        pass

    def retrieve_consignment(self):
        pass

    def unconsign_edition(self):
        pass

    def list_all_unconsignments(self):
        pass

    def request_unconsignment(self):
        pass

    def deny_unconsignment(self):
        pass

    def retrieve_unconsignment(self):
        pass

    def loan_edition(self):
        pass

    def list_loans_for_editions(self):
        pass

    def retrieve_loan_for_edition(self):
        pass

    def confirm_loan_for_edition(self):
        pass

    def deny_loan_for_edition(self):
        pass

if __name__ == '__main__':
    token = "Bearer x"
    am = AscribeWrapper(token)