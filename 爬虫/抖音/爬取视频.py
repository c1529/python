import requests
import execjs
import json
import os

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # cookie应该也需要处理
    'cookie': 'ttwid=1%7CVqMcHD1_f08OJWrRLT-6LhiMZ3cXa8HVquHQkrPfl8k%7C1708138458%7Cfd1c3c37ae7bdf4d6d89b385a7945470beea4a9743a4adb591789e55789166ff; passport_csrf_token=5badc617a8d71424d24ad3dd74acdae2; passport_csrf_token_default=5badc617a8d71424d24ad3dd74acdae2; bd_ticket_guard_client_web_domain=2; xgplayer_user_id=115338428258; passport_assist_user=Cj1Z-31Oe4mRthg07I1Jmvkx4SF3Es_J2aQhMiFJvlH9Z7qdiwYBRTZbmIWi2RZjeCzRdNNSSdqTHFKnmhhhGkoKPBpKpWMTS_MHbivpyFKlOdHiQXQHrArwGHKMcJBqngoTuaHha9Z-XsHurVekWopUrflqajAf88z4W-ygTBCnzskNGImv1lQgASIBA1JDvGo%3D; n_mh=ujowtLLjbHNDMWcWgiOoJthTKWFKz_u3vGYy5qsT42E; sso_uid_tt=34b156392dc2ef94ffdfb31207e58853; sso_uid_tt_ss=34b156392dc2ef94ffdfb31207e58853; toutiao_sso_user=7e5ffb68a56add54812fd53ed7006df1; toutiao_sso_user_ss=7e5ffb68a56add54812fd53ed7006df1; passport_auth_status=2859def01f9c7ab7c8060edc88ebb42a%2C; passport_auth_status_ss=2859def01f9c7ab7c8060edc88ebb42a%2C; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=f2bf476fcb7a09adb269938d40a43522; __security_server_data_status=1; store-region=cn-ln; store-region-src=uid; s_v_web_id=verify_lspm0xlg_kE6apfSO_kPRD_48V5_9RPY_B1Qs8qMjuBm8; my_rd=2; __live_version__=%221.1.1.8009%22; live_use_vvc=%22false%22; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; dy_swidth=1920; dy_sheight=1080; publish_badge_show_info=%220%2C0%2C0%2C1710393426619%22; csrf_session_id=187631e18b937fc464d7eab50b695017; strategyABtestKey=%221710393427.303%22; sid_ucp_sso_v1=1.0.0-KDllYzMxMDYxNDM0YzQ1Zjg5MGI0MGJlMDNkNDJkNTQ1YTk2NTY4ODcKHQie9bGY_wIQ1ZDKrwYY7zEgDDDo-LnbBTgGQPQHGgJsZiIgN2U1ZmZiNjhhNTZhZGQ1NDgxMmZkNTNlZDcwMDZkZjE; ssid_ucp_sso_v1=1.0.0-KDllYzMxMDYxNDM0YzQ1Zjg5MGI0MGJlMDNkNDJkNTQ1YTk2NTY4ODcKHQie9bGY_wIQ1ZDKrwYY7zEgDDDo-LnbBTgGQPQHGgJsZiIgN2U1ZmZiNjhhNTZhZGQ1NDgxMmZkNTNlZDcwMDZkZjE; sid_ucp_v1=1.0.0-KDU4OGI4ZGM2NWQ0NmJjMDg2ZjI3NDM5MDQ1YTkxMDRlMzFjMTJkOTgKGQie9bGY_wIQ1ZDKrwYY7zEgDDgGQPQHSAQaAmxxIiBhMmIxMDQ1MTI4NGE5NWQxNzJjMjJlZTZkMjUwMjllNg; ssid_ucp_v1=1.0.0-KDU4OGI4ZGM2NWQ0NmJjMDg2ZjI3NDM5MDQ1YTkxMDRlMzFjMTJkOTgKGQie9bGY_wIQ1ZDKrwYY7zEgDDgGQPQHSAQaAmxxIiBhMmIxMDQ1MTI4NGE5NWQxNzJjMjJlZTZkMjUwMjllNg; sid_guard=7e5ffb68a56add54812fd53ed7006df1%7C1710393429%7C5184001%7CMon%2C+13-May-2024+05%3A17%3A10+GMT; uid_tt=34b156392dc2ef94ffdfb31207e58853; uid_tt_ss=34b156392dc2ef94ffdfb31207e58853; sid_tt=7e5ffb68a56add54812fd53ed7006df1; sessionid=7e5ffb68a56add54812fd53ed7006df1; sessionid_ss=7e5ffb68a56add54812fd53ed7006df1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; xg_device_score=6.8699304628410225; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAx7JRrYNydaN-WN_rrN4zVIXN_PJZyJrA2ddjC3aa1kY%2F1710432000000%2F0%2F0%2F1710401095251%22; download_guide=%223%2F20240314%2F0%22; passport_fe_beating_status=true; pwa2=%220%7C0%7C3%7C0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTXQ4VEo4Uk1sdkdNdXdCRDdIbENhMDVlbTNCejJpbGQ2ZE1WcXg3aW5JMU4wZ1pDSStEZW9pWXNJRk40a056MEJRYXZXeVM2TUUxSysvTFdqdWFndVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=CiyZkOEjrmsXx6ZDyAY9-ogcr2SeltDM1cxwhReRAudpPIhmmQcSPcYei-cKQFnst4EEbNxjSE1WZNg9TGtC0_xPXZFTfC3JCN4Zdx4JGCnn9JZD2XtjsT4vw1w=; tt_scid=P1SaQYM0il1xMDZDrvdVa1jF-qgQxJLRLY7-OtQQSytvYt47Ffqbb-CQntGCwQRmd30f; home_can_add_dy_2_desktop=%220%22; odin_tt=d7c3a330b63bc53f2965637bfa9a1bf33cc10441ca5f05d1cd00384425762aa1d24cd46c671c6abbab81beb13f2bc6e3479dae5cfdd023718af86d4f1950174a; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; msToken=aaXtOdyZsLomn059MtnfMPmqQXXVqGGfMmR-fICzl_sVRGaSlZEEW7PkN5yIyCeo1AL07lODWMJht9TW5gD9dZqruaCL2MlvgLk6n0mJW6oJY_iQ7N709-munPM=; __ac_nonce=065f2aea800cff21e6141; __ac_signature=_02B4Z6wo00f01NWHpsAAAIDB36F9aMqwD3DVp6JAAFCYgowOO.R8I.CnBb8vhGSTfAmSKo2HJMnlZBhqbfLhBpTzTRQIF9kj0Don62ueaiuQsMl2cbq-bE3fUIIZ-l.dOcGmtQtvpoYLqqByd5; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A2.95%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22',
    # 用户主页地址
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAwAtMzv5ELHT-qxga5avkrQo_62sQF1WSQ9FWVF-Bhlo?vid=7344674715815939379',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}
user_id = 'MS4wLjABAAAAlPZ_iWnigiNMeX2gzrLjz_sl0vr6AomKc_SyLZCfQms'
max_cursor = '0'
need_time_list = '1'
with open('xbogs.js', 'r') as file:
    js = file.read()
