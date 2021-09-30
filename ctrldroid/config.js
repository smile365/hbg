module.exports = (()=>{
  let config = {}
  try {
    config = JSON.parse(files.read("./.env"));
    log(config)
  } catch (error) {
    console.log(error)
  }
  return {
    bmobHeaders: {"X-Bmob-Application-Id":config.appid,"X-Bmob-REST-API-Key":config.appkey},
    apiUrl: "https://api2.bmob.cn/1/"+config.dbname
  }

})();

