function callback(success, result, error)
    if result.status == 0 then
        mp.osd_message("Launched browser", 1)
    else
        mp.osd_message("Unable to find kinopoisk URL", 3)
    end
end

function launch_kinopoisk()
    mp.osd_message("Finding kinopoisk URL...", 30)
    local script_dir = debug.getinfo(1).source:match("@?(.*/)")
    local table = {}
    table.name = "subprocess"
    table.args = {"python", script_dir.."open-kinopoisk-page.py", mp.get_property("filename")}
    local cmd = mp.command_native_async(table, callback)
end

-- change key binding as desired
mp.add_forced_key_binding('alt+ctrl+K', 'launch_kinopoisk', launch_kinopoisk)

