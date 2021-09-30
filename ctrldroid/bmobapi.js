let {apiUrl,bmobHeaders} = require('./config.js')

function getData(table,params){
  let geturl = apiUrl+"/"+table;
  if(params) {
    geturl = geturl +"?where=" +JSON.stringify({"packageName":packageName});
  }
  let res = http.get(geturl, {headers: bmobHeaders});
  try {
    let data = res.body.json();
    return data["results"]
  } catch (error) {
    // log(res)
  }
  //if(!data || !data["results"] || data["results"].length < 1) return;
}


let d = getData("taskklist") // 获取下载链接
log("data:"+d)
/**
 * 先回到主界面，然后启动其他 APP
 */
function goHOme2app(fn){
  print("a")
  fn()
}

/**
 * 关掉广告
 */
function closeAd(){
   // id = operational_act_dlg_cancel_iv
}


function getDowloadUrl(){

}

