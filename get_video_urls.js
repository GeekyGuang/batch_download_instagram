// 自定义从控制台将变量保存到本地的函数
; (function (console) {
    console.save = function (data, filename) {
        if (!data) {
            console.error("Console.save: No data")
            return
        }

        if (!filename) filename = "console.json"

        if (typeof data === "object") {
            data = JSON.stringify(data, undefined, 4)
        }

        var blob = new Blob([data], { type: "text/json" }),
            e = document.createEvent("MouseEvents"),
            a = document.createElement("a")

        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl = ["text/json", a.download, a.href].join(":")
        e.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null,)
        a.dispatchEvent(e)
    }
})(console)


// 获取下载链接
const download_items = document.querySelectorAll('.download')
const download_itemsArray = [...download_items]
const download_itemshref = download_itemsArray.map(item => item.href).join('\n')
// 保存下载到本地
console.save(download_itemshref, '下载链接.txt')

// 获取shortcode和videoname
const items = document.querySelectorAll('.item')
const itemsArray = [...items]
const itemsMap = itemsArray.map(item => {
    shortcode = item.children[0].children[0].href.match(/(?<=\/p\/).*/)[0]
    video_name_arr = item.children[1].children[1].href.match(/[^/]*\.mp4/)
    if (video_name_arr) {
        video_name = video_name_arr[0]
    } else {
        video_name = ''
    }
    return { shortcode: shortcode, video_name: video_name }
})
console.save(itemsMap, 'code_video.json')