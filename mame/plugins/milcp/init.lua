local exports = {}
exports.name = "milcp"
exports.version = "0.0.1"
exports.description = "MAME Input LEDs Controller Plugin"
exports.license = "GNU Lesser General Public License v3.0"
exports.author = "Marchah"

local inputController = exports
local json = require('json')

function getConfigPath()
	local file = io.open(manager:machine():options().entries.pluginspath:value() .. "/milcp/mapping.json", "r")
	if not file then
		print("Roms mapping not found")
		return nil
	end
	local data = file:read("*a")
	file:close()
	local mapping = json.parse(data)
	local filename = mapping[emu.romname()]
	if not filename then
    manager:machine():popmessage(_("Rom " .. emu.romname() .. " not supported yet !"))
		return nil
	end
	return manager:machine():options().entries.pluginspath:value() .. "/milcp/config/" .. filename .. ".json"
end

function inputController.startplugin()
	emu.register_start(function()
		emu.print_verbose("Starting " .. emu.gamename())

		local configPath = getConfigPath()
		if not configPath then
			return
		end

		os.execute("python " .. manager:machine():options().entries.pluginspath:value() .. "/milcp/startQuery.py " .. emu.romname() .." "  .. configPath)
	end)

	emu.register_stop(function()
		emu.print_verbose("Exiting " .. emu.gamename())

		os.execute("python " .. manager:machine():options().entries.pluginspath:value() .. "/milcp/endQuery.py " .. emu.romname())
	end)
end

return exports
