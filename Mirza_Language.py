class MirzaLanguage:
    """
    A class to handle localization and language translation for Mirza Antivirus.
    """

    translate_dict = {
        "en_US": {
            "title": "Mirza Antivirus",
            "quick_scan": "Quick Scan",
            "full_scan": "Full Scan",
            "single_file_scan": "Single File Scan",
            "firewall_status": "Firewall Status: Active (Full Isolation)",
            "rabbitmq_status_active": "RabbitMQ: Active",
            "rabbitmq_status_stopped": "RabbitMQ: Stopped",
            "status": "System Status: Protected",
            "scan_complete": "Scan Complete",
            "no_threats_detected": "No threats detected",
            "malware_found": "Malware Found",
            "warning": "Warning",
            "update_virus_definitions": "Update Virus Definitions",
            "scan": "Scan",
            "file": "File",
            "settings": "Settings",
            "quarantine": "Quarantine",
            "logs": "Logs",
            "quick_scan_complete": "Quick scan has been completed",
            "full_scan_complete": "Full scan has been completed",
            "HASH_scan": "HASH Scan",
            "YARA_scan": "YARA Scan",
            "POLY_scan": "POLY Scan",
            "FULL_isolation": "FULL Isolation",
            "SELECTIVE_protection": "SELECTIVE Protection",
            "Start_rabbitmq": "Start RabbitMQ",
            "Stop_rabbitmq": "Stop RabbitMQ",
            "Rabbitmq_status": "RabbitMQ Status",
            "rabbitmq_active": "RabbitMQ - Active",
            "rabbitmq_stopped": "RabbitMQ - Stopped",
            "firewall_active": "Firewall - Active",
            "firewall_selective": "Firewall - Selective",
        },
        "ru_RU": {
            "title": "Мирза Антивирус",
            "quick_scan": "Быстрая проверка",
            "full_scan": "Полная проверка",
            "single_file_scan": "Проверка файла",
            "firewall_status": "Состояние фаервола: Активен (Полная изоляция)",
            "rabbitmq_status_active": "RabbitMQ: Активен",
            "rabbitmq_status_stopped": "RabbitMQ: Остановлен",
            "status": "Состояние системы: Защищено",
            "scan_complete": "Проверка завершена",
            "no_threats_detected": "Угроз не найдено",
            "malware_found": "Найдено вредоносное ПО",
            "warning": "Предупреждение",
            "update_virus_definitions": "Обновить вирусные базы",
            "scan": "Проверка",
            "file": "Файл",
            "settings": "Настройки",
            "quarantine": "Карантин",
            "logs": "Журналы",
            "quick_scan_complete": "Быстрая проверка завершена",
            "full_scan_complete": "Полная проверка завершена",
            "HASH_scan": "HASH проверка",
            "YARA_scan": "YARA проверка",
            "POLY_scan": "POLY проверка",
            "FULL_isolation": "ПОЛНАЯ изоляция",
            "SELECTIVE_protection": "Выборочная изоляция",
            "Start_rabbitmq": "Начать RabbitMQ мониторинг",
            "Stop_rabbitmq": "Остановить RabbitMQ мониторинг",
            "Rabbitmq_status": "RabbitMQ статус",
            "rabbitmq_active": "RabbitMQ - Активен",
            "rabbitmq_stopped": "RabbitMQ - Остановлен",
            "firewall_active": "Firewall - Активен",
            "firewall_selective": "Firewall - Селективен",
        },
        "zh_TW": {
    "title": "Mirza 防毒軟體",
    "quick_scan": "快速掃描",
    "full_scan": "全盤掃描",
    "single_file_scan": "單檔掃描",
    "firewall_status": "防火牆狀態: 活躍 (完全隔離)",
    "rabbitmq_status_active": "RabbitMQ: 活躍",
    "rabbitmq_status_stopped": "RabbitMQ: 已停止",
    "status": "系統狀態: 已受保護",
    "scan_complete": "掃描完成",
    "no_threats_detected": "沒有發現威脅",
    "malware_found": "已發現惡意軟件",
    "warning": "警告",
    "update_virus_definitions": "更新病毒定義",
    "scan": "掃描",
    "file": "文件",
    "settings": "設置",
    "quarantine": "隔離區",
    "logs": "日誌",
    "quick_scan_complete": "快速掃描已完成",
    "full_scan_complete": "全盤掃描已完成",
    "HASH_scan": "HASH 掃描",
    "YARA_scan": "YARA 掃描",
    "POLY_scan": "POLY 掃描",
    "FULL_isolation": "完全隔離",
    "SELECTIVE_protection": "選擇性保護",
    "Start_rabbitmq": "啟動 RabbitMQ",
    "Stop_rabbitmq": "停止 RabbitMQ",
    "Rabbitmq_status": "RabbitMQ 狀態",
    "rabbitmq_active": "RabbitMQ - 活躍",
    "rabbitmq_stopped": "RabbitMQ - 已停止",
    "firewall_active": "防火牆 - 活躍",
    "firewall_selective": "防火牆 - 選擇性",
},
        "kk_KZ": {
    "title": "Мирза Антивирус",
    "quick_scan": "Жылдам сканерлеу",
    "full_scan": "Толық сканерлеу",
    "single_file_scan": "Жеке файлды сканерлеу",
    "firewall_status": "Фаервол күйі: Белсенді (Толық оқшаулау)",
    "rabbitmq_status_active": "RabbitMQ: Белсенді",
    "rabbitmq_status_stopped": "RabbitMQ: Тоқтатылған",
    "status": "Қорғаныс күйі: Қауіпсіз",
    "scan_complete": "Сканерлеу аяқталды",
    "no_threats_detected": "Қауіп табылған жоқ",
    "malware_found": "Зиянды бағдарлама табылды",
    "warning": "Ескерту",
    "update_virus_definitions": "Вирус дерекқорын жаңарту",
    "scan": "Сканерлеу",
    "file": "Файл",
    "settings": "Баптаулар",
    "quarantine": "Карантин",
    "logs": "Журналдар",
    "quick_scan_complete": "Жылдам сканерлеу аяқталды",
    "full_scan_complete": "Толық сканерлеу аяқталды",
    "HASH_scan": "HASH Сканерлеу",
    "YARA_scan": "YARA Сканерлеу",
    "POLY_scan": "POLY Сканерлеу",
    "FULL_isolation": "ТОЛЫҚ оқшаулау",
    "SELECTIVE_protection": "Таңдамалы қорғау",
    "Start_rabbitmq": "RabbitMQ іске қосу",
    "Stop_rabbitmq": "RabbitMQ тоқтату",
    "Rabbitmq_status": "RabbitMQ күйі",
    "rabbitmq_active": "RabbitMQ - Белсенді",
    "rabbitmq_stopped": "RabbitMQ - Тоқтатылған",
    "firewall_active": "Фаервол - Белсенді",
    "firewall_selective": "Фаервол - Таңдамалы",
},

    }

    @staticmethod
    def get_translation(key: str, language: str = "en_US") -> str:
        """
        Get a translated string for the given key and language.

        Args:
            key (str): The translation key.
            language (str): The language code (default is "en_US").

        Returns:
            str: The translated string or a default error message.
        """
        if language not in MirzaLanguage.translate_dict:
            language = "en_US"
        return MirzaLanguage.translate_dict.get(language, {}).get(key, f"Missing translation for key: {key}")

