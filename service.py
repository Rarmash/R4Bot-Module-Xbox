from xpa import ErrorHandler as XboxErrorHandler

PROFILE_FIELDS_HOOK = "profile.fields"


class XboxService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        self.module.register_hook_provider(PROFILE_FIELDS_HOOK, self.build_profile_fields)

    def unregister_hooks(self):
        self.module.unregister_hook_provider(PROFILE_FIELDS_HOOK)

    def build_profile_fields(self, ctx, member, user_data, server_data):
        xuid = user_data.get("xbox")
        if not xuid:
            return []

        try:
            gamertag = self.module.xpa.get_account_info_xuid(xuid).Gamertag
        except XboxErrorHandler.XboxApiError:
            gamertag = str(xuid)

        return [
            {
                "name": "Профиль Xbox",
                "value": f"[{gamertag}](https://www.xbox.com/play/user/{str(gamertag).replace(' ', '%20')})",
            }
        ]
