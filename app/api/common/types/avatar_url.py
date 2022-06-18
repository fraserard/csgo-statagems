import strawberry


@strawberry.type
class AvatarUrl:
    steam_avatar_hash: str

    @strawberry.field
    def big_avatar_url(self) -> str:
        if self.steam_avatar_hash == EMPTY_AVATAR_HASH:
            return f"{DEFAULT_AVATAR_URL}_full.jpg"
        return f"{AVATAR_URL}{self.steam_avatar_hash}_full.jpg"

    @strawberry.field
    def medium_avatar_url(self) -> str:
        if self.steam_avatar_hash == EMPTY_AVATAR_HASH:
            return f"{DEFAULT_AVATAR_URL}_medium.jpg"
        return f"{AVATAR_URL}{self.steam_avatar_hash}_medium.jpg"

    @strawberry.field
    def small_avatar_url(self) -> str:
        if self.steam_avatar_hash == EMPTY_AVATAR_HASH:
            return f"{DEFAULT_AVATAR_URL}.jpg"
        return f"{AVATAR_URL}{self.steam_avatar_hash}.jpg"


AVATAR_URL = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/50/"
DEFAULT_AVATAR_URL = "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/fe/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb"
EMPTY_AVATAR_HASH = "0000000000000000000000000000000000000000"
