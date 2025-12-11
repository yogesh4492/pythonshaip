import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json
import csv

class JSONExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Field Extractor")
        self.root.geometry("800x600")
        
        self.json_data = None
        self.json_file_path = None
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File selection
        ttk.Label(main_frame, text="Select JSON File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.file_label = ttk.Label(main_frame, text="No file selected", foreground="gray")
        self.file_label.grid(row=0, column=1, sticky=tk.W, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.load_json).grid(row=0, column=2, padx=5)
        
        # Available fields display
        ttk.Label(main_frame, text="Available Fields:").grid(row=1, column=0, sticky=tk.NW, pady=10)
        
        fields_frame = ttk.Frame(main_frame)
        fields_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.fields_listbox = tk.Listbox(fields_frame, selectmode=tk.MULTIPLE, height=10)
        self.fields_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(fields_frame, orient=tk.VERTICAL, command=self.fields_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.fields_listbox.config(yscrollcommand=scrollbar.set)
        
        # Field input for nested fields
        ttk.Label(main_frame, text="Or enter field path (e.g., user.name):").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.field_entry = ttk.Entry(main_frame, width=40)
        self.field_entry.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        ttk.Button(buttons_frame, text="Extract to CSV", command=self.extract_to_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Extract to JSON", command=self.extract_to_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Preview", command=self.preview_data).pack(side=tk.LEFT, padx=5)
        
        # Output preview
        ttk.Label(main_frame, text="Preview:").grid(row=5, column=0, sticky=tk.NW, pady=5)
        
        preview_frame = ttk.Frame(main_frame)
        preview_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.preview_text = tk.Text(preview_frame, height=10, wrap=tk.WORD)
        self.preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        preview_scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=self.preview_text.yview)
        preview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.preview_text.config(yscrollcommand=preview_scrollbar.set)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)
    
    def load_json(self):
        file_path = filedialog.askopenfilename(
            title="Select JSON file",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.json_data = json.load(f)
                
                self.json_file_path = file_path
                self.file_label.config(text=file_path.split('/')[-1], foreground="black")
                self.populate_fields()
                messagebox.showinfo("Success", "JSON file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load JSON file:\n{str(e)}")
    
    def populate_fields(self):
        self.fields_listbox.delete(0, tk.END)
        
        if self.json_data:
            fields = self.get_all_fields(self.json_data)
            for field in sorted(fields):
                self.fields_listbox.insert(tk.END, field)
    
    def get_all_fields(self, data, prefix=''):
        fields = set()
        
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{prefix}.{key}" if prefix else key
                fields.add(current_path)
                if isinstance(value, (dict, list)):
                    fields.update(self.get_all_fields(value, current_path))
        elif isinstance(data, list) and data:
            fields.update(self.get_all_fields(data[0], prefix))
        
        return fields
    
    def get_nested_value(self, data, path):
        keys = path.split('.')
        value = data
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            elif isinstance(value, list) and value:
                value = value[0].get(key) if isinstance(value[0], dict) else None
            else:
                return None
            
            if value is None:
                return None
        
        return value
    
    def extract_fields(self):
        if not self.json_data:
            messagebox.showwarning("Warning", "Please load a JSON file first!")
            return None
        
        selected_indices = self.fields_listbox.curselection()
        manual_field = self.field_entry.get().strip()
        
        fields = [self.fields_listbox.get(i) for i in selected_indices]
        if manual_field:
            fields.append(manual_field)
        
        if not fields:
            messagebox.showwarning("Warning", "Please select or enter at least one field!")
            return None
        
        return fields
    
    def extract_to_csv(self):
        fields = self.extract_fields()
        if not fields:
            return
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if save_path:
            try:
                data_list = self.json_data if isinstance(self.json_data, list) else [self.json_data]
                
                with open(save_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    
                    for item in data_list:
                        row = {field: self.get_nested_value(item, field) for field in fields}
                        writer.writerow(row)
                
                messagebox.showinfo("Success", f"Data extracted to {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export CSV:\n{str(e)}")
    
    def extract_to_json(self):
        fields = self.extract_fields()
        if not fields:
            return
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if save_path:
            try:
                data_list = self.json_data if isinstance(self.json_data, list) else [self.json_data]
                
                extracted_data = []
                for item in data_list:
                    row = {field: self.get_nested_value(item, field) for field in fields}
                    extracted_data.append(row)
                
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(extracted_data, f, indent=2)
                
                messagebox.showinfo("Success", f"Data extracted to {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export JSON:\n{str(e)}")
    
    def preview_data(self):
        fields = self.extract_fields()
        if not fields:
            return
        
        self.preview_text.delete(1.0, tk.END)
        
        try:
            data_list = self.json_data if isinstance(self.json_data, list) else [self.json_data]
            
            preview_data = []
            for i, item in enumerate(data_list[:5]):  # Preview first 5 items
                row = {field: self.get_nested_value(item, field) for field in fields}
                preview_data.append(row)
            
            preview_text = json.dumps(preview_data, indent=2)
            self.preview_text.insert(1.0, preview_text)
            
            if len(data_list) > 5:
                self.preview_text.insert(tk.END, f"\n\n... (showing 5 of {len(data_list)} items)")
        except Exception as e:
            self.preview_text.insert(1.0, f"Error generating preview:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONExtractorGUI(root)
    root.mainloop()