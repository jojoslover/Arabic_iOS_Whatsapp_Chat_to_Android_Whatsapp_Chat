# Arabic_iOS_Whatsapp_Chat_to_Android_Whatsapp_Chat
WhatsApp Arabic Chat Formatter &amp; Attachment Normalizer - اعادة ترميز وتنسيق المحادثات لجعلها مقروءة في تطبيقات قراءة المحادثات المستخرجة
This Python script converts Arabic WhatsApp chat exports into a clean, standardized format that is compatible with common WhatsApp chat parsers and archive tools.

It is specifically designed to handle Arabic WhatsApp exports, which contain hidden RTL (Right-To-Left) characters that often break standard parsers.

### Features
<ol>
  <li>✅ Supports Arabic WhatsApp chat exports</li>
  <li>✅ Removes hidden RTL control characters (\u200e, \u200f, \u202a, etc.)</li>
  <li>✅ Converts timestamps to 24-hour format with seconds</li>
  <li>✅ Normalizes dates to DD.MM.YY</li>
  <li>✅ Correctly detects and formats attachments</li>
  <li>✅ Supports images, audio, video, and any file type</li>
  <li>✅ Preserves multi-line messages</li>
  <li>✅ Produces output compatible with tools like whatsapp-chat-parser</li>
</ol>


### Attachment Formatting
Arabic WhatsApp attachments such as:<br/>
`<المُرفق: 00000002-VIDEO-2019-06-20-16-01-42.opus>`

<br/>are automatically converted to:<br/>
`[20.06.19, 16:01:42] Name: <attached: 00000002-VIDEO-2019-06-20-16-01-42.opus>`


### Why This Exists
Most WhatsApp chat parsers fail with Arabic exports due to:
<ol>
<li>Hidden RTL characters</li>
<li>Arabic punctuation (،)</li>
<li>Inconsistent spacing</li>
<li>Localized attachment markers</li>
</ol>
This script solves those issues by cleaning, normalizing, and rebuilding each message from scratch.


### Use Cases
<ul>
<li>Preparing Arabic WhatsApp chats for parsing</li>
<li>Chat archiving and forensic analysis</li>
<li>Migration to HTML / JSON / CSV</li>
<li>Compatibility with WhatsApp chat visualization tools</li>
</ul>

### Requirements
Python 3.8+, No external dependencies


### Usage
`python convert_whatsapp_chat.py`

Input file: `input.txt`

Output file: `output.txt`
