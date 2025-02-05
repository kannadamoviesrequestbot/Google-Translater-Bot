from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 

LANGUAGE = InlineKeyboardMarkup(
 [[
 InlineKeyboardButton("Afrikaans", callback_data='af')
 ],[
 InlineKeyboardButton("Albanian", callback_data='sq')
 ],[
 InlineKeyboardButton("Amharic",callback_data ='am')
 ],[  
 InlineKeyboardButton("Arabic", callback_data='ar')
 ],[
 InlineKeyboardButton("Armenian", callback_data='hy') 
 ],[
 InlineKeyboardButton("Azerbaijani",callback_data = 'az')       
 ],[
 InlineKeyboardButton("Basque",callback_data ="eu")
 ],[
 InlineKeyboardButton("Belarusian",callback_data ="be")
 ],[
 InlineKeyboardButton("Bengali",callback_data="bn")
 ],[
 InlineKeyboardButton("Bosnian",callback_data = "bs")
 ],[
 InlineKeyboardButton("Bulgarian",callback_data ="bg")
 ],[
 InlineKeyboardButton("Catalan",callback_data = "ca")
 ],[ 
 InlineKeyboardButton("Corsican",callback_data ="co")
 ],[
 InlineKeyboardButton("Croatian",callback_data = "hr")
 ],[
 InlineKeyboardButton("Czech", callback_data = "cs")
 ],[
 InlineKeyboardButton("Danish",callback_data = "da")
 ],[
 InlineKeyboardButton("Dutch",callback_data = "nl")
 ],[
 InlineKeyboardButton("Esperanto",callback_data = "eo")
 ],[
 InlineKeyboardButton("English",callback_data = "en")
 ],[
 InlineKeyboardButton("Estonian",callback_data = "et")
 ],[
 InlineKeyboardButton("Finnish",callback_data = "fi")
 ],[
 InlineKeyboardButton("French",callback_data = "fr")
 ],[
 InlineKeyboardButton("Frisian",callback_data = "fy")
 ],[
 InlineKeyboardButton("Galician",callback_data = "gl")
 ],[
 InlineKeyboardButton("Georgian",callback_data = "ka")
 ],[
 InlineKeyboardButton("German",callback_data = "de")
 ],[
 InlineKeyboardButton("Greek",callback_data = "el")
 ],[
 InlineKeyboardButton("Gujarati",callback_data = "gu")
 ],[
 InlineKeyboardButton("Haitian Creole",callback_data = "ht")
 ],[
 InlineKeyboardButton("Hausa",callback_data ="ha")
 ],[
 InlineKeyboardButton("Hindi",callback_data = "hi")
 ],[
 InlineKeyboardButton("Hungarian",callback_data = "hu")
 ],[
 InlineKeyboardButton("Icelandic",callback_data = "is")
 ],[
 InlineKeyboardButton("Igbo",callback_data = "ig")
 ],[
 InlineKeyboardButton("Indonesian",callback_data = "id")
 ],[
 InlineKeyboardButton("Irish",callback_data = "ga")
 ],[
 InlineKeyboardButton("Italian",callback_data = "it")
 ],[
 InlineKeyboardButton("Japanese",callback_data = "ja")
 ],[
 InlineKeyboardButton("Javanese",callback_data = "jv")
 ],[
 InlineKeyboardButton("Kannada",callback_data = "kn")
 ],[
 InlineKeyboardButton("Kazakh",callback_data = "kk")
 ],[
 InlineKeyboardButton("Khmer",callback_data = "km")
 ],[
 InlineKeyboardButton("Kinyarwanda",callback_data = "rw")
 ],[
 InlineKeyboardButton("Korean",callback_data ="ko")
 ],[
 InlineKeyboardButton("Kurdish",callback_data = "ku")
 ],[
 InlineKeyboardButton("Kyrgyz",callback_data ="ky")
 ],[
 InlineKeyboardButton("Lao",callback_data = "lo")
 ],[
 InlineKeyboardButton("Latin",callback_data = "la")
 ],[
 InlineKeyboardButton("Latvian",callback_data = "lv")
 ],[
 InlineKeyboardButton('Lithuanian',callback_data ="lt")
 ],[
 InlineKeyboardButton("Luxembourgish",callback_data = "lb")
 ],[
 InlineKeyboardButton("Macedonian",callback_data = "mk")
 ],[
 InlineKeyboardButton("Malagasy",callback_data ="mg")
 ],[
 InlineKeyboardButton("Malay",callback_data ="ms")
 ],[
 InlineKeyboardButton("Malayalam",callback_data = "ml")
 ],[
 InlineKeyboardButton("Maltese",callback_data = "mt")
 ],[
 InlineKeyboardButton("Maori",callback_data = "mi")
 ],[
 InlineKeyboardButton("Marathi",callback_data = "mr")
 ],[
 InlineKeyboardButton("Mongolian",callback_data = "mn")
 ],[
 InlineKeyboardButton("Myanmar (Burmese)",callback_data = "my")
 ],[
 InlineKeyboardButton("Nepali",callback_data ="ne")
 ],[
 InlineKeyboardButton("Norwegian",callback_data = "no")
 ],[
 InlineKeyboardButton("Nyanja (Chichewa)",callback_data = "ny")
 ],[
 InlineKeyboardButton("Odia",callback_data = "or")
 ],[
 InlineKeyboardButton("Pashto",callback_data = "ps")
 ],[
 InlineKeyboardButton("Persian",callback_data = "fa")
 ],[
 InlineKeyboardButton("Polish",callback_data = "pl")
 ],[
 InlineKeyboardButton("Portuguese",callback_data = "pt")
 ],[
 InlineKeyboardButton("Punjabi",callback_data = "pa")
 ],[
 InlineKeyboardButton("Romanian",callback_data = "ro")
 ],[
 InlineKeyboardButton("Russian",callback_data = "ru")
 ],[
 InlineKeyboardButton("Samoan",callback_data= "sm")
 ],[
 InlineKeyboardButton("Scots Gaelic",callback_data = "gd")
 ],[
 InlineKeyboardButton("Serbian",callback_data = "sr")
 ],[
 InlineKeyboardButton("Sesotho",callback_data = "st")
 ],[
 InlineKeyboardButton("Shona",callback_data ="sn")
 ],[
 InlineKeyboardButton("Sindhi",callback_data ="sd")
 ],[
 InlineKeyboardButton("Sinhala (Sinhalese)",callback_data = "si")
 ],[
 InlineKeyboardButton("Slovak",callback_data = "sk")
 ],[
 InlineKeyboardButton("Slovenian",callback_data = "sl")
 ],[
 InlineKeyboardButton("Somali",callback_data = "so")
 ],[
 InlineKeyboardButton("Spanish",callback_data = "es")
 ],[
 InlineKeyboardButton("Sundanese",callback_data ="su")
 ],[
 InlineKeyboardButton("Swahili",callback_data ="sw")
 ],[
 InlineKeyboardButton("Swedish",callback_data = "sv")
 ],[
 InlineKeyboardButton("Tagalog (Filipino)",callback_data ='tl')
 ],[
 InlineKeyboardButton("Tajik",callback_data = "tg")
 ],[
 InlineKeyboardButton("Tamil",callback_data = "ta")
 ],[
 InlineKeyboardButton("Tatar",callback_data = "tt")
 ],[
 InlineKeyboardButton("Telugu",callback_data = "te")
 ],[
 InlineKeyboardButton("Thai",callback_data = "th"),
 ],[
 InlineKeyboardButton("Turkish",callback_data = "tr")
 ],[
 InlineKeyboardButton("Turkmen",callback_data ="tk")    
 ],[
 InlineKeyboardButton("Ukrainian",callback_data = "uk")
 ],[
 InlineKeyboardButton("Urdu",callback_data = "ur")
 ],[    
 InlineKeyboardButton("Uyghur",callback_data ="ug")
 ],[     
 InlineKeyboardButton("Uzbek",callback_data = "uz")
 ],[  
 InlineKeyboardButton("Vietnamese",callback_data ="vi")
 ],[   
 InlineKeyboardButton("Welsh",callback_data = "cy")
 ],[    
 InlineKeyboardButton("Xhosa",callback_data = "xh")
 ],[   
 InlineKeyboardButton("Yiddish",callback_data = "yi")
 ],[     
 InlineKeyboardButton("Yoruba",callback_data = "yo")
 ]]
 )
