from PIL import Image, ImageSequence
import struct

# Function to convert an RGB pixel to RGB565 format
def rgb888_to_rgb565(r, g, b):
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

# Function to process the animated GIF and generate the header file
def gif_to_header(input_gif, output_header, array_name):
    try:
        # Open the GIF
        gif = Image.open(input_gif)

        # Verify dimensions
        width, height = gif.size
        if width != 240 or height != 240:
            raise ValueError("Image dimensions must be 240x240.")

        # Prepare the header file
        with open(output_header, "w") as header:
            # Write the header guard
            header.write(f"#ifndef {array_name.upper()}_H\n")
            header.write(f"#define {array_name.upper()}_H\n\n")
            header.write("#include <avr/pgmspace.h>\n\n")

            # Write the array declaration
            header.write(f"const uint16_t {array_name}[][240*240] PROGMEM = {{\n")

            # Process each frame in the GIF
            frame_number = 0
            for frame in ImageSequence.Iterator(gif):
                frame = frame.convert("RGB")

                # Start the frame
                header.write(f"    {{   // Frame #{frame_number}")
                header.write("\n")

                # Write the RGB565 data for the frame
                for y in range(height):
                    header.write("        ")
                    row_data = []
                    for x in range(width):
                        r, g, b = frame.getpixel((x, y))

                        # print( f"r g b = {r}, {g}, {b}")
                        
                        rgb565 = rgb888_to_rgb565(r, g, b)
                        row_data.append(f"0x{rgb565:04X}")
                    header.write(", ".join(row_data))
                    header.write(",\n")

                # End the frame
                header.write("    },\n")
                frame_number += 1

            # Close the array
            header.write("};\n\n")

            # Close the header guard
            header.write(f"#endif // {array_name.upper()}_H\n")

        print(f"Header file '{output_header}' generated successfully with {frame_number} frames.")

    except Exception as e:
        print(f"Error: {e}")

# Input and output paths
input_gif = "fish.gif"  # Replace with your input GIF file name
output_header = "fish.h"  # Output header file
array_name = "fish"  # Array name

# Convert the GIF to a header file
gif_to_header(input_gif, output_header, array_name)
