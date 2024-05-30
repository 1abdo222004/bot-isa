import requests

cookies = {
    'uuid': '7f7f6b65-ffca-4fba-a4b7-9dcd3bf10f20',
    '_ga': 'GA1.1.1793510034.1717015922',
    'fpestid': 'K-1y9C66KOh1Pw0S6mp31WxkqWGvLlbhyAAjznIciTTWyPUmcUkNsfY34mszbYeTycabgw',
    'cf_clearance': 'lxzfw7jwHJTS4VU2Wf_nIshdSXAeaTCEW_ePCstQ.4U-1717015924-1.0.1.1-buXYjSYT19.W6djNYtLLmJ2LaU1xjDuLWO.2oo4nKNGOsOOZAIp9iJTn2b0aITcQYpx_vvE05kxEC.hlG1zlqA',
    '_clck': 'k7n602%7C2%7Cfm6%7C0%7C1610',
    '__gads': 'ID=5179a8a8fa7e1c39:T=1717015928:RT=1717015928:S=ALNI_MaZOUCBb106PChnvMBkC3A2WJNVfQ',
    '__gpi': 'UID=00000e33f0b4bcff:T=1717015928:RT=1717015928:S=ALNI_MaiVm13-UNQv-yLfYdwxZfOuu-Kkw',
    '__eoi': 'ID=f19abb4923d33c9a:T=1717015928:RT=1717015928:S=AA-AfjbznoQNqIBZNSRyzbHMnJtS',
    '_ga_MXNCR42D3E': 'GS1.1.1717015921.1.1.1717015982.0.0.0',
    '_clsk': 'supipw%7C1717015990993%7C2%7C1%7Cw.clarity.ms%2Fcollect',
    'FCNEC': '%5B%5B%22AKsRol-XHwQaoVQVCmbyQhcNIXm2kHelOwgJMYTjhfO527n79jVC4CYpliw8LrThWoQYjYJfjlMT6tRj2UC_bkg2DLiCJMbmCFXk28YKkyhWXVb9LwNAWuGQrbi5L0aJPVTZM1-KmIAQUHtdUrJBTKw860VSJ-jJMA%3D%3D%22%5D%5D',
}

headers = {
    'authority': 'ttsmaker.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'uuid=7f7f6b65-ffca-4fba-a4b7-9dcd3bf10f20; _ga=GA1.1.1793510034.1717015922; fpestid=K-1y9C66KOh1Pw0S6mp31WxkqWGvLlbhyAAjznIciTTWyPUmcUkNsfY34mszbYeTycabgw; cf_clearance=lxzfw7jwHJTS4VU2Wf_nIshdSXAeaTCEW_ePCstQ.4U-1717015924-1.0.1.1-buXYjSYT19.W6djNYtLLmJ2LaU1xjDuLWO.2oo4nKNGOsOOZAIp9iJTn2b0aITcQYpx_vvE05kxEC.hlG1zlqA; _clck=k7n602%7C2%7Cfm6%7C0%7C1610; __gads=ID=5179a8a8fa7e1c39:T=1717015928:RT=1717015928:S=ALNI_MaZOUCBb106PChnvMBkC3A2WJNVfQ; __gpi=UID=00000e33f0b4bcff:T=1717015928:RT=1717015928:S=ALNI_MaiVm13-UNQv-yLfYdwxZfOuu-Kkw; __eoi=ID=f19abb4923d33c9a:T=1717015928:RT=1717015928:S=AA-AfjbznoQNqIBZNSRyzbHMnJtS; _ga_MXNCR42D3E=GS1.1.1717015921.1.1.1717015982.0.0.0; _clsk=supipw%7C1717015990993%7C2%7C1%7Cw.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol-XHwQaoVQVCmbyQhcNIXm2kHelOwgJMYTjhfO527n79jVC4CYpliw8LrThWoQYjYJfjlMT6tRj2UC_bkg2DLiCJMbmCFXk28YKkyhWXVb9LwNAWuGQrbi5L0aJPVTZM1-KmIAQUHtdUrJBTKw860VSJ-jJMA%3D%3D%22%5D%5D',
    'origin': 'https://ttsmaker.com',
    'referer': 'https://ttsmaker.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = '{"user_uuid_text":"7f7f6b65-ffca-4fba-a4b7-9dcd3bf10f20","user_input_text":"hi","user_select_language_id":"en-us","user_select_announcer_id":"148","user_select_tts_setting_audio_format":"mp3","user_select_tts_setting_speed":"1.0","user_select_tts_setting_volume":"1","user_select_tts_setting_pitch":"1","user_input_captcha_text":"3265","user_input_captcha_key":"ey8MAK","user_input_paragraph_pause_time":"0","user_select_tts_voice_high_quality":"0","user_bgm_config":{}}'

response = requests.post('https://ttsmaker.com/api/create-tts-order', cookies=cookies, headers=headers, data=data).text
print(response)