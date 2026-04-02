import utils

top_comment = """
// bwaa skin made by guhw
// https://github.com/gustwindy/guhw-bwaa-skin
// ^ fork this if you want to have an easier time editing
//
// variant: {variant}

"""

fallback = {
    "General": {
        "Name": "z~◊《 Bwaa 》~ {variant} ~《 guhws skin 》~ ◊~z",
        "Author": "guhw",
        "Version": 2.7,
        "CursorRotate": 0,
        "CursorExpand": 0,
        "CursorCentre": 1,
        "CursorTrailRotate": 0,

        "SliderStyle": 2,
        "SliderBallFlip": 0,
        "SliderBallFrames": 1,

        "HitCircleOverlayAboveNumber": 1,
        "SpinnerFadePlayfield": 0,
        "AllowSliderBallTint": 0,
        "AnimationFramrate": 24
    },
    "Colours": {
        "SongSelectActiveText": "#FFFFFF",
        "InputOverlayText": "#FFFFFF",

        "SliderBorder": "#000000",
        "SliderTrackOverride": "#000000",
        "MenuGlow": "#FFFFFF"
    },
    "Fonts": {
        "HitCirclePrefix": "default",
        "HitCircleOverlap": 160,
        "ScorePrefix": "score",
        "ComboPrefix": "score",
        "ScoreOverlap": 4,
        "ComboOverlap": 4,
    }
}

variants = {
    "default": {
        "General": {
            #"CursorExpand": 1,
        },
        "Colours": {
            "Combo1": "#96E6FF",
            "Combo2": "#FF7DB1",
            "Combo3": "#82FFA0",
            "SliderBorder": "#FBE9FF",
            "SliderTrackOverride": "#2B292C"
        },
        "Fonts": {
            "HitCircleOverlap": 4
        }
    },
    "performance": {
        "Colours": {
            "Combo1": "#FFFFFF"
        }
    }
}

def build(variant):
    current = fallback.copy()
    target = variants[variant]
    
    for cat,tab in target.items():
        for k,v in tab.items():
            current[cat][k] = v
    
    ini = top_comment.replace("{variant}",variant)
    
    for cat,tab in current.items():
        ini += f"\n\n[{cat}]"
        for k,v in tab.items():
            v = str(v)
            if v.startswith("#"):
                v = ",".join(str(i) for i in utils.hex_to_rgb(v))
            ini += f"\n{k}: {v}"
    
    with open("build/skin.ini","w+") as f:
        f.write(ini)