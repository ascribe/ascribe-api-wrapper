import responses


def test_ascribe_wrapper_instantiation():
    from ascribe import AscribeWrapper
    token = 'token'
    ascribe_wrapper = AscribeWrapper(token)
    assert ascribe_wrapper.token == token
    assert ascribe_wrapper.base == 'https://www.ascribe.io'
    assert 'Authorization' in ascribe_wrapper.headers
    assert 'User-Agent' in ascribe_wrapper.headers
    assert 'Content-Type' in ascribe_wrapper.headers
    assert ascribe_wrapper.headers['Authorization'] == token
    assert ascribe_wrapper.headers['User-Agent'] == 'ascribe-api-wrapper v0.01'
    assert ascribe_wrapper.headers['Content-Type'] == 'application/json'


@responses.activate
def test_list_pieces(ascribe_wrapper):
    responses.add(responses.GET, 'https://www.ascribe.io/api/pieces/',
                  json={'pieces': []}, status=200,
                  content_type='application/json')

    response_json = ascribe_wrapper.list_pieces()
    assert response_json == {'pieces': []}


@responses.activate
def test_create_piece(ascribe_wrapper):
    json = {
        'edition': {
            'title': 'New Piece',
            'artist_name': 'New Artist',
            'num_editions': 1,
            'user_registered': 'alice',
            'datetime_registered': '2015-07-01T13:40:28.635Z',
            'date_created': '2015-01-01',
            'thumbnail': 'thumbnail_url',
            'license_type': {
                'code': 'default',
                'name': 'All rights reserved',
                'organization': 'ascribe',
                'url': 'https://www.ascribe.io/faq/#legals',
            },
            'edition_number': 0,
            'bitcoin_id': 'bitcoin-id',
            'acl': [],
        },
    }
    responses.add(
        responses.POST,
        'https://www.ascribe.io/api/pieces/',
        json=json,
        status=201,
        content_type='application/json',
    )
    piece = {
        'file_url': 'https://abc.xyz/img.jpg',
        'artist_name': 'alice',
        'title': 'The green grass',
    }
    response_json = ascribe_wrapper.create_piece(piece)
    assert response_json == json


@responses.activate
def test_share_piece(ascribe_wrapper):
    json = {
        'notification': 'You have successfully shared 1 piece with alice.',
        'success': True,
    }
    responses.add(
        responses.POST,
        'https://www.ascribe.io/api/ownership/shares/pieces/',
        json=json,
        status=201,
        content_type='application/json',
    )
    data = {
        'share_emails': 'alice@wonder.lnd',
        'share_message': 'Check this out! - alice',
        'piece_id': 3,
    }
    response_json = ascribe_wrapper.share_piece(data)
    assert response_json == json
