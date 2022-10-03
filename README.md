# Emoji pic
Converts a colour image (png, jpeg, etc*) into a grid of emoji characters as a low-resolution version of the image.

*Supported image types are png, jpeg, and the rest of the formats supported by `imageio`.

## Requirements
Please install the following `python3` packages using `pip`:  
* `imageio`  
* `numpy`

## Example usage

### Input
The program can be run using just two arguments, the following command is given as an example:  
```
python3 emoji_pic.py aus_flag.png 40
```  
Where `aus_flag.png` is an image of that Australian national flag, in the current directory, and `40` is the number of columns that'll be filled in each row of emojis.  
<b>Note</b>: the number of rows is decided automatically based on the image's dimensions and the requested number of columns.

### Output
The below shows a `40`-column emoji version of the requested image - change the resolution as needed.  

```
🟫⬜⬜🟦🟦🟦🟦🟦⬜🟥🟥⬜🟦🟦🟦🟦🟦🟫🟫⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟫🟫⬜⬜🟦🟦🟦⬜🟥🟥⬜🟦🟦🟦🟫🟫⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟫🟫⬜⬜🟦⬜🟥🟥⬜🟦🟫🟫⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬜⬜🟫🟫🟦⬜🟥🟥⬜🟦⬜⬜🟫🟫🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜🟦🟦🟦🟦🟦
🟦⬜⬜🟫🟫🟦🟦🟦⬜🟥🟥⬜🟦🟦🟦⬜⬜🟫🟫🟦🟦🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
⬜🟫🟫🟦🟦🟦🟦🟦⬜🟥🟥⬜🟦🟦🟦🟦🟦⬜⬜🟫🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
```
<b>Note</b>: The above can appear jagged in some viewers due to inconsistent representation of `⬜`.
