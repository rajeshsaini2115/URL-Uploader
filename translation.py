from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hai {} , I Am A Url Uploader Bot</b>
"""
    HELP_TEXT = """
<b>⁍ Send A Http YouTube DL Supported Link Or Direct Link</b>
<b>⁍ Next Choose The Desired Option</b>
<b>⁍ Wait Until The Process Get Completed</b>
<b>⁍ Send /showthumbnail To View Current Thumbnail</b>
<b>⁍ Send /deletethumbnail To Delete Current Thumbnail</b>
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
    FORMAT_SELECTION = """<b>Select the Desired Format : </b> <a href='{}'>File Size Might Be Approximate</a>"""
    CHECKING_LINK = "<b>Processing...⏳</b>"
    BANNED_USER_TEXT = "<b>You Are Banned</b>"
    SET_CUSTOM_USERNAME_PASSWORD = """ """
    DOWNLOAD_START = "<b>Downloading ⬇️</b>"    
    UPLOAD_START = "<b>Uploading ⬆️</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "⭕ <b>Downloaded In</b> {} <b>Seconds</b> \n⭕ <b>Uploaded In</b> {} <b>Seconds</b>"
    RCHD_TG_API_LIMIT = "⭕ <b>Downloaded In</b> {} <b>Seconds</b> \n<b>Detected File Size</b> : {}\n<b>Sorry, I Cannot Upload Files Greater Than 1.95GB Due To Telegram API limitations</b>"
    CUSTOM_CAPTION_UL_FILE = "<b>© @TheUrlUploader_bot/b>"
    SLOW_URL_DECED = "<b>It Is A Slow Link , Transload It. Us @Transload</b>"
    NO_VOID_FORMAT_FOUND = "<b>{}</b>"
    REPORT_SITE_TEXT = "<b>Can't Upload Media From This Site</b>"
    SOMETHING_WRONG = "<b>Something Wrong Try again</b>"
    FORCE_SUBSCRIBE_TEXT = "<b>Join Updates Channel</b>"
    FREE_USER_LIMIT_Q_SZE = "<b>1 Request Per</b> {} <b>Minutes \nWait</b> {} <b>Seconds</b>"
