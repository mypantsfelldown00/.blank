"""Complete translations for all supported languages."""

from typing import Dict, Any

translations: Dict[str, Dict[str, str]] = {
    # Base translations in English
    'en': {
        'title': 'POINT.BLANK',
        'disclaimer_title': 'DISCLAIMER',
        'accept_disclaimer': 'I have read and accept the disclaimer',
        'language_select': 'Select your preferred language',
        'ticker_label': 'Ticker',
        'period_label': 'History period',
        'interval_label': 'Interval',
        'indicators_label': 'Show Indicators',
        'run_button': 'Run All',
        'price_chart': 'Price Chart & Technical Indicators',
        'ai_forecasts': 'AI Forecasts',
        'running_models': 'Running forecasting models...',
        'news': 'NEWS',
        'export_data': 'Export Data',
        'historical': 'Historical',
        'forecast': 'Forecast'
    },

    # Spanish translations
    'es': {
        'title': 'PUNTO.BLANCO',
        'disclaimer_title': 'AVISO LEGAL',
        'accept_disclaimer': 'He leído y acepto el aviso legal',
        'language_select': 'Seleccione su idioma preferido',
        'ticker_label': 'Símbolo',
        'period_label': 'Período histórico',
        'interval_label': 'Intervalo',
        'indicators_label': 'Mostrar Indicadores',
        'run_button': 'Ejecutar Todo',
        'price_chart': 'Gráfico de Precios e Indicadores Técnicos',
        'ai_forecasts': 'Pronósticos de IA',
        'running_models': 'Ejecutando modelos de pronóstico...',
        'news': 'NOTICIAS',
        'export_data': 'Exportar Datos',
        'historical': 'Histórico',
        'forecast': 'Pronóstico'
    },

    # German translations
    'de': {
        'title': 'PUNKT.LEER',
        'disclaimer_title': 'HAFTUNGSAUSSCHLUSS',
        'accept_disclaimer': 'Ich habe den Haftungsausschluss gelesen und akzeptiere ihn',
        'language_select': 'Wählen Sie Ihre bevorzugte Sprache',
        'ticker_label': 'Tickersymbol',
        'period_label': 'Historischer Zeitraum',
        'interval_label': 'Intervall',
        'indicators_label': 'Indikatoren anzeigen',
        'run_button': 'Alle ausführen',
        'price_chart': 'Preischart & Technische Indikatoren',
        'ai_forecasts': 'KI-Prognosen',
        'running_models': 'Prognosemodelle werden ausgeführt...',
        'news': 'NACHRICHTEN',
        'export_data': 'Daten exportieren',
        'historical': 'Historisch',
        'forecast': 'Prognose'
    },

    # Russian translations
    'ru': {
        'title': 'ТОЧКА.ПУСТОТА',
        'disclaimer_title': 'ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ',
        'accept_disclaimer': 'Я прочитал и принимаю отказ от ответственности',
        'language_select': 'Выберите предпочитаемый язык',
        'ticker_label': 'Тикер',
        'period_label': 'Исторический период',
        'interval_label': 'Интервал',
        'indicators_label': 'Показать индикаторы',
        'run_button': 'Запустить все',
        'price_chart': 'График цен и технические индикаторы',
        'ai_forecasts': 'Прогнозы ИИ',
        'running_models': 'Запуск моделей прогнозирования...',
        'news': 'НОВОСТИ',
        'export_data': 'Экспорт данных',
        'historical': 'Исторический',
        'forecast': 'Прогноз'
    },

    # Chinese translations
    'zh': {
        'title': '点.空',
        'disclaimer_title': '免责声明',
        'accept_disclaimer': '我已阅读并接受免责声明',
        'language_select': '选择您的首选语言',
        'ticker_label': '股票代码',
        'period_label': '历史周期',
        'interval_label': '时间间隔',
        'indicators_label': '显示指标',
        'run_button': '运行全部',
        'price_chart': '价格图表和技术指标',
        'ai_forecasts': '人工智能预测',
        'running_models': '正在运行预测模型...',
        'news': '新闻',
        'export_data': '导出数据',
        'historical': '历史数据',
        'forecast': '预测'
    },

    # Japanese translations
    'ja': {
        'title': 'ポイント.ブランク',
        'disclaimer_title': '免責事項',
        'accept_disclaimer': '免責事項を読み、同意します',
        'language_select': '希望する言語を選択してください',
        'ticker_label': 'ティッカー',
        'period_label': '履歴期間',
        'interval_label': '間隔',
        'indicators_label': '指標を表示',
        'run_button': 'すべて実行',
        'price_chart': '価格チャートとテクニカル指標',
        'ai_forecasts': 'AI予測',
        'running_models': '予測モデルを実行中...',
        'news': 'ニュース',
        'export_data': 'データのエクスポート',
        'historical': '履歴',
        'forecast': '予測'
    },

    # Arabic translations (Right-to-Left)
    'ar': {
        'title': 'نقطة.فارغة',
        'disclaimer_title': 'إخلاء المسؤولية',
        'accept_disclaimer': 'لقد قرأت وأوافق على إخلاء المسؤولية',
        'language_select': 'اختر لغتك المفضلة',
        'ticker_label': 'الرمز',
        'period_label': 'الفترة التاريخية',
        'interval_label': 'الفاصل الزمني',
        'indicators_label': 'عرض المؤشرات',
        'run_button': 'تشغيل الكل',
        'price_chart': 'مخطط الأسعار والمؤشرات الفنية',
        'ai_forecasts': 'توقعات الذكاء الاصطناعي',
        'running_models': 'تشغيل نماذج التنبؤ...',
        'news': 'الأخبار',
        'export_data': 'تصدير البيانات',
        'historical': 'تاريخي',
        'forecast': 'توقع'
    },

    # Hindi translations
    'hi': {
        'title': 'पॉइंट.ब्लैंक',
        'disclaimer_title': 'अस्वीकरण',
        'accept_disclaimer': 'मैंने अस्वीकरण पढ़ा और स्वीकार करता हूं',
        'language_select': 'अपनी पसंदीदा भाषा चुनें',
        'ticker_label': 'टिकर',
        'period_label': 'ऐतिहासिक अवधि',
        'interval_label': 'अंतराल',
        'indicators_label': 'संकेतक दिखाएं',
        'run_button': 'सभी चलाएं',
        'price_chart': 'मूल्य चार्ट और तकनीकी संकेतक',
        'ai_forecasts': 'एआई पूर्वानुमान',
        'running_models': 'पूर्वानुमान मॉडल चल रहे हैं...',
        'news': 'समाचार',
        'export_data': 'डेटा निर्यात करें',
        'historical': 'ऐतिहासिक',
        'forecast': 'पूर्वानुमान'
    },

    # French translations
    'fr': {
        'title': 'POINT.BLANC',
        'disclaimer_title': 'AVERTISSEMENT',
        'accept_disclaimer': 'J\'ai lu et j\'accepte l\'avertissement',
        'language_select': 'Sélectionnez votre langue préférée',
        'ticker_label': 'Symbole',
        'period_label': 'Période historique',
        'interval_label': 'Intervalle',
        'indicators_label': 'Afficher les indicateurs',
        'run_button': 'Tout exécuter',
        'price_chart': 'Graphique des prix et indicateurs techniques',
        'ai_forecasts': 'Prévisions IA',
        'running_models': 'Exécution des modèles de prévision...',
        'news': 'ACTUALITÉS',
        'export_data': 'Exporter les données',
        'historical': 'Historique',
        'forecast': 'Prévision'
    },

    # Portuguese translations
    'pt': {
        'title': 'PONTO.BRANCO',
        'disclaimer_title': 'AVISO LEGAL',
        'accept_disclaimer': 'Li e aceito o aviso legal',
        'language_select': 'Selecione seu idioma preferido',
        'ticker_label': 'Símbolo',
        'period_label': 'Período histórico',
        'interval_label': 'Intervalo',
        'indicators_label': 'Mostrar indicadores',
        'run_button': 'Executar tudo',
        'price_chart': 'Gráfico de preços e indicadores técnicos',
        'ai_forecasts': 'Previsões de IA',
        'running_models': 'Executando modelos de previsão...',
        'news': 'NOTÍCIAS',
        'export_data': 'Exportar dados',
        'historical': 'Histórico',
        'forecast': 'Previsão'
    },

    # Italian translations
    'it': {
        'title': 'PUNTO.BIANCO',
        'disclaimer_title': 'AVVISO LEGALE',
        'accept_disclaimer': 'Ho letto e accetto l\'avviso legale',
        'language_select': 'Seleziona la tua lingua preferita',
        'ticker_label': 'Simbolo',
        'period_label': 'Periodo storico',
        'interval_label': 'Intervallo',
        'indicators_label': 'Mostra indicatori',
        'run_button': 'Esegui tutto',
        'price_chart': 'Grafico dei prezzi e indicatori tecnici',
        'ai_forecasts': 'Previsioni IA',
        'running_models': 'Esecuzione dei modelli di previsione...',
        'news': 'NOTIZIE',
        'export_data': 'Esporta dati',
        'historical': 'Storico',
        'forecast': 'Previsione'
    },

    # Greek translations
    'el': {
        'title': 'ΣΗΜΕΙΟ.ΚΕΝΟ',
        'disclaimer_title': 'ΑΠΟΠΟΙΗΣΗ ΕΥΘΥΝΩΝ',
        'accept_disclaimer': 'Έχω διαβάσει και αποδέχομαι την αποποίηση ευθυνών',
        'language_select': 'Επιλέξτε την προτιμώμενη γλώσσα σας',
        'ticker_label': 'Σύμβολο',
        'period_label': 'Ιστορική περίοδος',
        'interval_label': 'Διάστημα',
        'indicators_label': 'Εμφάνιση δεικτών',
        'run_button': 'Εκτέλεση όλων',
        'price_chart': 'Γράφημα τιμών και τεχνικοί δείκτες',
        'ai_forecasts': 'Προβλέψεις ΤΝ',
        'running_models': 'Εκτέλεση μοντέλων πρόβλεψης...',
        'news': 'ΕΙΔΗΣΕΙΣ',
        'export_data': 'Εξαγωγή δεδομένων',
        'historical': 'Ιστορικό',
        'forecast': 'Πρόβλεψη'
    },

    # Finnish translations
    'fi': {
        'title': 'PISTE.TYHJÄ',
        'disclaimer_title': 'VASTUUVAPAUSLAUSEKE',
        'accept_disclaimer': 'Olen lukenut ja hyväksyn vastuuvapauslausekkeen',
        'language_select': 'Valitse haluamasi kieli',
        'ticker_label': 'Symboli',
        'period_label': 'Historiajakso',
        'interval_label': 'Aikaväli',
        'indicators_label': 'Näytä indikaattorit',
        'run_button': 'Suorita kaikki',
        'price_chart': 'Hintakaavio ja tekniset indikaattorit',
        'ai_forecasts': 'Tekoälyennusteet',
        'running_models': 'Suoritetaan ennustemalleja...',
        'news': 'UUTISET',
        'export_data': 'Vie data',
        'historical': 'Historiallinen',
        'forecast': 'Ennuste'
    },

    # Swedish translations
    'sv': {
        'title': 'PUNKT.TOM',
        'disclaimer_title': 'ANSVARSFRISKRIVNING',
        'accept_disclaimer': 'Jag har läst och accepterar ansvarsfriskrivningen',
        'language_select': 'Välj ditt föredragna språk',
        'ticker_label': 'Symbol',
        'period_label': 'Historisk period',
        'interval_label': 'Intervall',
        'indicators_label': 'Visa indikatorer',
        'run_button': 'Kör alla',
        'price_chart': 'Priskurva och tekniska indikatorer',
        'ai_forecasts': 'AI-prognoser',
        'running_models': 'Kör prognosmodeller...',
        'news': 'NYHETER',
        'export_data': 'Exportera data',
        'historical': 'Historisk',
        'forecast': 'Prognos'
    },

    # Polish translations
    'pl': {
        'title': 'PUNKT.PUSTY',
        'disclaimer_title': 'ZASTRZEŻENIE',
        'accept_disclaimer': 'Przeczytałem i akceptuję zastrzeżenie',
        'language_select': 'Wybierz preferowany język',
        'ticker_label': 'Symbol',
        'period_label': 'Okres historyczny',
        'interval_label': 'Interwał',
        'indicators_label': 'Pokaż wskaźniki',
        'run_button': 'Uruchom wszystko',
        'price_chart': 'Wykres cen i wskaźniki techniczne',
        'ai_forecasts': 'Prognozy AI',
        'running_models': 'Uruchamianie modeli prognozowania...',
        'news': 'WIADOMOŚCI',
        'export_data': 'Eksportuj dane',
        'historical': 'Historyczny',
        'forecast': 'Prognoza'
    },

    # Turkish translations
    'tr': {
        'title': 'NOKTA.BOŞ',
        'disclaimer_title': 'SORUMLULUK REDDİ',
        'accept_disclaimer': 'Sorumluluk reddini okudum ve kabul ediyorum',
        'language_select': 'Tercih ettiğiniz dili seçin',
        'ticker_label': 'Sembol',
        'period_label': 'Tarihsel dönem',
        'interval_label': 'Aralık',
        'indicators_label': 'Göstergeleri göster',
        'run_button': 'Tümünü çalıştır',
        'price_chart': 'Fiyat grafiği ve teknik göstergeler',
        'ai_forecasts': 'Yapay zeka tahminleri',
        'running_models': 'Tahmin modelleri çalıştırılıyor...',
        'news': 'HABERLER',
        'export_data': 'Verileri dışa aktar',
        'historical': 'Tarihsel',
        'forecast': 'Tahmin'
    },

    # Afrikaans translations
    'af': {
        'title': 'PUNT.LEEG',
        'disclaimer_title': 'VRYWARING',
        'accept_disclaimer': 'Ek het die vrywaring gelees en aanvaar dit',
        'language_select': 'Kies jou voorkeur taal',
        'ticker_label': 'Simbool',
        'period_label': 'Geskiedkundige tydperk',
        'interval_label': 'Interval',
        'indicators_label': 'Wys aanwysers',
        'run_button': 'Begin alles',
        'price_chart': 'Prys grafiek en tegniese aanwysers',
        'ai_forecasts': 'KI voorspellings',
        'running_models': 'Voorspellingsmodelle word uitgevoer...',
        'news': 'NUUS',
        'export_data': 'Voer data uit',
        'historical': 'Geskiedkundig',
        'forecast': 'Voorspelling'
    },

    # Zulu translations
    'zu': {
        'title': 'IPHUZU.NGANGI',
        'disclaimer_title': 'ISAZISO SOKUNGATHWALI MLANDU',
        'accept_disclaimer': 'Ngifundile futhi ngiyakwamukela ukungathwali mlandu',
        'language_select': 'Khetha ulimi lwakho oluthandayo',
        'ticker_label': 'Uphawu',
        'period_label': 'Isikhathi somlando',
        'interval_label': 'Ikhefu',
        'indicators_label': 'Khombisa izinkomba',
        'run_button': 'Qalisa konke',
        'price_chart': 'Ishadi lentengo nezinkomba zobuchwepheshe',
        'ai_forecasts': 'Ukubikezela kwe-AI',
        'running_models': 'Kuqhutshwa amamodeli okubikezela...',
        'news': 'IZINDABA',
        'export_data': 'Thumela idatha',
        'historical': 'Umlando',
        'forecast': 'Ukubikezela'
    },

    # Xhosa translations
    'xh': {
        'title': 'INDAWO.NGANENO',
        'disclaimer_title': 'ISAZISO SOKUNGATHWALI XANDUVA',
        'accept_disclaimer': 'Ndifundile kwaye ndiyayamkela inkcazelo yokungathwali xanduva',
        'language_select': 'Khetha ulwimi olulungiselele wena',
        'ticker_label': 'Uphawu',
        'period_label': 'Ixesha lembali',
        'interval_label': 'Isithuba',
        'indicators_label': 'Bonisa izalathisi',
        'run_button': 'Qalisa konke',
        'price_chart': 'Itshati yamaxabiso nezalathiso zobugcisa',
        'ai_forecasts': 'Uqikelelo lwe-AI',
        'running_models': 'Ukuqhuba iimodeli zokuqikelela...',
        'news': 'IINDABA',
        'export_data': 'Khuphela idatha',
        'historical': 'Yembali',
        'forecast': 'Uqikelelo'
    },

    # Northern Sotho (Sepedi) translations
    'nso': {
        'title': 'NTLHA.NTLE',
        'disclaimer_title': 'TEMANA YA GO SE BE LE MAIKARABELO',
        'accept_disclaimer': 'Ke badile ebile ke amogela temana ya go se be le maikarabelo',
        'language_select': 'Kgetha polelo ya gago ya kgetho',
        'ticker_label': 'Seka',
        'period_label': 'Nako ya histori',
        'interval_label': 'Sekgoba',
        'indicators_label': 'Bontšha ditšhupetšo',
        'run_button': 'Tshepediša tšohle',
        'price_chart': 'Tšhate ya ditheko le ditšhupetšo tša sethekniki',
        'ai_forecasts': 'Diponelopele tša AI',
        'running_models': 'Go tshepediša dimotlolo tša diponelopele...',
        'news': 'DITABA',
        'export_data': 'Romela data',
        'historical': 'Ya histori',
        'forecast': 'Ponelopele'
    },

    # Tswana translations
    'tn': {
        'title': 'NTLHA.LOLEA',
        'disclaimer_title': 'KITSISO YA GO SE RWALE MAIKARABELO',
        'accept_disclaimer': 'Ke badile ebile ke amogela kitsiso ya go se rwale maikarabelo',
        'language_select': 'Tlhopha puo e o e ratang',
        'ticker_label': 'Letshwao',
        'period_label': 'Paka ya ditso',
        'interval_label': 'Sekgala',
        'indicators_label': 'Bontsha ditshupiso',
        'run_button': 'Tsamaisa tsotlhe',
        'price_chart': 'Tšhate ya ditlhwatlhwa le ditshupiso tsa setegeniki',
        'ai_forecasts': 'Diponelopele tsa AI',
        'running_models': 'Go tsamaisa dimotlolo tsa diponelopele...',
        'news': 'DIKGANG',
        'export_data': 'Romela data',
        'historical': 'Ya ditso',
        'forecast': 'Ponelopele'
    },

    # Southern Sotho translations
    'st': {
        'title': 'NTLHA.FEELA',
        'disclaimer_title': 'TLHALOSETSO YA HO SE JARELE BOIKARABELO',
        'accept_disclaimer': 'Ke badile mme ke amohela tlhalosetso ya ho se jarele boikarabelo',
        'language_select': 'Kgetha puo eo o e ratang',
        'ticker_label': 'Letshwao',
        'period_label': 'Nako ya nalane',
        'interval_label': 'Sekgeo',
        'indicators_label': 'Bontsha ditshupiso',
        'run_button': 'Tsamaisa tsohle',
        'price_chart': 'Tjhate ya ditheko le ditshupiso tsa tekgeniki',
        'ai_forecasts': 'Diponelopele tsa AI',
        'running_models': 'Ho tsamaisa dimotlolo tsa diponelopele...',
        'news': 'DITABA',
        'export_data': 'Romela data',
        'historical': 'Ya nalane',
        'forecast': 'Ponelopele'
    },

    # Tsonga translations
    'ts': {
        'title': 'NDHAWU.HAVA',
        'disclaimer_title': 'XITIVISO XA KU TSHIKA VUTIHLAMULERI',
        'accept_disclaimer': 'Ndzi hlayile na ku amukela xitiviso xa ku tshika vutihlamuleri',
        'language_select': 'Hlawula ririmi leri u ri tsakelaka',
        'ticker_label': 'Xikombiso',
        'period_label': 'Nkarhi wa matimu',
        'interval_label': 'Ndhawu',
        'indicators_label': 'Kombisa swikombiso',
        'run_button': 'Fambisa hinkwaswo',
        'price_chart': 'Tchati ya minxavo na swikombiso swa xithekiniki',
        'ai_forecasts': 'Vuprofeta bya AI',
        'running_models': 'Ku fambisa timodele ta vuprofeta...',
        'news': 'MAHUNGU',
        'export_data': 'Rhumela data',
        'historical': 'Ya matimu',
        'forecast': 'Vuprofeta'
    },

    # Swati translations
    'ss': {
        'title': 'INDZAWO.LITE',
        'disclaimer_title': 'SATISO SEKUNGATSATSI UMTFWALO',
        'accept_disclaimer': 'Ngifundzile futsi ngiyasemukela satiso sekungatsatsi umtfwalo',
        'language_select': 'Khetsa lulwimi lolutsandzako',
        'ticker_label': 'Luphawu',
        'period_label': 'Sikhatsi semlandvo',
        'interval_label': 'Sikhala',
        'indicators_label': 'Khombisa tinkhomba',
        'run_button': 'Sebentisa konkhe',
        'price_chart': 'Itjhati yemandla netinkhomba tebuchwepheshe',
        'ai_forecasts': 'Kubiketela kwe-AI',
        'running_models': 'Kusebentisa timodeli tekubiketela...',
        'news': 'TINDZABA',
        'export_data': 'Khipha idata',
        'historical': 'Yemlandvo',
        'forecast': 'Kubiketela'
    },

    # Venda translations
    've': {
        'title': 'FHETHU.THONGO',
        'disclaimer_title': 'NDIVHADZO YA U SA DZHIA VHUḒIFHINDULELI',
        'accept_disclaimer': 'Ndo vhala na u tenda ndivhadzo ya u sa dzhia vhuḓifhinduleli',
        'language_select': 'Nanga luambo lune na lu takalela',
        'ticker_label': 'Tshiga',
        'period_label': 'Tshifhinga tsha ḓivhazwakale',
        'interval_label': 'Tshikhala',
        'indicators_label': 'Sumbedza zwisumbedzisi',
        'run_button': 'Thoma zwoṱhe',
        'price_chart': 'Tshati ya mitengo na zwisumbedzisi zwa thekhiniki',
        'ai_forecasts': 'Vhudavhidzano ha AI',
        'running_models': 'U tshimbidza modele dza vhudavhidzano...',
        'news': 'MAFHUNGO',
        'export_data': 'Bvisa data',
        'historical': 'Ya ḓivhazwakale',
        'forecast': 'Vhudavhidzano'
    },

    # Southern Ndebele translations
    'nr': {
        'title': 'INDAWO.ZEZE',
        'disclaimer_title': 'ISAZISO SOKUNGATHWALI MLANDU',
        'accept_disclaimer': 'Ngifundile begodu ngiyavuma isaziso sokungathwali mlandu',
        'language_select': 'Khetha ilimi okhetha lona',
        'ticker_label': 'Uphawu',
        'period_label': 'Isikhathi somlando',
        'interval_label': 'Isikhala',
        'indicators_label': 'Khombisa iintjengisi',
        'run_button': 'Thoma koke',
        'price_chart': 'Itjhati yamaphreisi neentjengisi zethekhniki',
        'ai_forecasts': 'Ukubika kwe-AI',
        'running_models': 'Ukutjhayisa amamodeli wokubika...',
        'news': 'IINDABA',
        'export_data': 'Khupa idatha',
        'historical': 'Yomlando',
        'forecast': 'Ukubika'
    },

    # Swahili translations
    'sw': {
        'title': 'NUKTA.TUPU',
        'disclaimer_title': 'KANUSHO',
        'accept_disclaimer': 'Nimesoma na kukubali kanusho',
        'language_select': 'Chagua lugha unayopendelea',
        'ticker_label': 'Alama',
        'period_label': 'Kipindi cha historia',
        'interval_label': 'Muda',
        'indicators_label': 'Onyesha viashiria',
        'run_button': 'Endesha yote',
        'price_chart': 'Chati ya bei na viashiria vya kiufundi',
        'ai_forecasts': 'Utabiri wa AI',
        'running_models': 'Kuendesha miundo ya utabiri...',
        'news': 'HABARI',
        'export_data': 'Hamisha data',
        'historical': 'Ya kihistoria',
        'forecast': 'Utabiri'
    },

    # Berber (Tamazight) translations
    'ber': {
        'title': 'TANQIṬ.TILEMT',
        'disclaimer_title': 'ASEFHEM',
        'accept_disclaimer': 'Ɣriɣ u qebleɣ asefhem',
        'language_select': 'Fren tutlayt i tebɣiḍ',
        'ticker_label': 'Azamul',
        'period_label': 'Akud n umezruy',
        'interval_label': 'Azilal',
        'indicators_label': 'Sken inmaɣnuten',
        'run_button': 'Selkem akk',
        'price_chart': 'Aɣanib n ssuma d inmaɣnuten itiqniyen',
        'ai_forecasts': 'Asmerwes n AI',
        'running_models': 'Aselkem n imedyaten n usmerwes...',
        'news': 'ISALLEN',
        'export_data': 'Sifeḍ isefka',
        'historical': 'Amezruy',
        'forecast': 'Asmerwes'
    },

    # Hebrew translations (Right-to-Left)
    'he': {
        'title': 'נקודה.ריק',
        'disclaimer_title': 'כתב ויתור',
        'accept_disclaimer': 'קראתי ואני מקבל את כתב הוויתור',
        'language_select': 'בחר את השפה המועדפת עליך',
        'ticker_label': 'סימול',
        'period_label': 'תקופה היסטורית',
        'interval_label': 'מרווח',
        'indicators_label': 'הצג מדדים',
        'run_button': 'הרץ הכל',
        'price_chart': 'גרף מחירים ומדדים טכניים',
        'ai_forecasts': 'תחזיות בינה מלאכותית',
        'running_models': 'מריץ מודלים של תחזיות...',
        'news': 'חדשות',
        'export_data': 'ייצוא נתונים',
        'historical': 'היסטורי',
        'forecast': 'תחזית'
    },

    # Urdu translations (Right-to-Left)
    'ur': {
        'title': 'نقطہ.خالی',
        'disclaimer_title': 'دستبرداری',
        'accept_disclaimer': 'میں نے دستبرداری پڑھی اور قبول کرتا ہوں',
        'language_select': 'اپنی پسندیدہ زبان منتخب کریں',
        'ticker_label': 'علامت',
        'period_label': 'تاریخی مدت',
        'interval_label': 'وقفہ',
        'indicators_label': 'اشاریے دکھائیں',
        'run_button': 'سب چلائیں',
        'price_chart': 'قیمت چارٹ اور تکنیکی اشاریے',
        'ai_forecasts': 'مصنوعی ذہانت کی پیشگوئیاں',
        'running_models': 'پیشگوئی ماڈلز چل رہے ہیں...',
        'news': 'خبریں',
        'export_data': 'ڈیٹا برآمد کریں',
        'historical': 'تاریخی',
        'forecast': 'پیشگوئی'
    },

    # Tamil translations
    'ta': {
        'title': 'புள்ளி.வெற்று',
        'disclaimer_title': 'பொறுப்புத் துறப்பு',
        'accept_disclaimer': 'பொறுப்புத் துறப்பை படித்து ஏற்றுக்கொள்கிறேன்',
        'language_select': 'உங்கள் விருப்பமான மொழியைத் தேர்ந்தெடுக்கவும்',
        'ticker_label': 'குறியீடு',
        'period_label': 'வரலாற்று காலம்',
        'interval_label': 'இடைவெளி',
        'indicators_label': 'குறிகாட்டிகளைக் காட்டு',
        'run_button': 'அனைத்தையும் இயக்கு',
        'price_chart': 'விலை விளக்கப்படம் & தொழில்நுட்ப குறிகாட்டிகள்',
        'ai_forecasts': 'செயற்கை நுண்ணறிவு முன்னறிவிப்புகள்',
        'running_models': 'முன்னறிவிப்பு மாதிரிகள் இயங்குகின்றன...',
        'news': 'செய்திகள்',
        'export_data': 'தரவை ஏற்றுமதி செய்',
        'historical': 'வரலாற்று',
        'forecast': 'முன்னறிவிப்பு'
    },

    # Nepali translations
    'ne': {
        'title': 'बिन्दु.खाली',
        'disclaimer_title': 'अस्वीकरण',
        'accept_disclaimer': 'मैले अस्वीकरण पढेको छु र स्वीकार गर्छु',
        'language_select': 'आफ्नो रुचाइएको भाषा छान्नुहोस्',
        'ticker_label': 'टिकर',
        'period_label': 'ऐतिहासिक अवधि',
        'interval_label': 'अन्तराल',
        'indicators_label': 'सूचकहरू देखाउनुहोस्',
        'run_button': 'सबै चलाउनुहोस्',
        'price_chart': 'मूल्य चार्ट र प्राविधिक सूचकहरू',
        'ai_forecasts': 'एआई पूर्वानुमानहरू',
        'running_models': 'पूर्वानुमान मोडेलहरू चलिरहेका छन्...',
        'news': 'समाचार',
        'export_data': 'डाटा निर्यात गर्नुहोस्',
        'historical': 'ऐतिहासिक',
        'forecast': 'पूर्वानुमान'
    },

    # Bengali translations
    'bn': {
        'title': 'পয়েন্ট.ফাঁকা',
        'disclaimer_title': 'দায়মুক্তি',
        'accept_disclaimer': 'আমি দায়মুক্তি পড়েছি এবং স্বীকার করি',
        'language_select': 'আপনার পছন্দের ভাষা নির্বাচন করুন',
        'ticker_label': 'টিকার',
        'period_label': 'ঐতিহাসিক সময়কাল',
        'interval_label': 'অন্তরাল',
        'indicators_label': 'সূচকগুলি দেখান',
        'run_button': 'সব চালান',
        'price_chart': 'মূল্য চার্ট এবং কারিগরি সূচকগুলি',
        'ai_forecasts': 'এআই পূর্বাভাস',
        'running_models': 'পূর্বাভাস মডেলগুলি চলছে...',
        'news': 'সংবাদ',
        'export_data': 'ডেটা রপ্তানি করুন',
        'historical': 'ঐতিহাসিক',
        'forecast': 'পূর্বাভাস'
    },

    # Sinhala translations
    'si': {
        'title': 'ලක්ෂය.හිස්',
        'disclaimer_title': 'වගකීම් ප්‍රතික්ෂේප කිරීම',
        'accept_disclaimer': 'මම වගකීම් ප්‍රතික්ෂේප කිරීම කියවා පිළිගනිමි',
        'language_select': 'ඔබේ කැමති භාෂාව තෝරන්න',
        'ticker_label': 'ටිකර්',
        'period_label': 'ඓතිහාසික කාලය',
        'interval_label': 'පරතරය',
        'indicators_label': 'දර්ශක පෙන්වන්න',
        'run_button': 'සියල්ල ක්‍රියාත්මක කරන්න',
        'price_chart': 'මිල සටහන සහ තාක්ෂණික දර්ශක',
        'ai_forecasts': 'කෘතිම බුද්ධි පුරෝකථන',
        'running_models': 'පුරෝකථන ආකෘති ක්‍රියාත්මක වේ...',
        'news': 'පුවත්',
        'export_data': 'දත්ත අපනයනය කරන්න',
        'historical': 'ඓතිහාසික',
        'forecast': 'පුරෝකථනය'
    },

    # Thai translations
    'th': {
        'title': 'จุด.ว่าง',
        'disclaimer_title': 'ข้อจำกัดความรับผิดชอบ',
        'accept_disclaimer': 'ฉันได้อ่านและยอมรับข้อจำกัดความรับผิดชอบ',
        'language_select': 'เลือกภาษาที่คุณต้องการ',
        'ticker_label': 'สัญลักษณ์',
        'period_label': 'ช่วงเวลาประวัติศาสตร์',
        'interval_label': 'ช่วงเวลา',
        'indicators_label': 'แสดงตัวชี้วัด',
        'run_button': 'เริ่มทั้งหมด',
        'price_chart': 'แผนภูมิราคาและตัวชี้วัดทางเทคนิค',
        'ai_forecasts': 'การพยากรณ์ด้วย AI',
        'running_models': 'กำลังรันโมเดลการพยากรณ์...',
        'news': 'ข่าวสาร',
        'export_data': 'ส่งออกข้อมูล',
        'historical': 'ประวัติศาสตร์',
        'forecast': 'พยากรณ์'
    },

    # Malay translations
    'ms': {
        'title': 'TITIK.KOSONG',
        'disclaimer_title': 'PENAFIAN',
        'accept_disclaimer': 'Saya telah membaca dan menerima penafian',
        'language_select': 'Pilih bahasa pilihan anda',
        'ticker_label': 'Simbol',
        'period_label': 'Tempoh sejarah',
        'interval_label': 'Selang',
        'indicators_label': 'Tunjuk penunjuk',
        'run_button': 'Jalankan semua',
        'price_chart': 'Carta harga & penunjuk teknikal',
        'ai_forecasts': 'Ramalan AI',
        'running_models': 'Menjalankan model ramalan...',
        'news': 'BERITA',
        'export_data': 'Eksport data',
        'historical': 'Sejarah',
        'forecast': 'Ramalan'
    },

    # Indonesian translations
    'id': {
        'title': 'TITIK.KOSONG',
        'disclaimer_title': 'PENAFIAN',
        'accept_disclaimer': 'Saya telah membaca dan menerima penafian',
        'language_select': 'Pilih bahasa yang Anda sukai',
        'ticker_label': 'Simbol',
        'period_label': 'Periode historis',
        'interval_label': 'Interval',
        'indicators_label': 'Tampilkan indikator',
        'run_button': 'Jalankan semua',
        'price_chart': 'Grafik harga & indikator teknis',
        'ai_forecasts': 'Prediksi AI',
        'running_models': 'Menjalankan model prediksi...',
        'news': 'BERITA',
        'export_data': 'Ekspor data',
        'historical': 'Historis',
        'forecast': 'Prediksi'
    },

    # Korean translations
    'ko': {
        'title': '포인트.공백',
        'disclaimer_title': '면책 조항',
        'accept_disclaimer': '면책 조항을 읽고 동의합니다',
        'language_select': '선호하는 언어를 선택하세요',
        'ticker_label': '티커',
        'period_label': '기록 기간',
        'interval_label': '간격',
        'indicators_label': '지표 표시',
        'run_button': '모두 실행',
        'price_chart': '가격 차트 및 기술적 지표',
        'ai_forecasts': 'AI 예측',
        'running_models': '예측 모델 실행 중...',
        'news': '뉴스',
        'export_data': '데이터 내보내기',
        'historical': '과거',
        'forecast': '예측'
    },

    # Kazakh translations
    'kk': {
        'title': 'НҮКТЕ.БОС',
        'disclaimer_title': 'ЖАУАПКЕРШІЛІКТЕН БАС ТАРТУ',
        'accept_disclaimer': 'Жауапкершіліктен бас тартуды оқып, қабылдаймын',
        'language_select': 'Қалаған тілді таңдаңыз',
        'ticker_label': 'Тикер',
        'period_label': 'Тарихи кезең',
        'interval_label': 'Аралық',
        'indicators_label': 'Индикаторларды көрсету',
        'run_button': 'Барлығын іске қосу',
        'price_chart': 'Баға графигі және техникалық индикаторлар',
        'ai_forecasts': 'AI болжамдары',
        'running_models': 'Болжам модельдері орындалуда...',
        'news': 'ЖАҢАЛЫҚТАР',
        'export_data': 'Деректерді экспорттау',
        'historical': 'Тарихи',
        'forecast': 'Болжам'
    },

    # Uzbek translations
    'uz': {
        'title': 'NUQTA.BO\'SH',
        'disclaimer_title': 'MASULIYATDAN VOZ KECHISH',
        'accept_disclaimer': 'Masuliyatdan voz kechishni o\'qib chiqdim va qabul qilaman',
        'language_select': 'Afzal ko\'rgan tilingizni tanlang',
        'ticker_label': 'Tiker',
        'period_label': 'Tarixiy davr',
        'interval_label': 'Interval',
        'indicators_label': 'Ko\'rsatkichlarni ko\'rsatish',
        'run_button': 'Hammasini ishga tushirish',
        'price_chart': 'Narx grafigi va texnik ko\'rsatkichlar',
        'ai_forecasts': 'AI bashoratlari',
        'running_models': 'Bashorat modellari ishga tushmoqda...',
        'news': 'YANGILIKLAR',
        'export_data': 'Ma\'lumotlarni eksport qilish',
        'historical': 'Tarixiy',
        'forecast': 'Bashorat'
    },

    # Mongolian translations
    'mn': {
        'title': 'ЦЭГ.ХООСОН',
        'disclaimer_title': 'ҮҮРЭГ ХҮЛЭЭХЭЭС ТАТГАЛЗАХ',
        'accept_disclaimer': 'Би үүрэг хүлээхээс татгалзах мэдэгдлийг уншиж, зөвшөөрч байна',
        'language_select': 'Сонгох хэлээ сонгоно уу',
        'ticker_label': 'Тикер',
        'period_label': 'Түүхэн хугацаа',
        'interval_label': 'Интервал',
        'indicators_label': 'Үзүүлэлтүүдийг харуулах',
        'run_button': 'Бүгдийг ажиллуулах',
        'price_chart': 'Үнийн график ба техникийн үзүүлэлтүүд',
        'ai_forecasts': 'AI таамаглал',
        'running_models': 'Таамаглалын загваруудыг ажиллуулж байна...',
        'news': 'МЭДЭЭ',
        'export_data': 'Өгөгдлийг экспортлох',
        'historical': 'Түүхэн',
        'forecast': 'Таамаглал'
    },

    # Burmese translations
    'my': {
        'title': 'အမှတ်.အလွတ်',
        'disclaimer_title': 'သတိပေးချက်',
        'accept_disclaimer': 'သတိပေးချက်ကို ဖတ်ရှုပြီး လက်ခံပါသည်',
        'language_select': 'သင့်နှစ်သက်ရာ ဘာသာစကားကို ရွေးချယ်ပါ',
        'ticker_label': 'တစ်ခုး',
        'period_label': 'သမိုင်းကာလ',
        'interval_label': 'ကြားကာလ',
        'indicators_label': 'အညွှန်းကိန်းများကို ပြပါ',
        'run_button': 'အားလုံးကို လုပ်ဆောင်ပါ',
        'price_chart': 'စျေးနှုန်းဇယား နှင့် နည်းပညာအညွှန်းကိန်းများ',
        'ai_forecasts': 'AI ခန့်မှန်းချက်များ',
        'running_models': 'ခန့်မှန်းချက်ပုံစံများကို လုပ်ဆောင်နေသည်...',
        'news': 'သတင်း',
        'export_data': 'ဒေတာထုတ်ယူပါ',
        'historical': 'သမိုင်းဆိုင်ရာ',
        'forecast': 'ခန့်မှန်းချက်'
    },

    # Maori translations
    'mi': {
        'title': 'KOINGA.PUTANGA',
        'disclaimer_title': 'WHAKAKORENGA',
        'accept_disclaimer': 'Kua pānuihia, whakaae hoki au ki te whakakorenga',
        'language_select': 'Tīpakohia tō reo e hiahia ana',
        'ticker_label': 'Tohu',
        'period_label': 'Wā hītori',
        'interval_label': 'Takiwā',
        'indicators_label': 'Whakaatu tohu',
        'run_button': 'Whakahaerehia katoa',
        'price_chart': 'Tūtohi utu me ngā tohu hangarau',
        'ai_forecasts': 'Matapae AI',
        'running_models': 'E whakahaere ana i ngā tauira matapae...',
        'news': 'PŪRONGO',
        'export_data': 'Kaweake raraunga',
        'historical': 'Hītori',
        'forecast': 'Matapae'
    }
}

# Add all remaining languages with base English translations
remaining_languages = [
    'fr', 'pt', 'ta', 'it', 'el', 'fi', 'sv', 'pl', 'tr', 'zu', 'xh', 'af', 
    'nso', 'tn', 'st', 'ts', 'ss', 've', 'nr', 'sw', 'ber', 'he', 'ur', 'ne', 
    'bn', 'si', 'th', 'ms', 'id', 'ko', 'kk', 'uz', 'mn', 'my', 'mi'
]

for lang in remaining_languages:
    if lang not in translations:
        translations[lang] = translations['en'].copy()

def get_translation(key: str, lang: str = "en") -> str:
    """Get translation for a key in the specified language."""
    try:
        # First try the requested language
        if lang in translations and key in translations[lang]:
            return translations[lang][key]
        # Fallback to English
        if key in translations["en"]:
            return translations["en"][key]
        # If not found in English, return the key itself
        return key
    except Exception:
        return key