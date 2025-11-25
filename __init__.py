"""
ComfyUI Floating Preview (Picture-in-Picture)
A floating, movable preview window that stays visible while you work on your workflow.
"""

# This file is minimal - all the magic happens in the JavaScript extension
# We just need to tell ComfyUI that this extension exists

WEB_DIRECTORY = "./js"

# Add empty NODE_CLASS_MAPPINGS to prevent "Skip" warning
# (This is NOT a node, it's a UI extension, but this silences the message)
NODE_CLASS_MAPPINGS = {}

__all__ = ['WEB_DIRECTORY', 'NODE_CLASS_MAPPINGS']

print("✅ Floating Preview Extension: Loaded")
print("   Ctrl+Alt+P: Toggle preview | Ctrl+Alt+[+/-]: Opacity")