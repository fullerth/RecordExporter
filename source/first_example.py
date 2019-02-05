import discogs_client

d = discogs_client.Client('ExampleApplication/0.1', user_token="aUrgiZwwAlcixXEFWYMARymQJYMQcmLXlqJBJcZy")

me = d.identity()

test_release = me.collection_folders[0].releases[0]

import pdb;pdb.set_trace();


