# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# TODO: Read from remote API

languages = {
    "en": {
        "model": "neongeckocom/tts-vits-ljspeech-en@v0.4",
        "language": {
            "name": "English (US)",
            "code": "en-US",
            "gender": "female"
        },
        "sentence": "A rainbow is a meteorological phenomenon that is caused "
                    "by reflection, refraction and dispersion of light.",
    },
    "es": {
        "model": "neongeckocom/tts-vits-css10-es@v0.2",
        "language": {
            "name": "Spanish (Spain)",
            "code": "es-ES",
            "gender": "male"
        },
        "sentence": "Un arco??ris o arco iris es un fen??meno ??ptico y "
                    "meteorol??gico que consiste en la aparici??n en el cielo "
                    "de un arco de luz multicolor.",
    },
    "fr": {
        "model": "neongeckocom/tts-vits-css10-fr@v0.3", 
        "sentence": "Un arc-en-ciel est un photom??t??ore, un ph??nom??ne optique "
                    "se produisant dans le ciel, visible dans la direction "
                    "oppos??e au Soleil.",
        "language": {
            "name": "French (France)",
            "code": "fr-FR",
            "gender": "male"
        },
    },
    "de": {
        "model": "neongeckocom/tts-vits-css10-de@v0.2", 
        "sentence": "Der Regenbogen ist ein atmosph??risch-optisches Ph??nomen, "
                    "das als kreisbogenf??rmiges farbiges Lichtband in einer "
                    "von der Sonne.",
        "language": {
            "name": "German",
            "code": "de-DE",
            "gender": "female"
        },
    },
    "it": {
        "model": "neongeckocom/tts-vits-cv-it@v0.1",
        "language": {
            "name": "Italian",
            "code": "it-IT",
            "gender": "female"
        },
        "sentence": "In fisica dell'atmosfera e meteorologia, l'arcobaleno ?? "
                    "un fenomeno ottico atmosferico che produce uno spettro "
                    "quasi continuo di luce nel cielo quando la luce del Sole "
                    "attraversa le gocce d'acqua rimaste in sospensione dopo "
                    "un temporale.",
    },
    "pl": {
        "model": "neongeckocom/tts-vits-mai-pl@v0.6",
        "language": {
            "name": "Polish",
            "code": "pl-PO",
            "gender": "female"
        },
        "sentence": "T??cza, zjawisko optyczne i meteorologiczne, wyst??puj??ce "
                    "w postaci charakterystycznego wielobarwnego ??uku "
                    "powstaj??cego w wyniku rozszczepienia ??wiat??a widzialnego.",
    },
    "uk": {
        "model": "neongeckocom/tts-vits-mai-uk@v0.9",
        "language": {
            "name": "Ukrainian",
            "code": "uk-UA",
            "gender": "female"
        },
        "sentence": "??????????????, ?????????? ?????????????? ?????????????? ?????????? ?? ??????????????????, ???? "
                    "?????????? ?????????? ????????, ?????? ???? ???????????????? ?????????????????????????????? ??????, "
                    "???? ?????????????????????????????? ???? ?????? ??????????, ???????? ???????? ?????????????????????? "
                    "?????????? ??????????.",
    },
    "nl": {
        "model": "neongeckocom/tts-vits-css10-nl@v0.2",
        "language": {
            "name": "Dutch",
            "code": "nl-NL",
            "gender": "male"
        },
        "sentence": "Een regenboog is een gekleurde cirkelboog die aan de "
                    "hemel waargenomen kan worden als de, laagstaande.",
    },
    "ro": {
        "model": "neongeckocom/tts-vits-cv-ro@v0.1",
        "language": {
            "name": "Romanian",
            "code": "ro-RO",
            "gender": "female"
        },
        "sentence": "Curcubeul este un fenomen optic ??i meteorologic "
                    "atmosferic care se manifest?? prin apari??ia pe cer a unui "
                    "spectru de forma unui arc colorat atunci c??nd lumina "
                    "soarelui se refract?? ??n pic??turile de ap?? din atmosfer??.",
    },
    "hu": {
        "model": "neongeckocom/tts-vits-css10-hu@v0.1",
        "language": {
            "name": "Hungarian",
            "code": "hu-HU",
            "gender": "female"
        },
        "sentence": "A sziv??rv??ny olyan optikai jelens??g, melyet es??- vagy "
                    "p??racseppek okoznak, mikor a f??ny prizmaszer??en megt??rik "
                    "rajtuk ??s sz??neire bomlik.",
    },
    "el": {
        "model": "neongeckocom/tts-vits-cv-el@v0.1",
        "language": {
            "name": "Greek",
            "code": "el-GR",
            "gender": "female"
        },
        "sentence": "???? ?????????????? ???????? ?????????????????????? ???????? ???? ?????????????? ?????? ?????????? "
                    "?????????????? ???????????????? ???????????? ???????? ???????????????????? ?????? ?????? ?????? "
                    "?????????? ?????? ???????????????????? ?????????????????? ???????? ?????? ????????????????.",
    },
    "cs": {
        "model": "neongeckocom/tts-vits-cv-cs@v0.1",
        "language": {
            "name": "Czech",
            "code": "cs-CZ",
            "gender": "female"
        },
        "sentence": "Duha je fotometeor, projevuj??c?? se jako skupina "
                    "soust??edn??ch barevn??ch oblouk??, kter?? vznikaj?? lomem a "
                    "vnit??n??m odrazem slune??n??ho nebo m??s????n??ho sv??tla na "
                    "vodn??ch kapk??ch v atmosf????e.",
    },
    "sv": {
        "model": "neongeckocom/tts-vits-cv-sv@v0.1",
        "language": {
            "name": "Swedish",
            "code": "sv-SE",
            "gender": "female"
        },
        "sentence": "En regnb??ge ??r ett optiskt, meteorologiskt fenomen som "
                    "upptr??der som ett fullst??ndigt ljusspektrum i form av en "
                    "b??ge p?? himlen d?? solen lyser p?? nedfallande regn. "
                    "Klarast lyser regnb??gen d?? halva himlen fortfarande ??r "
                    "t??ckt med m??rka moln som avger regn och betraktaren "
                    "befinner sig under klar himmel.",
    },
    "pt": {
        "model": "neongeckocom/tts-vits-cv-pt@v0.1",
        "language": {
            "name": "Portuguese (Portugal)",
            "code": "pt-PT",
            "gender": "male"
        },
        "sentence": "Um arco-??ris ?? um fen??meno ??ptico e meteorol??gico que "
                    "separa a luz do sol em seu espectro cont??nuo quando o "
                    "sol brilha sobre got??culas de ??gua suspensas no ar.",
    },
    "bg": {
        "model": "neongeckocom/tts-vits-cv-bg@v0.1",
        "language": {
            "name": "Bulgarian",
            "code": "bg-BG",
            "gender": "female"
        },
        "sentence": "???????? ?? ?????????????? ?? ???????????????????????????? ??????????????, ???????????????? ?? "
                    "?????????????? ?? ???????????? ???? ?????????? ?????????????????????? ?????????????? ???? "
                    "????????????????????.",
    },
    "hr": {
        "model": "neongeckocom/tts-vits-cv-hr@v0.1",
        "language": {
            "name": "Hungarian",
            "code": "hr-HU",
            "gender": "female"
        },
        "sentence": "Duga je ??esta opti??ka pojava u Zemljinoj atmosferi u "
                    "obliku jednog ili vi??e obojenih kru??nih lukova, koja "
                    "nastaje jednostrukim ili vi??estrukim lomom i odbijanjem "
                    "zraka svjetlosti u kapljicama ki??e.",
    },
    "da": {
        "model": "neongeckocom/tts-vits-cv-da@v0.1",
        "language": {
            "name": "Danish",
            "code": "da-DK",
            "gender": "female"
        },
        "sentence": "En regnbue er et optisk f??nomen; en lyseffekt, som "
                    "skabes p?? himlen, n??r lys fra Solen rammer sm?? "
                    "vanddr??ber i luften, f.eks. faldende regn.",
    },
    "sk": {
        "model": "neongeckocom/tts-vits-cv-sk@v0.1",
        "language": {
            "name": "Slovak",
            "code": "sk-SK",
            "gender": "female"
        },
        "sentence": "D??ha je optick?? ??kaz vznikaj??ci v atmosf??re Zeme. Vznik "
                    "d??hy je sp??soben?? disperziou slne??n??ho svetla "
                    "prech??dzaj??ceho kvapkou.",
    },
    "fi": {
        "model": "neongeckocom/tts-vits-css10-fi@v0.1",
        "language": {
            "name": "Finnish",
            "code": "fi-FI",
            "gender": "male"
        },
        "sentence": "Sateenkaari on spektrin v??reiss?? esiintyv?? ilmakeh??n "
                    "optinen ilmi??. Se syntyy, kun valo taittuu pisaran "
                    "etupinnasta.",
    },
    "lt": {
        "model": "neongeckocom/tts-vits-cv-lt@v0.1",
        "language": {
            "name": "Lithuanian",
            "code": "lt-LT",
            "gender": "female"
        },
        "sentence": "Vaivoryk??t?? - optinis ir meteorologinis rei??kinys, "
                    "kuomet Saulei ap??vietus atmosferoje esan??ius vandens "
                    "la??elius, danguje atsiranda i??tisin?? spalv?? spektro "
                    "juosta.",
    },
    "sl": {
        "model": "neongeckocom/tts-vits-cv-sl@v0.1",
        "language": {
            "name": "Slovenian",
            "code": "sl-SI",
            "gender": "female"
        },
        "sentence": "Mavrica je svetlobni pojav v ozra??ju, ki ga vidimo v "
                    "obliki loka spektralnih barv. Nastane zaradi loma, "
                    "disperzije in odboja son??nih ??arkov v vodnih kapljicah v "
                    "zraku. Mavrica, ki nastane zaradi son??nih ??arkov, se "
                    "vedno pojavi na nasprotni strani od Sonca, tako da ima "
                    "opazovalec Sonce vedno za hrbtom.",
    },
    "lv": {
        "model": "neongeckocom/tts-vits-cv-lv@v0.1",
        "language": {
            "name": "Latvian",
            "code": "lv-LV",
            "gender": "female"
        },
        "sentence": "Varav??ksne ir optiska par??d??ba atmosf??r??, kuru rada "
                    "Saules staru lau??ana un atstaro??ana kr??to??os lietus "
                    "pilienos. T?? par??d??s iepretim Saulei uz m??ko??u fona, kad "
                    "l??st. Varav??ksnes loks p??ri debesjumam ir viens no "
                    "kr????????kajiem dabas skatiem. P??r??j??s kr??sas izvietoju????s "
                    "atbilsto??i t?? loka gammai.",
    },
    "et": {
        "model": "neongeckocom/tts-vits-cv-et@v0.1",
        "language": {
            "name": "Estonian",
            "code": "et-EE",
            "gender": "female"
        },
        "sentence": "Vikerkaare p??hjustab p??ikesekiirte eri lainepikkustel "
                    "erinev murdumine ja peegeldumine ligikaudu "
                    "kerakujulistelt vihmapiiskadelt vihmaseinal v??i "
                    "vihmapilves, kui p??ikesevalgus langeb piiskadele "
                    "vaatleja selja tagant.",
    },
    "ga": {
        "model": "neongeckocom/tts-vits-cv-ga@v0.2",
        "language": {
            "name": "Irish (Gaelic)",
            "code": "ga-IE",
            "gender": "female"
        },
        "sentence": "Do r??ir lucht na heola??ochta, is ?? solas na gr??ine ag "
                    "taitneamh ar bhraonta b??ist?? sa sp??ir faoi ndearna an "
                    "tuar ceatha. Dar linne n?? tagann ??n ngr??in ach aon "
                    "tsolais amh??in, ach n?? mar sin at??.",
    },
    "mt": {
        "model": "neongeckocom/tts-vits-cv-mt@v0.1",
        "language": {
            "name": "Maltese",
            "code": "mt-MT",
            "gender": "female"
        },
        "sentence": "Qawsalla hija fenomenu meteorolo??iku li huwa kkaw??at "
                    "minn riflessjoni, rifrazzjoni u tixrid ta 'dawl fi qtar "
                    "ta' l-ilma li jirri??ulta fi spettru ta 'dawl li jidher "
                    "fis-sema.",
    },
}

tts_config = {config['language']['code']: [
    {
        'lang': config['language']['code'],
        'display_name': f'{config["language"]["name"]}',
        'gender': config["language"]["gender"],
        'offline': True,
        'priority': 20
    }
] for config in languages.values()}