js_compile = execjs.compile(js)
path = 'D:\\PycharmProjects\\douyin\\我的喜欢'
def download_video(video_url,video_name,path):
    response = requests.get(video_url, headers=headers).content
    with open(f'{path}\\{video_name}.mp4', 'wb') as f:
        f.write(response)

def get_video(user_id,max_cursor,need_time_list,path):
    params = (f'device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={user_id}'
              f'&max_cursor={max_cursor}&locate_item_id=7344674715815939379&locate_query=false'
              f'&show_live_replay_strategy=1&need_time_list={need_time_list}&time_list_query=0&whale_cut_token=&cut_version=1&count=18'
              '&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled'
              '=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name'
              '=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name'
              '=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=2.95&effective_type=4g'
              '&round_trip_time=50&webid=7336398739394790923&msToken=aaXtOdyZsLomn059MtnfMPmqQXXVqGGfMmR'
              '-fICzl_sVRGaSlZEEW7PkN5yIyCeo1AL07lODWMJht9TW5gD9dZqruaCL2MlvgLk6n0mJW6oJY_iQ7N709-munPM=&')
    base_url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?'
    x_b = js_compile.call("window.xbogs", params)
    url = base_url + params + '&X-Bogus=' + x_b
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    max_cursor = result['max_cursor']
    aweme_list = result['aweme_list']
    for i in aweme_list:
        title = i['desc']
        if '\n' in title:
            return title.split('\n')[0]
        video_url = i['video']['play_addr']['url_list'][0]
        try:
            download_video(video_url, title, path)
        except Exception as e:
            print(e)
    return max_cursor


for i in range(1,20):
    try:
        max_cursor = get_video(user_id, max_cursor, need_time_list, path)
    except Exception as e:
        print(e)
    print(f'你已经获取{i*20}个视频')


