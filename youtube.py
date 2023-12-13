import requests

def youtubeDownloader(link):
    url = "https://youtube86.p.rapidapi.com/api/youtube/links"

    payload = { "url": link }
    headers = {
        "content-type": "application/json",
        "X-Forwarded-For": "70.41.3.18",
        "X-RapidAPI-Key": "166dbbdddemsh19c386e1d2d8066p100816jsnc5126b1f27a5",
        "X-RapidAPI-Host": "youtube86.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    video_dict = {}
    try:
        data = response.json()
        video_dict["urls"] = data['urls']
        for i in data['meta']:
            video_dict['title'] = i.get('title')
            video_dict['duration'] = i.get('duration')
        video_dict['videoQuality'] = data.get('videoQuality')
        return video_dict
    except:
        return 'error'



# [
#   {
#     "resourceId": "a9LDPn-MO4I",
#     "urls": [
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=17&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2F3gpp&gir=yes&clen=620190&dur=60.418&lmt=1394357177132150&mt=1701622872&fvip=5&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIhAI_kKjINNr1G771tUZIRDD1_nhsXiAZXtqIRNMHsPcLxAiAHVD0DDjNPNQ4c5X8cfQb6K5Iow0GV3GqRZkaiVkCBag%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "3GP",
#         "subName": "144",
#         "extension": "3gp",
#         "quality": "144",
#         "qualityNumber": 144,
#         "audio": false,
#         "itag": "17",
#         "filesize": 620190,
#         "isBundle": true
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=60.046&lmt=1664358444745901&mt=1701622872&fvip=5&fexp=24007246&c=ANDROID&txp=1438434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=ANLwegAwRQIhALiEid0BDZNcBzSvHRqjkVNfhDMW6U1fSFRjH6Ko4DQ2AiAyMyc5jrknUtXBA6N6qvOvzhaaRon8zF3aT1ISv7_uwg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D&title=UHDTV%20TEST%208K%20VIDEO.mp4",
#         "name": "MP4",
#         "subName": "360",
#         "extension": "mp4",
#         "quality": "360",
#         "qualityNumber": 360,
#         "audio": false,
#         "itag": "18",
#         "videoCodec": "avc1",
#         "audioCodec": "mp4a",
#         "isBundle": true
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=60.046&lmt=1471147739243075&mt=1701622872&fvip=5&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=ANLwegAwRQIgXUGgnl10lfzha6oOl_fYnX3o-Gx4UcPTUPevL18UNiQCIQCcaRTIXUs5_7QSE6Ev4PrtjcBRNE-oGtxjLox3bLepOA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D&title=UHDTV%20TEST%208K%20VIDEO.mp4",
#         "name": "MP4",
#         "subName": "720",
#         "extension": "mp4",
#         "quality": "720",
#         "qualityNumber": 720,
#         "audio": false,
#         "itag": "22",
#         "videoCodec": "avc1",
#         "audioCodec": "mp4a",
#         "isBundle": true
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=134&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=3312395&dur=60.000&lmt=1429588265946044&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgbCRQgF3ZDF48Eyqxf43qMChD5_scxyHm1hj1_XOyk4wCIQCqAaC0E356tVvu6_UQ02XbIy5EaZq_iN7c5CoL1HLWHA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "MP4",
#         "subName": "360",
#         "extension": "mp4",
#         "quality": "360",
#         "qualityNumber": 360,
#         "audio": false,
#         "itag": "134",
#         "filesize": 3312395,
#         "contentLength": 3312395,
#         "videoCodec": "avc1",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=135&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=6742544&dur=60.000&lmt=1429588282217465&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRAIgZfJe3y7YpBGB0F8y8lmnVjAxdua2OKL2VsrveQOhOW8CIBSdRTF15XEiXdSs6f09N4El5SBSkR2_RwdYNWRdSPIH&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "MP4",
#         "subName": "480",
#         "extension": "mp4",
#         "quality": "480",
#         "qualityNumber": 480,
#         "audio": false,
#         "itag": "135",
#         "filesize": 6742544,
#         "contentLength": 6742544,
#         "videoCodec": "avc1",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=136&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=12980989&dur=60.000&lmt=1429588467133981&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgfdLSZB6xJbXRQ3v-zeXtsCub0DkvD_ZM6HcaxE5F-NACIQDqXj4A-p_fJual2RMmY3TxPIAvSe966GVvJ401-Qzuyg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "MP4",
#         "subName": "720",
#         "extension": "mp4",
#         "quality": "720",
#         "qualityNumber": 720,
#         "audio": false,
#         "itag": "136",
#         "filesize": 12980989,
#         "contentLength": 12980989,
#         "videoCodec": "avc1",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=137&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=23357226&dur=60.000&lmt=1429588423245678&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIhANWAbJ6Jo4ah_Cf9zc7UyuXObJ3nSWi68qVHlpCpkLftAiBEngOGFUPzpvHODshU4Dsi5OF4VthaYZa8gvT0cNQCjg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "MP4",
#         "subName": "1080",
#         "extension": "mp4",
#         "quality": "1080",
#         "qualityNumber": 1080,
#         "audio": false,
#         "itag": "137",
#         "filesize": 23357226,
#         "contentLength": 23357226,
#         "videoCodec": "avc1",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=139&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=363506&dur=60.139&lmt=1429588232663902&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgeTtLYnLSxaGYKEqCeachfD5cIXmYeMoyJwy6MxT1MAQCIQDAyw8ijpOJrvbc5XkVazvfAXIrPPlMAwyisQ8XG2QC8w%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "Audio M4A",
#         "subName": "53",
#         "extension": "m4a",
#         "quality": "53",
#         "qualityNumber": 53,
#         "audio": true,
#         "itag": "139",
#         "filesize": 363506,
#         "contentLength": 363506,
#         "audioCodec": "mp4a",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=964710&dur=60.046&lmt=1429588232985407&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRAIgYrnYR484sSpucY3qnYScn-tFMwusKxNeyyhuwIpC7L0CIGBcqiNSvg8K_gSeFcE-a0a0S7zF9IDt_P7m6OTS9rvo&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "Audio M4A",
#         "subName": "146",
#         "extension": "m4a",
#         "quality": "146",
#         "qualityNumber": 146,
#         "audio": true,
#         "itag": "140",
#         "filesize": 964710,
#         "contentLength": 964710,
#         "audioCodec": "mp4a",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=243&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2896796&dur=60.000&lmt=1543753346930186&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgTldqQ0PZ_6nVtkKoeaMLrofsnqU-RxU6tDwV1xfb4SkCIQCiee0t5CfdTbdH_uM4YuvV_KOadhkyDTUfnDgFfJRT5Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "WEBM",
#         "subName": "360",
#         "extension": "webm",
#         "quality": "360",
#         "qualityNumber": 360,
#         "audio": false,
#         "itag": "243",
#         "filesize": 2896796,
#         "contentLength": 2896796,
#         "videoCodec": "vp9",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=244&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=5320416&dur=60.000&lmt=1543753346952197&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIhAJ-jcPZXZhjsC77dnZVayHj-LmjZ5LgtB6vUBMQK0HUsAiBKCFLPGjnnzBw2icX7oO2cHO8zEHtDKEEETphYaDvWzg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "WEBM",
#         "subName": "480",
#         "extension": "webm",
#         "quality": "480",
#         "qualityNumber": 480,
#         "audio": false,
#         "itag": "244",
#         "filesize": 5320416,
#         "contentLength": 5320416,
#         "videoCodec": "vp9",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=247&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=10880214&dur=60.000&lmt=1543753347008399&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgFSCelCljfcoLY-218b0znVj7fymaQG1WgvGMhpyvY4gCIQD_w-EiSD79_RxTxU9sifZVgfh_LaZrXtBS4ftCEs1saQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "WEBM",
#         "subName": "720",
#         "extension": "webm",
#         "quality": "720",
#         "qualityNumber": 720,
#         "audio": false,
#         "itag": "247",
#         "filesize": 10880214,
#         "contentLength": 10880214,
#         "videoCodec": "vp9",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=248&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=19325967&dur=60.000&lmt=1543752590580967&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRgIhAIgag2drVkBazToTTJxPvpaYTVmVJYQAMnRtRY3OitMkAiEAjKLAVOccsaGSwInbV47iW4nvF5rIJmLJrRvHvSYwh_o%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "WEBM",
#         "subName": "1080",
#         "extension": "webm",
#         "quality": "1080",
#         "qualityNumber": 1080,
#         "audio": false,
#         "itag": "248",
#         "filesize": 19325967,
#         "contentLength": 19325967,
#         "videoCodec": "vp9",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=249&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=27510&dur=60.001&lmt=1473044330757461&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRgIhAIpcVvAfz0edp3gxXYc_obL2UfBs_8MxNC4rIAVELWw7AiEAoZ2lFsOJNm1vrQ9OGDAV6j5vwi6wI-xcHCEUAQ-itcI%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "Audio OPUS",
#         "subName": "4",
#         "extension": "opus",
#         "quality": "4",
#         "qualityNumber": 4,
#         "audio": true,
#         "itag": "249",
#         "filesize": 27510,
#         "contentLength": 27510,
#         "audioCodec": "opus",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=250&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=27510&dur=60.001&lmt=1473044330081627&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgRI_SbJ9ouXkWy1muPD7XYP1RyAKSNpGmhgrbAsXH5MACIQCNPwQwtYWIObKVkKKq7dSgUGnodDry2I1D8E0RgorM9Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "Audio OPUS",
#         "subName": "4",
#         "extension": "opus",
#         "quality": "4",
#         "qualityNumber": 4,
#         "audio": true,
#         "itag": "250",
#         "filesize": 27510,
#         "contentLength": 27510,
#         "audioCodec": "opus",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=27510&dur=60.001&lmt=1473044330741546&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRgIhAKBIvXUDlOd2prTr6_EVeSYCYNF4UKwu8ne525jEj4VYAiEA-06f95wtsh_9pyPPnlV7ZwjoyR1kOF--jyMV2pheWQY%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "Audio OPUS",
#         "subName": "4",
#         "extension": "opus",
#         "quality": "4",
#         "qualityNumber": 4,
#         "audio": true,
#         "itag": "251",
#         "filesize": 27510,
#         "contentLength": 27510,
#         "audioCodec": "opus",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=271&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55989644&dur=60.000&lmt=1543752754526824&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRAIgA_FAQqJFkCLU1EpPLAi-nK9cPyGDyI1mac03O8UuGqkCIB6RCipE_ViHoAZQ4PRItrcAZhuYEusZz-hmqjFnR49z&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "WEBM",
#         "subName": "1440",
#         "extension": "webm",
#         "quality": "1440",
#         "qualityNumber": 1440,
#         "audio": false,
#         "itag": "271",
#         "filesize": 55989644,
#         "contentLength": 55989644,
#         "videoCodec": "vp9",
#         "isBundle": false
#       },
#       {
#         "url": "https://rr4---sn-ab5sznzl.googlevideo.com/videoplayback?expire=1701644974&ei=TrZsZfWBNo-O_9EP6bSaaA&ip=64.43.111.77&id=o-AN1Ay06gsK_qCq5mlynWbQO_2cSenXeky8iVQcGYpopL&itag=313&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=1F&mm=31%2C29&mn=sn-ab5sznzl%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=29443750&spc=UWF9f65mkw_BG-_wkWSsKSbujcZgal8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=123687889&dur=60.000&lmt=1543753097350319&mt=1701622872&fvip=5&keepalive=yes&fexp=24007246&c=ANDROID&txp=5432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIhALOw5sGIZHynD1sRBusp6OEz16O9EaCmilknT1S4XhIgAiAje1Ih_IGHeZeZ1uVVK56n1xCVctxLvN5OY9w60atolw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRgIhAKizjOQyMZIcBvpggDo3wSnx6VTbnFzHjI-ESbLoi2p0AiEAzAzjZjj9VaEFf3QoLBeBIptVHJgsEZnfrZTDwX-kExs%3D",
#         "name": "WEBM",
#         "subName": "2160",
#         "extension": "webm",
#         "quality": "2160",
#         "qualityNumber": 2160,
#         "audio": false,
#         "itag": "313",
#         "filesize": 123687889,
#         "contentLength": 123687889,
#         "videoCodec": "vp9",
#         "isBundle": false
#       }
#     ],
#     "meta": {
#       "title": "UHDTV TEST 8K VIDEO.mp4",
#       "sourceUrl": "https://www.youtube.com/watch?v=a9LDPn-MO4I",
#       "duration": "1:00",
#       "tags": "8K,VIDEO,UHD,SUPER,HI-VISION,ULTRA,HIGH,DEFINITION"
#     },
#     "pictureUrl": "https://i.ytimg.com/vi/a9LDPn-MO4I/hqdefault.jpg",
#     "videoQuality": [
#       "2160",
#       "1440",
#       "1080",
#       "720",
#       "480",
#       "360",
#       "240",
#       "144"
#     ],
#     "service": "youtube.com"
#   }
# ]