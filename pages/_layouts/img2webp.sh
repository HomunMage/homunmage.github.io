#!/bin/bash

# Recursively find all .png and .jpg files under the current directory,
# but skip anything under ./_site
find . -path "./_site" -prune -o \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) -print0 | while IFS= read -r -d $'\0' file; do
  # Get the directory path of the file
  dirpath=$(dirname "$file")
  # Get the filename without the extension
  filename=$(basename "$file" | sed 's/\.[^.]*$//')
  # Generate the output filename with .webp extension
  output_filename="${dirpath}/${filename}.webp"

  # Skip if .webp already exists (avoids ffmpeg overwrite prompt)
  if [ -f "$output_filename" ]; then
    echo "Skipping \"$file\" (\"$output_filename\" already exists)"
    continue
  fi

  # Convert .png/.jpg to .webp.
  # -nostdin: ffmpeg must NOT read from stdin — otherwise it eats bytes from
  # the find -print0 pipe and silently skips files in the while-read loop.
  # -y: auto-confirm any overwrite (belt-and-braces even with the skip above).
  echo "Converting \"$file\" to \"$output_filename\"..."
  ffmpeg -nostdin -y -i "$file" "$output_filename" </dev/null

  # Check if ffmpeg command was successful
  if [ $? -eq 0 ]; then
    echo "Successfully converted \"$file\""
  else
    echo "Error converting \"$file\""
  fi
done
