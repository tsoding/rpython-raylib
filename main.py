import os
from rpython.rtyper.lltypesystem import rffi
from rpython.translator.tool.cbuild import ExternalCompilationInfo

# help(rffi.lltype);
# exit(69);

info = ExternalCompilationInfo(
    include_dirs=[os.path.abspath("./raylib-5.0_linux_amd64/include/")],
    includes=["raylib.h"],
    library_dirs=[os.path.abspath("./raylib-5.0_linux_amd64/lib/")],
    libraries=[":libraylib.a", "m"]
    # libraries=["raylib", "m"]
)

InitWindow = rffi.llexternal(
    name = "InitWindow", args = [rffi.INT, rffi.INT, rffi.CCHARP], result = rffi.lltype.Void, compilation_info=info
)
WindowShouldClose = rffi.llexternal(
    name = "WindowShouldClose", args = [], result = rffi.lltype.Bool, compilation_info=info
)
BeginDrawing = rffi.llexternal(
    name = "BeginDrawing", args = [], result = rffi.lltype.Void, compilation_info=info
)
EndDrawing = rffi.llexternal(
    name = "EndDrawing", args = [], result = rffi.lltype.Void, compilation_info=info
)

# __________  Entry point  __________

def entry_point(argv):
    InitWindow(800, 600, "Hello from RPython")
    while not WindowShouldClose():
        BeginDrawing()
        EndDrawing()
    return 0

# _____ Define and setup target ___

def target(driver, args):
    driver.exe_name = "urmom"
    print dir(driver.config)
    return entry_point
