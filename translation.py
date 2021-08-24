from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hai {} , I Am A Url Uploader Bot</b>
"""
    HELP_TEXT = """
<b>⁍ Send Me A Http Or Direct Link</b>
<b>⁍ Next Choose The Option Which You Want</b>
<b>⁍ I Will Upload The Media To Telegram</b>
<b>⁍ Send /showthumb To View Current Thumbnail</b>
<b>⁍ Send /deletethumb To Delete Current Thumbnail</b>
<b>⁍ Send /about For Bot Information</b>
"""
    ABOUT_TEXT = """
**A Modified Url Uploader Bot**
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HELP', callback_data='help'),
        InlineKeyboardButton('ABOUT', callback_data='about'),
        InlineKeyboardButton('CLOSE', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME', callback_data='home'),
        InlineKeyboardButton('ABOUT', callback_data='about'),
        InlineKeyboardButton('CLOSE', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME', callback_data='home'),
        InlineKeyboardButton('HELP', callback_data='help'),
        InlineKeyboardButton('CLOSE', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the Desired Format : </b> <a href='{}'>file size might be approximate</a>"""
    CHECKING_LINK = "<b>Processing...⏳</b>"
    BANNED_USER_TEXT = "<b>You Are Banned</b>"
    SET_CUSTOM_USERNAME_PASSWORD = """ """
    DOWNLOAD_START = "<b>Downloading ⬇️</b>"    
    UPLOAD_START = "<b>Uploading ⬆️</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "⭕ <b>Downloaded In</b> {} <b>Seconds</b> \n⭕ <b>Uploaded In</b> {} <b>Seconds</b>"
    RCHD_TG_API_LIMIT = "⭕ <b>Downloaded In</b> {} <b>Seconds</b> \n<b>Detected File Size</b> : {}\n<b>Sorry, I Cannot Upload Files Greater Than 1.95GB Due To Telegram API limitations</b>."
    CUSTOM_CAPTION_UL_FILE = "<b>© BotUserName}</b>"
    SLOW_URL_DECED = "<b>It Is A Slow Link , Please Transload It. Us @Transload.</b>"
    NO_VOID_FORMAT_FOUND = "<b>{}</b>"
    REPORT_SITE_TEXT = "<b>I Can Upload Media From This Site</b>"
    SOMETHING_WRONG = "<b>Something Wrong. Try again.</b>"
    FORCE_SUBSCRIBE_TEXT = "<b>You Must Join My Channel</b>"
    FREE_USER_LIMIT_Q_SZE = "<b>Sorry , User Can Only 1 Request Per {} Minutes. Please Try Again After {} Seconds Later</b>."
