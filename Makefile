
main : apps libs system others_build
		powershell del "build/SeniorOS/apps/*.py"
		powershell del "build/SeniorOS/lib/*.py"
		powershell cd "build/SeniorOS/system/"
		powershell ren "main.py" "main.bak"
		powershell del "*.py"
		powershell ren "main.bak" "main.py"
		powershell cd "../../.."
		powershell del "build/SeniorOS/style/*.py"
		powershell del "build/SeniorOS/others_build/*.py"
		powershell del "build/SeniorOS/fonts/*.py"

#apps
makepy: tools/make.py
		python tools/make.py
apps: 
		@$(foreach item,$(wildcard build/SeniorOS/apps/*.py),echo $(item) && powershell mpy-cross-v5 "$(item)")
#mpy-cross-v5 build/SeniorOS/apps/app0.py
#mpy-cross-v5 build/SeniorOS/apps/app1.py
#mpy-cross-v5 build/SeniorOS/apps/app2.py
#mpy-cross-v5 build/SeniorOS/apps/app3.py
#mpy-cross-v5 build/SeniorOS/apps/app4.py
#mpy-cross-v5 build/SeniorOS/apps/logo.py
#mpy-cross-v5 build/SeniorOS/apps/port.py

#lib
libs: $(wildcard build/SeniorOS/lib/*.py)
		mpy-cross-v5 build/SeniorOS/lib/devlib.py
		mpy-cross-v5 build/SeniorOS/lib/pages_manager.py
		mpy-cross-v5 build/SeniorOS/lib/log_manager.py
		mpy-cross-v5 build/SeniorOS/lib/BetterGui.py

system: $(wildcard build/SeniorOS/system/*.py)
		mpy-cross-v5 build/SeniorOS/system/daylight.py
		mpy-cross-v5 build/SeniorOS/system/pages.py
		mpy-cross-v5 build/SeniorOS/system/radient.py
		mpy-cross-v5 build/SeniorOS/system/ftreader.py
		mpy-cross-v5 build/SeniorOS/system/core.py
		mpy-cross-v5 build/SeniorOS/system/smart_wifi.py
		mpy-cross-v5 build/SeniorOS/system/typer.py
		mpy-cross-v5 build/SeniorOS/system/update.py
		mpy-cross-v5 build/SeniorOS/style/home.py
		mpy-cross-v5 build/SeniorOS/style/port.py
		mpy-cross-v5 build/SeniorOS/fonts/misans.py
		mpy-cross-v5 build/SeniorOS/fonts/misans_16.py

others_build: $(wildcard build/SeniorOS/others_build/*.py)
		mpy-cross-v5 build/SeniorOS/others_build/FOS_A_dev34.py
		mpy-cross-v5 build/SeniorOS/others_build/GxxkSystem.py
		mpy-cross-v5 build/SeniorOS/others_build/LP_OS_V3.py
		mpy-cross-v5 build/SeniorOS/others_build/POS2_8-9.py
		mpy-cross-v5 build/SeniorOS/others_build/POS3_230128.py
		mpy-cross-v5 build/SeniorOS/others_build/Rong_OS.py

#all:main;echo "$(SRCS)"