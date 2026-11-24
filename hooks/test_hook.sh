#!/bin/sh
# Run: sh hooks/test_hook.sh   (expects every line to say ok)
H="python3 $(dirname "$0")/block_unsafe_blender_python.py"
c(){ printf '%s' "$1" | $H 2>/dev/null; r=$?; [ "$r" = "$2" ] && echo "ok   $3" || echo "FAIL $3 (got $r want $2)"; }
c '{"tool_input":{"code":"import bpy\nbpy.ops.mesh.primitive_cube_add()"}}' 0 "safe cube"
c '{"tool_input":{"code":"import bpy, mathutils\nfrom math import cos\nv=cos(1); pos=obj.location"}}' 0 "safe math/pos"
c '{"tool_input":{"code":"f=open(\"//data.csv\")"}}' 0 "open for reading"
c '{"tool_input":{"code":"import bpy, os\nos.remove(\"x\")"}}' 2 "import bpy, os"
c '{"tool_input":{"code":"import subprocess"}}' 2 "subprocess"
c '{"tool_input":{"code":"from shutil import rmtree"}}' 2 "from shutil"
c '{"tool_input":{"code":"__import__(\"os\").system(\"ls\")"}}' 2 "__import__"
c '{"tool_input":{"args":{"src":"open(\"/etc/x\",\"w\")"}}}' 2 "nested open-for-write"
