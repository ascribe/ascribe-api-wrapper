ascribe SPOOL API Python Wrapper
================================

This is a communauty-based python wrapper around the `ascribe ownership REST
API <http://docs.ascribe.apiary.io>`_.


Installation
------------

.. code-block:: python

    pip install ascribe


Usage Example: Registering a Piece
----------------------------------

.. code-block:: python
    
    >>> from ascribe import AscribeWrapper
    >>> ascribe_wrapper = AscribeWrapper('your-token')
    >>> piece = {
        'file_url': 'https://s3.eu-central-1.amazonaws.com/bucket/img.jpg',
        'artist_name': 'mystery',
        'title': 'universe',
    }
    >>> ascribe_wrapper.create_piece(piece)
    {'piece': {
        'artist_name': 'mystery',
        'bitcoin_id': 'bitcoin-id',
        'date_created': '2015-01-01',
        'datetime_registered': '2015-11-28T20:42:19.917896Z',
        'license_type': {
            'code': 'default',
            'name': 'All rights reserved',
            'organization': 'ascribe',
            'url': 'https://www.ascribe.io/faq/#legals'
        },
        'title': 'universe',
        'user_registered': 'mystery'
        ...
        ...
    }}


Documentation
-------------

https://ascribe.readthedocs.org
