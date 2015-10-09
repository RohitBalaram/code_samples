import math


def geo_json_builder(data):
    geo_json = {"type": "FeatureCollection", "features": []}
    first = True
    current = 0
    length = len(data)
    
    color_map = [('#000205', .4), ('#02142a', .45), 
                 ('#052550', .45), ('#073675', .5),
                 ('#09479a', .55), ('#0b58bf', .6), 
                 ('#0d69e4', .6)]
                 
    max_count = data[0][6]
    min_count = data[0][5]
    count_range = abs(min_count - max_count)
    color_interval = count_range/len(color_map)
    total = data[0][7]

    for i, x in enumerate(data):

        cur_count = int(math.ceil((x[2]-min_count)/float(color_interval)))
        if cur_count > len(color_map):
            cur_count = len(color_map)

        if first:
            color = color_map[cur_count-1]
            if x[2] == min_count:
                color = color_map[0]
            feature = {
                "type": "Feature",
                "properties": {
                    "nta": x[0],
                    "neighborhood": x[1],
                    "Count": x[2],
                    "fillColor": color[0],
                    "fillOpacity": color[1],
                    "percentage": str(int(x[2]/float(total) * 100)) + '%'

                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [float(x[3]), float(x[4])]
                        ]
                    ]
                }
            }
            geo_json["features"].append(feature)
            first = False

        else:
            geo_json["features"][current]["geometry"]["coordinates"][0].append([float(x[3]), float(x[4])])
            if i != length - 1:
                if data[i+1][0] != x[0]:
                    first = True
                    current += 1
            else:
                return geo_json
