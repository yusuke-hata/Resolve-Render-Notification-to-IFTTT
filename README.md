# Resolve-Render-Notification-to-IFTTT
Notification to IFTTT Webhooks, and is triggered after DaVinci Resolve rendering is completed

* Japanese: https://note.com/yusukehata/n/n9679e19c7e5c



This trigger is tested on the following environment.

https://github.com/yusuke-hata/Resolve-Render-Notification-to-IFTTT/blob/main/Tested_Environment.txt

_Python 3.6.8_

Install python 3.6.8 first, then install "requests" in commend line tools

<code>pip3 install requests</code>

<h2>Getting your key</h2>

Obtain your IFTTT webhook key from your IFTTT mypage, then input it on <code>{your_key} </code>

1. Open IFTTT
2. Open <b>My Services/Webhooks</b>, then open <b>"Documentation"</b>
3. Copy "your key"
4. Also ensure to type <code>"Resolve_Render_Job"</code> event name on <code>{event}</code> section

<img width="1552" alt="Screen Shot 2022-01-18 at 18 51 36" src="https://user-images.githubusercontent.com/547701/149913809-01c05588-9c5f-4c3d-b109-791f6eddc046.png">

<h2>Setup Webhooks trigger on IFTTT</h2>

1. Create your own applet. Choose <b>"Webhooks"</b>
2. Select <b>"Receive a web request"</b>
3. Input <code>"Resolve_Render_Job"</code> in Event name
4. Press <b>"create trigger"</b>

<img width="1552" alt="Screen Shot 2022-01-18 at 18 56 50" src="https://user-images.githubusercontent.com/547701/149914925-23d71f94-d8c0-448b-9081-decbdaf3ffb0.png">



<h2>Usage</h2>

1. In Resolve, open the <b>Deliver</b> page and open the <b>Render settings</b> panel
2. Click the <b>Video</b> tab, then open <b>Advanced Settings</b> and scroll down to the bottom
3. Check the checkbox for <b>Trigger script at __ of render job</b>
4. Choose <code>END</code> of render job
5. Choose the script you want to run

<img width="439" alt="Screen Shot 2022-01-18 at 19 20 43" src="https://user-images.githubusercontent.com/547701/149918614-2d100a71-89e7-41e6-b819-6900889d0dac.png">

