def ready():
    # from geocoder import model_signals
    try:
        from django.core import serializers
        # from geocoder.zip_search_3d import getSingletonZipSearch
        with open('blah.json', 'r') as json_file:
            serialized = json_file.read()
        obj_generator = serializers.json.Deserializer(serialized)  # change this line.
        zips = []
        for zip in obj_generator:
            zips.append(zip.object)
        # getSingletonZipSearch(zips)
        # logger.info('loaded zips from json file')
    except Exception as ex:
        # logger.warning('loading zips from database')
        print('lol')


ready()
