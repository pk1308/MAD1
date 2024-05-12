import fitz  # Install using pip install fitz-py

def compress_pdf(input_file, output_file, quality=50, grayscale=False):
  """
  Compresses a PDF file using PyMuPDF (fitz-py).

  Args:
      input_file (str): Path to the input PDF file.
      output_file (str): Path to save the compressed PDF file.
      quality (int, optional): Compression level for JPEG images in the PDF (1-100, lower is better quality, default=None for automatic).
      grayscale (bool, optional): Convert all images to grayscale before compression (default=False).
  """

  try:
    # Open the PDF document
    doc = fitz.open(input_file)

    # Iterate through all pages
    for page in doc:
      # Compress images (if any)
      xref = page.get_xref()
      for block_id in xref:
        if fitz.IMAGE in fitz.IMAGE_LIST[xref[block_id][1]]:
          # Extract image data
          xreff = xref[block_id]
          image_data = xref["stream"]

          # Apply compression (if quality is provided)
          if quality:
            image = fitz.open_image_stream(image_data, fmt="JPEG")
            new_data = image.compress(quality=quality)
          else:
            new_data = image_data

          # Update image stream with compressed data
          xref["stream"] = new_data

      # Convert to grayscale (optional)
      if grayscale:
        pix = page.get_pixmap()
        pix = pix.convert("GRAY")
        page.set_pixmap(pix)

    # Save the compressed PDF
    doc.save(output_file)
    print(f"PDF compressed successfully: {output_file}")

  except Exception as e:
    print(f"Error compressing PDF: {e}")
if __name__ == "__main__":

    # Example usage:
    input_file = "/home/pk/Desktop/gitmaster/DBMS/docs/arifacts/Abraham Silberschatz, Henry Korth, S. Sudarshan - Database System Concepts-McGraw-Hill Education (2019)-30-33.pdf"
    output_file = "compressed.pdf"
    quality = 75  # Adjust quality as needed (1-100)
    grayscale = True  # Set to True to convert images to grayscale

    compress_pdf(input_file, output_file, quality, grayscale)
