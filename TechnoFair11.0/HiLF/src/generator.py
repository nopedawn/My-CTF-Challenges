import random
import datetime
import ipaddress
import pytz

def genrandip():
    ip = ipaddress.IPv4Address(random.randint(0x01000000, 0xFFFFFFFF))
    while ip.is_private or ip.is_multicast or ip.is_reserved or ip.is_unspecified or ip.is_loopback:
        ip = ipaddress.IPv4Address(random.randint(0x01000000, 0xFFFFFFFF))
    return str(ip)

def generate_timestamps(start_time, lines_count):
    tz = pytz.timezone('Asia/Jakarta')
    timestamps = []
    for _ in range(lines_count):
        days_increment = random.randint(0, 2)
        hours_increment = random.randint(0, 23)
        minutes_increment = random.randint(0, 59)
        seconds_increment = random.randint(0, 59)

        increment = datetime.timedelta(days=days_increment,
                                       hours=hours_increment,
                                       minutes=minutes_increment,
                                       seconds=seconds_increment)
        
        current_time = start_time + increment
        current_time = tz.localize(current_time)
        timestamps.append(current_time)
    
    return sorted(timestamps)

def genlogline(timestamp, hid_parts, index, special_index):
    common_urls = [
        "http://example.com", "https://amazon.com", "https://www.google.com", "https://facebook.com", "https://cnn.com/us", "https://www.blogger.com", "https://www.youtube.com", "https://apple.com", "https://linkedin.com", "https://wordpress.org", "https://googleusercontent.com", "https://cloudflare.com", "https://support.google.com", "https://play.google.com", "https://docs.google.com", "https://microsoft.com", "https://maps.google.com", "https://en.wikipedia.org", "https://whatsapp.com", "https://t.me", "https://accounts.google.com", "https://mozilla.org", "https://europa.eu", "https://sites.google.com", "https://adobe.com", "https://github.com", "https://vk.com", "https://creativecommons.org", "https://dailymotion.com", "https://istockphoto.com", "https://who.int", "https://developers.google.com", "https://w3.org", "https://medium.com", "https://www.yahoo.com", "https://cpanel.net", "https://gravatar.com", "scribd.com", "wp.com", "issuu.com", "independent.co.uk", "www.wix.com", "https://nginx.org", "nginx.org", "https://nasa.gov", "nasa.gov", "https://website.com", "website.com", "https://ctftime.org", "ctftime.org",
        "http://example.org", "http://example.net", "http://example.edu", "http://example.biz", "http://example.info", "http://example.us", "http://example.mobi", "http://example.name", "http://example.pro", "http://example.xxx", "http://example.tv", "http://example.co", "http://example.io", "http://example.me", "sanangelolive.com", "iherb.com", "sina.com", "sunglasshut.com", "steamcommunity.com", "slideplayer.com", "store.steampowered.com", "customerportal.sandiego.gov", "esvt.viasat.com", "library.sdsu.edu", "pool--4-74-3.phlapa.fios.verizon.net", "selectblinds.com", "gluecksspirale.spiegel.de", "velocitypayment.com", "juniper.net", "jmu.edu", "sandisk.com", "supply.comaccess.sdmts.com", "onlinedegrees.sandiego.edu", "icicibank.co", "blacklib969.swarthmore.edu", "eproptax.saccounty.net", "idastream.idahopower.com", "sfmta.com", "scu.edu", "careers.scripps.org", "vacationexpress.com", "asia.sega.com", "smallerliving.orgsiliconangle.com", "kan.sogou.com", "sage.com", "srs.sandiegocounty.gov", "prevalence.spectrumnews.org", "insurancenewsnet.com", "fr.vwr.co", "archivesspace.smith.edu", "infoweb.itsmarta.com", "idealimage.com",
    ]

    paths = [
        "/favicon.ico", "/dashboard/login", "/dashboard/logout", "/post", "/humans.txt", "/publishing.xml", "/reading.xml", "/robots.txt", "/security.txt", "/sitemap.xml", "/home", "/about", "/ideas", "/intractable", "/now", "/purpose", "/wish", "/%", "/", "/?", "/?=", "/id", "/../", "/../../", "/%20", "/%6553", "/%1337", "/%20curl%20-v%20google.com", "/%20ping%20google.com"
    ]

    methods = ["GET", "POST"]
    status_codes = [200, 404, 500, 301, 302]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0",
        "Lynx/2.8.9dev.8 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/3.4.9",
        "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
        "AppleTV11,1/11.1",
        ""
    ]

    url = random.choice(common_urls)
    method = random.choice(methods)
    path = random.choice(paths)
    status_code = random.choice(status_codes)
    user_agent = random.choice(user_agents)
    formatted_time = timestamp.strftime('%d/%b/%Y:%H:%M:%S %z')
    ip_address = genrandip()

    if index in hid_parts:
        path = hid_parts[index]
    elif index == special_index:
        path = "/%20ssh%20-i%20id_rsa%20leus@103.185.53.181%20-p%207151"

    log_line = f'{ip_address}\t - - [{formatted_time}] "{method} {path} HTTP/1.1" {status_code} "{url}" - "{user_agent}"'
    return log_line

def genlogfile(filename, lines_count=29674):
    hid_val = "/%68 /%74 /%74 /%70 /%73 /%3a /%2f /%2f /%6d /%65 /%67 /%61 /%2e /%6e /%7a /%2f /%66 /%69 /%6c /%65 /%2f /%55 /%79 /%70 /%6b /%7a /%51 /%44 /%53 /%23 /%38 /%59 /%6a /%5f /%50 /%58 /%69 /%74 /%32 /%4f /%6e /%4b /%55 /%78 /%38 /%6b /%66 /%56 /%6f /%68 /%78 /%4f /%76 /%6b /%51 /%69 /%68 /%56 /%74 /%36 /%55 /%63 /%41 /%76 /%4b /%5a /%41 /%35 /%32 /%42 /%69 /%65 /%63"
    hid_parts_indices = sorted(random.sample(range(lines_count), len(hid_val.split())))
    hid_parts = {i: part for i, part in zip(hid_parts_indices, hid_val.split())}

    special_index = random.randint(0, lines_count - 1)

    start_time = datetime.datetime.now()
    timestamps = generate_timestamps(start_time, lines_count)

    with open(filename, 'w') as f:
        for i, timestamp in enumerate(timestamps):
            log_line = genlogline(timestamp, hid_parts, i, special_index)
            f.write(log_line + '\n')

genlogfile('../release/chall/access.log')