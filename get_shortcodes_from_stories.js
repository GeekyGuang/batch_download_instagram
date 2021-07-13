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


let a = document.querySelectorAll('a')
let b = [...a]
let c = b.filter(i => i.href.indexOf('/p/') > 0)

const shortcodes = c.map(item => {
    shortcode_rough = item.href.match(/(?<=\/p\/).*/)[0]
    index = shortcode_rough.indexOf('/')
    shortcode = shortcode_rough.slice(0, index)
    return shortcode
})

const shortcodes_final = Array.from(new Set(shortcodes))

console.save(shortcodes_final, 'shortcodes.json')