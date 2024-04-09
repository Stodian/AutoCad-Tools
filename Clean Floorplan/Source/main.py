import sys
import ezdxf
import os

def process_dxf_file(file_path):
    # Load the DXF file
    doc = ezdxf.readfile(file_path)
    
    # Example operation: Remove 'A-Dimensions' layer if it exists
    if doc.layers.has('A-Dimensions'):
        doc.layers.remove('A-Dimensions')
    
    # Create a new folder for the modified file
    base_name = os.path.basename(file_path)
    new_folder_name = f"{os.path.splitext(base_name)[0]} - Stripped"
    new_folder_path = os.path.join(os.path.dirname(file_path), new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    
    # Define the new file path for the modified DXF
    new_file_path = os.path.join(new_folder_path, base_name)
    
    # Save the modified DXF file
    doc.saveas(new_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scriptname.py <path to DXF file>")
        sys.exit(1)
    
    dxf_file_path = sys.argv[1]
    process_dxf_file(dxf_file_path)
