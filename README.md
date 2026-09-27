# Bezier Curve for Aseprite

English | [日本語](README.ja.md)

An [Aseprite](https://www.aseprite.org/) extension that adds **curve layers**. Lines on a curve layer are drawn with Bezier curves and stay editable: select the layer and you can move the points, change how the lines bend, or change their color and width right on the canvas, at any time.

- Click and drag on the canvas, like the Pen tool in drawing apps. A small panel holds the settings
- Several lines per layer, each with its own color and width (1–32 px, round brush)
- Pixel-perfect option for clean 1px lines, or antialiasing for smooth edges (RGB and Grayscale)
- Closed shapes (connect the last point to the first), and filling the inside with a color, with or without the line
- Basic shapes to place: circles, rectangles, rounded rectangles, triangles, polygons and stars
- Each frame has its own lines
- Works with RGB, Grayscale and Indexed sprites

## Bezier Curve Pro

The paid version, **Bezier Curve Pro**, also has:

- **Transform**: scale, rotate, shear, flip and move shapes with a box on the canvas, or type exact values
- **Copy and paste**: copy shapes to other frames, layers and sprites
- **Stacking order**: bring shapes to the front or send them to the back

The store page is coming soon. Curves drawn with the free version can be edited in Pro as they are, and the other way around. Installing Pro replaces the free version.

## Installation

1. Download `bezier-curve.aseprite-extension` from the [latest release](https://github.com/MLSNKKSKK/aseprite-bezier-curve/releases/latest).
2. Double-click it (Windows, macOS), or in Aseprite choose **Edit > Preferences > Extensions > Add Extension** and pick the file.

It stays installed and is ready every time Aseprite starts. Its menus and messages are in English or Japanese, following Aseprite's language setting. To remove it, use **Uninstall** in the same Extensions page.

## Usage

Choose **Layer > New > New Curve Layer** (also in the right-click menu of the layers in the timeline). A layer named `Curve 1` is added right above the active layer. Curve layers are shown in green in the timeline, so they're easy to tell apart (curve layers made with an earlier version get the color with their next edit; a layer color you picked yourself is kept).

While a curve layer is selected, you edit its lines directly on the canvas, and a small panel opens at the right edge of the window. Zooming with the mouse wheel and scrolling with Space+drag work as usual.

| On the canvas | What it does |
| --- | --- |
| Click an empty spot | Starts a new shape, or adds a point to the end of the shape you're drawing (or the selected shape). |
| Press on an empty spot and drag | Adds a point and pulls out its handles, bending the line. |
| Click the last point of the shape you're drawing, or press **Enter** | Finishes the shape. The next click on an empty spot starts a new one. |
| Click the first point of the shape you're drawing | Closes the shape (joins its last point to the first) and finishes it. It stays selected. |
| Drag a point | Moves the point. |
| Drag a handle | Changes how the line bends. The handle on the other side turns with it, unless **One handle only** is checked. |
| Click a line | Selects its shape. Clicking a line of the selected shape adds a point there without changing its form. |
| Click inside a filled shape | Selects the shape (the one on top where fills overlap). To start a new shape on top of a fill, press **Draw New** first. |
| Drag a line, or inside a fill | Moves the whole shape. |
| Click a point | Selects it (it gets a white outline). |
| **Delete** / **Backspace** | Deletes the selected point, and selects the one before it (so pressing it again goes on with the points). When a shape is selected without a point (for example after clicking its line or fill, or closing it), deletes the whole shape. |
| **Ctrl+Z** / **Ctrl+Y** | Undo / redo. Your recent changes to the lines are undone first, then Aseprite's own history. |
| **Esc** | Cancels the drag in progress, or finishes / deselects the shape. |

While you're drawing a shape, clicks only add to that shape: other shapes can't be grabbed, so you can start on another shape's point or cross over its line. Inside fills, clicks and drags add points too (a drag pulls out a curved point). After you finish the shape, clicking another shape's line selects it for editing.

There is no "apply" step. When you select another layer or frame, or use another command (such as saving or a filter), the changes are put in Aseprite's undo history as a single step (**Edit > Undo** / Ctrl+Z). Saving applies the changes right away (the guides are never saved). After your first change, the sprite counts as modified, so closing its tab asks whether to save. Selecting the curve layer again lets you keep editing, and so does coming back after saving and reopening the file.

While you edit, the points and handles are shown on the curve layer in bright green: each point is a hollow 3×3 pixel square with the line showing in its middle (pale green for the selected point, darker green for the points of other shapes), and each handle is a dotted line ending in a filled 3×3 square. Clicking anywhere on the square of a point or a handle end grabs it.

Grayscale sprites can't show green, and neither can Indexed sprites whose palette has no green, so there the guides are black and white instead: points are hollow squares with black corners and white sides (the selected point the other way around), handles are dotted in black and white, and each handle end is a filled square with a black outline and a white center. Adding a bright green to an Indexed palette makes the guides green. They disappear when you leave the layer. Zoom in to work comfortably.

At the top of the panel are the buttons for drawing and placing new shapes, and for deleting them. Below them, the **Selected Shape** section holds the settings of the selected shape. It has two groups: **Line** for the line around the shape, and **Fill** for its inside.

| Panel | Description |
| --- | --- |
| **Draw New** | Finishes the current shape, so the next click starts a new one. |
| **Place Shape...** | Places a basic shape: a circle, rectangle, rounded rectangle, triangle, polygon or star. Choose it (and the number of corners, or the rounding), then drag on the canvas: the shape fills the box you drag, and updates while you drag. A click places it at a default size. **Same width and height** makes circles, squares and regular polygons (instead of Shift, which scripts can't read). The shape uses the settings in the panel, is closed, and can be edited like any other. Esc or Enter cancels. |
| **Delete Shape** | Deletes the selected shape. |
| **Antialias** | Smooths the edges of the line and the fill with partly transparent pixels. Where shapes overlap, they blend with each other. RGB and Grayscale only: Indexed sprites can't have partly transparent pixels, so there it's turned off. |
| **Line**: **Draw** | Turn it off to draw only the fill, without a line around it. |
| **Line**: **Color** | The line color. Starts as the current foreground color. |
| **Line**: **Width** | The line width in pixels (1–32). |
| **Line**: **Pixel-perfect** | Removes the doubled pixels at the corners of 1px lines (the shape's own points are always kept, so the corners of a square stay sharp). Not used with antialiasing. |
| **Fill**: **Fill** | Fills the inside of the shape. A shape whose ends aren't connected is filled as if they were joined by a straight line. The line is drawn on top of the fill. |
| **Fill**: **Color** | The fill color. |
| **One handle only** | Dragging a handle doesn't turn the one on the other side, so you can make sharp corners. |
| **Guides** | Shows or hides the points and handles, to check how the shapes really look. |
| **Closed** | Joins the last point of the selected shape back to the first. Connecting the ends of the shape you're drawing also finishes it (it stays selected). |
| **Delete Point** | Deletes the selected point. |
| **Round/Sharp** | Switches the selected point between round (with handles) and sharp. |
| **Undo** / **Redo** | Undo / redo your changes to the shapes. |
| **Close** | Closes the panel and stops editing the layer, so you can use Aseprite's tools on it (for example the Move tool). Closing the panel with its × button does the same. Selecting the layer again, or **Layer > Edit Curves**, starts editing again. |
| **Rasterize** | Turns the curve layer into a normal layer (see below). |
| **Help** | Opens a help window that lists what each item does (Aseprite scripts can't show tooltips). It can stay open while you edit. |

When a shape is selected, the fields show its settings and changing them changes that shape. When no shape is selected, the section is called **Next Shape** and holds the settings for the next new shape (while you draw one, it says **Drawing a Shape**).

Editing also pauses while the animation plays, and starts again when you stop it with Enter.

## Rasterizing

**Layer > Rasterize Curve Layer** (also in the timeline's right-click menu and the panel's **Rasterize** button) turns the curve layer into a normal layer. The pixels stay as they are, but the lines can no longer be edited as curves, and you can paint on the layer with Aseprite's tools. The cels are trimmed to their pixels and the green layer color is removed. **Edit > Undo** (Ctrl+Z) brings the curve layer back.

## Notes

- The lines are saved in the cels, so they're kept in `.aseprite` files. Other formats such as PNG only keep the pixels.
- If you move a curve layer with the Move tool, the lines move with it.
- New frames and copied cels keep their lines, so you can copy a frame and adjust the lines for the next pose. Linked cels share the same lines.
- If a frame of a curve layer is changed some other way (painted over by hand, a filter, and so on), it isn't editable right away, so those changes aren't lost by accident. **Layer > Edit Curves** asks first, then redraws the frame from the lines.
- Curve layers made with the earlier script version of Bezier Curve work as they are. Remove the old `Bezier Curve.lua` from your scripts folder.
- The points and handles are drawn on the curve layer itself, so layers above it can hide them, and the layer's opacity and blend mode apply to them.

## Limitations

Aseprite scripts can't draw on top of the canvas or tell which mouse button or modifier keys were used on it. That's why the points and handles are shown as pixels, and why deleting points, making sharp corners and finishing a line use the panel, the Delete key, Enter or Esc instead of right-click and Alt. Handles snap to whole pixels.

A second click right after the first can be taken as a double-click and ignored, so leave a short pause between clicks when placing points close together. (While editing, the extension turns off **Select a grid tile with double-click** in the preferences, and turns it back on afterwards.)

To rebuild the extension file from the [`src`](src) folder, run `python3 build.py`.

## Requirements

Aseprite v1.3 or later.

## Building

The extension's code is in [`src`](src). `python3 build.py` packs it (with the license) into `bezier-curve.aseprite-extension`.

## License

[MIT](LICENSE)
