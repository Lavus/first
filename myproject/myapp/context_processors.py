import cloudinary
def consts(request):
    return dict(
        ICON_EFFECTS = dict(
            format="png",
            type="facebook",
            transformation=[
                dict(height=95, width=95, crop="thumb", gravity="face", effect="sepia", radius=20),
                dict(angle=10),
            ]
        ),
        THUMBNAIL = {
            "format": "jpg", "crop": "fill", "height": 300, "width": 300,
        },
        DEPOTHUMBNAIL = {
            "format": "jpg", "crop": "fill", "radius":"max", "height": 300, "width": 300,
        },
        SLIDE = {
            "class": "thumbnail inline", "format": "jpg", "crop": "pad", "height": 1200, "width": 1920,
        },
        MINISLIDE = {
            "class": "thumbnail inline", "format": "jpg", "crop": "pad", "height": 565, "width": 565,
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
