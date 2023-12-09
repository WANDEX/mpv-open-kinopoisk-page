
function callback(success, result, error)
    if result.status == 0 then
        mp.osd_message(result.stdout, 1)
    else
        mp.osd_message(result.stdout, 8)
    end
end

function mpv_open_kinopoisk_page()
    mp.osd_message("Finding kinopoisk URL...", 10)
    local script_dir = debug.getinfo(1).source:match("@?(.*/)")
    local table = {}
    table.name = "subprocess"
    table.playback_only = false
    table.capture_stdout = true
    table.args = {"python", script_dir.."open-kinopoisk-page.py", mp.get_property("filename")}
    local cmd = mp.command_native_async(table, callback)
end

mp.add_key_binding('alt+ctrl+K', 'mpv_open_kinopoisk_page', mpv_open_kinopoisk_page)

