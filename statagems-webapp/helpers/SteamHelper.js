function getAvatarURL(hash) {
    var tag = hash.substr(0, 2);
    var url = "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/" + tag + "/" + hash + "_full.jpg";
    if(hash == "0000000000000000000000000000000000000000"){
      return "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/fe/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg"
    } else {
      return url;
    }
}
export default getAvatarURL