// 测试控制手机通过迅雷下载磁力链接资源
magnet = 'magnet:?xt=urn:btih:C12EDFCD702CD7ED2044AC0B0467FC3D2783302D&dn=魅惑的な若い女性は7人の男性と戦う'
setClip(magnet)
launch("com.xunlei.downloadprovider");

let addTaskBtn = desc("添加任务").findOne(3000)
print(addTaskBtn)
addTaskBtn.click();
let addUrlBtn = text("添加链接").findOne(3000)
addUrlBtn.click()


let downloadBtn = text("下载").findOne(3000)
let urlEdt = className("EditText").findOne(3000)
if (urlEdt.text().length > 0){
  downloadBtn.click()
}


let goDldBtn = text("立即下载").findOne(3000)
goDldBtn.click()
