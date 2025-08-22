import customtkinter as ctk
import tkinter as tk


class window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1015x800")
        self.resizable(True, True)
        
        self.title("Periodic Table")
        ctk.set_appearance_mode("dark")

        # Define category colors here in __init__
        self.category_colors = {
            "diatomic_nonmetal": "#ff9999",
            "noble_gas": "#ffb3e6",
            "alkali_metal": "#ffcc99",
            "alkaline_earth_metal": "#ffeb99",
            "metalloid": "#ccff99",
            "polyatomic_nonmetal": "#99ff99",
            "post_transition_metal": "#99ffeb",
            "transition_metal": "#99ccff",
            "lanthanide": "#cc99ff",
            "actinide": "#ff99cc"
        }

        self.bg_color = "#524646"  # Fixed hex color format
        self.button_color = "#1e1e1e"
        self.accent_color = "#4fd1c5"
        self.configure(fg_color=self.bg_color)
        self.create_widgets()
        self.current_font_size = 24
    
    def create_widgets(self):
        # Create a frame for the color legend
        legend_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        legend_frame.pack(padx=10, pady=5, fill="x")

        # Create color scheme squares with labels
        for idx, (category, color) in enumerate(self.category_colors.items()):
            # Create frame for each legend item
            item_frame = ctk.CTkFrame(legend_frame, fg_color=self.bg_color)
            item_frame.grid(row=idx // 5, column=idx % 5, padx=5, pady=2)

            # Color square
            square = ctk.CTkLabel(
                item_frame,
                text="",
                width=20,
                height=20,
                fg_color=color,
                corner_radius=3
            )
            square.grid(row=0, column=0, padx=(2, 5))

            # Category label
            label = ctk.CTkLabel(
                item_frame,
                text=category.replace('_', ' ').title(),
                text_color="white",
                font=("Arial", 12)
            )
            label.grid(row=0, column=1, padx=2)

        # Create a scrollable frame for the periodic table
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=580, height=500)
        self.scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Create a frame for element details
        self.details_frame = ctk.CTkFrame(self, width=580, height=70)
        self.details_frame.pack(padx=10, pady=(0, 10), fill="x")
        
        # Create labels for element details
        self.details_label = ctk.CTkLabel(self.details_frame, text="Click on an element to see details", 
                                               font=("Arial", 16, "bold"))
        self.details_label.pack(pady=10)
        
        # Create element buttons in a grid layout
        self.create_element_buttons()
    
    def create_element_buttons(self):
        # Define element data (symbol, name, atomic_mass, category)
        self.elements = {
            1: ("H", "Hydrogen", 1.008, "diatomic_nonmetal", "1s¹"),
            2: ("He", "Helium", 4.0026, "noble_gas", "1s²"),
            3: ("Li", "Lithium", 6.94, "alkali_metal", "[He] 2s¹"),
            4: ("Be", "Beryllium", 9.0122, "alkaline_earth_metal", "[He] 2s²"),
            5: ("B", "Boron", 10.81, "metalloid", "[He] 2s² 2p¹"),
            6: ("C", "Carbon", 12.011, "polyatomic_nonmetal", "[He] 2s² 2p²"),
            7: ("N", "Nitrogen", 14.007, "diatomic_nonmetal", "[He] 2s² 2p³"),
            8: ("O", "Oxygen", 15.999, "diatomic_nonmetal", "[He] 2s² 2p⁴"),
            9: ("F", "Fluorine", 18.998, "diatomic_nonmetal", "[He] 2s² 2p⁵"),
            10: ("Ne", "Neon", 20.180, "noble_gas", "[He] 2s² 2p⁶"),
            11: ("Na", "Sodium", 22.990, "alkali_metal", "[Ne] 3s¹"),
            12: ("Mg", "Magnesium", 24.305, "alkaline_earth_metal", "[Ne] 3s²"),
            13: ("Al", "Aluminum", 26.982, "post_transition_metal", "[Ne] 3s² 3p¹"),
            14: ("Si", "Silicon", 28.085, "metalloid", "[Ne] 3s² 3p²"),
            15: ("P", "Phosphorus", 30.974, "polyatomic_nonmetal", "[Ne] 3s² 3p³"),
            16: ("S", "Sulfur", 32.06, "polyatomic_nonmetal", "[Ne] 3s² 3p⁴"),
            17: ("Cl", "Chlorine", 35.45, "diatomic_nonmetal", "[Ne] 3s² 3p⁵"),
            18: ("Ar", "Argon", 39.948, "noble_gas", "[Ne] 3s² 3p⁶"),
            19: ("K", "Potassium", 39.098, "alkali_metal", "[Ar] 4s¹"),
            20: ("Ca", "Calcium", 40.078, "alkaline_earth_metal", "[Ar] 4s²"),
            21: ("Sc", "Scandium", 44.956, "transition_metal", "[Ar] 3d¹ 4s²"),
            22: ("Ti", "Titanium", 47.867, "transition_metal", "[Ar] 3d² 4s²"),
            23: ("V", "Vanadium", 50.942, "transition_metal", "[Ar] 3d³ 4s²"),
            24: ("Cr", "Chromium", 51.996, "transition_metal", "[Ar] 3d⁵ 4s¹"),
            25: ("Mn", "Manganese", 54.938, "transition_metal", "[Ar] 3d⁵ 4s²"),
            26: ("Fe", "Iron", 55.845, "transition_metal", "[Ar] 3d⁶ 4s²"),
            27: ("Co", "Cobalt", 58.933, "transition_metal", "[Ar] 3d⁷ 4s²"),
            28: ("Ni", "Nickel", 58.693, "transition_metal", "[Ar] 3d⁸ 4s²"),
            29: ("Cu", "Copper", 63.546, "transition_metal", "[Ar] 3d¹⁰ 4s¹"),
            30: ("Zn", "Zinc", 65.38, "transition_metal", "[Ar] 3d¹⁰ 4s²"),
            31: ("Ga", "Gallium", 69.723, "post_transition_metal", "[Kr] 4s² 4p¹"),
            32: ("Ge", "Germanium", 72.630, "metalloid", "[Kr] 4s² 4p²"),
            33: ("As", "Arsenic", 74.922, "metalloid", "[Kr] 4s² 4p³"),
            34: ("Se", "Selenium", 78.971, "polyatomic_nonmetal", "[Kr] 4s² 4p⁴"),
            35: ("Br", "Bromine", 79.904, "diatomic_nonmetal", "[Kr] 4s² 4p⁵"),
            36: ("Kr", "Krypton", 83.798, "noble_gas", "[Kr] 4s² 4p⁶"),
            37: ("Rb", "Rubidium", 85.468, "alkali_metal", "[Xe] 5s¹"),
            38: ("Sr", "Strontium", 87.62, "alkaline_earth_metal", "[Xe] 5s²"),
            39: ("Y", "Yttrium", 88.906, "transition_metal", "[Xe] 4d¹ 5s²"),
            40: ("Zr", "Zirconium", 91.224, "transition_metal", "[Xe] 4d² 5s²"),
            41: ("Nb", "Niobium", 92.906, "transition_metal", "[Xe] 4d⁴ 5s¹"),
            42: ("Mo", "Molybdenum", 95.95, "transition_metal", "[Xe] 4d⁵ 5s¹"),
            43: ("Tc", "Technetium", 98.0, "transition_metal", "[Xe] 4d⁵ 5s²"),
            44: ("Ru", "Ruthenium", 101.07, "transition_metal", "[Xe] 4d⁷ 5s²"),
            45: ("Rh", "Rhodium", 102.91, "transition_metal", "[Xe] 4d⁸ 5s²"),
            46: ("Pd", "Palladium", 106.42, "transition_metal", "[Xe] 4d¹⁰"),
            47: ("Ag", "Silver", 107.87, "transition_metal", "[Xe] 4d¹⁰ 5s¹"),
            48: ("Cd", "Cadmium", 112.41, "transition_metal", "[Xe] 4d¹⁰ 5s²"),
            49: ("In", "Indium", 114.82, "post_transition_metal", "[Xe] 5s² 5p¹"),
            50: ("Sn", "Tin", 118.71, "post_transition_metal", "[Xe] 5s² 5p²"),
            51: ("Sb", "Antimony", 121.76, "metalloid", "[Xe] 5s² 5p³"),
            52: ("Te", "Tellurium", 127.60, "metalloid", "[Xe] 5s² 5p⁴"),
            53: ("I", "Iodine", 126.90, "diatomic_nonmetal", "[Xe] 5s² 5p⁵"),
            54: ("Xe", "Xenon", 131.29, "noble_gas", "[Xe] 5s² 5p⁶"),
            55: ("Cs", "Cesium", 132.91, "alkali_metal", "[Rn] 6s¹"),
            56: ("Ba", "Barium", 137.33, "alkaline_earth_metal", "[Rn] 6s²"),
            (57): ("La\n*57-71", "Lanthanum", 138.91, "lanthanide", "[Xe] 5d¹ 6s²"),
            58: ("Ce", "Cerium", 140.12, "lanthanide", "[Xe] 4f¹ 5d¹ 6s²"),
            59: ("Pr", "Praseodymium", 140.91, "lanthanide", "[Xe] 4f³ 6s²"),
            60: ("Nd", "Neodymium", 144.24, "lanthanide", "[Xe] 4f⁴ 6s²"),
            61: ("Pm", "Promethium", 145.0, "lanthanide", "[Xe] 4f⁵ 6s²"),
            62: ("Sm", "Samarium", 150.36, "lanthanide", "[Xe] 4f⁶ 6s²"),
            63: ("Eu", "Europium", 151.96, "lanthanide", "[Xe] 4f⁷ 6s²"),
            64: ("Gd", "Gadolinium", 157.25, "lanthanide", "[Xe] 4f⁷ 5d¹ 6s²"),
            65: ("Tb", "Terbium", 158.93, "lanthanide", "[Xe] 4f⁹ 6s²"),
            66: ("Dy", "Dysprosium", 162.50, "lanthanide", "[Xe] 4f¹⁰ 6s²"),
            67: ("Ho", "Holmium", 164.93, "lanthanide", "[Xe] 4f¹¹ 6s²"),
            68: ("Er", "Erbium", 167.26, "lanthanide", "[Xe] 4f¹² 6s²"),
            69: ("Tm", "Thulium", 168.93, "lanthanide", "[Xe] 4f¹³ 6s²"),
            70: ("Yb", "Ytterbium", 173.05, "lanthanide", "[Xe] 4f¹⁴ 6s²"),
            71: ("Lu", "Lutetium", 174.97, "lanthanide", "[Xe] 4f¹⁵ 6s²"),
            72: ("Hf", "Hafnium", 178.49, "transition_metal", "[Xe] 4f¹⁶ 5d² 6s²"),
            73: ("Ta", "Tantalum", 180.95, "transition_metal", "[Xe] 4f¹⁶ 5d³ 6s²"),
            74: ("W", "Tungsten", 183.84, "transition_metal", "[Xe] 4f¹⁶ 5d⁴ 6s²"),
            75: ("Re", "Rhenium", 186.21, "transition_metal", "[Xe] 4f¹⁶ 5d⁵ 6s²"),
            76: ("Os", "Osmium", 190.23, "transition_metal", "[Xe] 4f¹⁶ 5d⁶ 6s²"),
            77: ("Ir", "Iridium", 192.22, "transition_metal", "[Xe] 4f¹⁶ 5d⁷ 6s²"),
            78: ("Pt", "Platinum", 195.08, "transition_metal", "[Xe] 4f¹⁶ 5d⁸ 6s²"),
            79: ("Au", "Gold", 196.97, "transition_metal", "[Xe] 4f¹⁶ 5d¹⁰ 6s¹"),
            80: ("Hg", "Mercury", 200.59, "transition_metal", "[Xe] 4f¹⁶ 5d¹⁰ 6s²"),
            81: ("Tl", "Thallium", 204.38, "post_transition_metal", "[Xe] 6s² 6p¹"),
            82: ("Pb", "Lead", 207.2, "post_transition_metal", "[Xe] 6s² 6p²"),
            83: ("Bi", "Bismuth", 208.98, "post_transition_metal", "[Xe] 6s² 6p³"),
            84: ("Po", "Polonium", 209.0, "post_transition_metal", "[Xe] 6s² 6p⁴"),
            85: ("At", "Astatine", 210.0, "metalloid", "[Xe] 6s² 6p⁵"),
            86: ("Rn", "Radon", 222.0, "noble_gas", "[Xe] 6s² 6p⁶"),
            87: ("Fr", "Francium", 223.0, "alkali_metal", "[Rn] 7s¹"),
            88: ("Ra", "Radium", 226.0, "alkaline_earth_metal", "[Rn] 7s²"),
            89: ("Ac\n*89-103", "Actinium", 227.0, "actinide", "[Rn] 6d¹ 7s²"),
            90: ("Th", "Thorium", 232.04, "actinide", "[Rn] 6d² 7s²"),
            91: ("Pa", "Protactinium", 231.04, "actinide", "[Rn] 6d⁴ 7s²"),
            92: ("U", "Uranium", 238.03, "actinide", "[Rn] 6d⁵ 7s²"),
            93: ("Np", "Neptunium", 237.0, "actinide", "[Rn] 6d⁵ 7s²"),
            94: ("Pu", "Plutonium", 244.0, "actinide", "[Rn] 6d⁷ 7s²"),
            95: ("Am", "Americium", 243.0, "actinide", "[Rn] 6d⁷ 7s²"),
            96: ("Cm", "Curium", 247.0, "actinide", "[Rn] 6d⁸ 7s²"),
            97: ("Bk", "Berkelium", 247.0, "actinide", "[Rn] 6d⁹ 7s²"),
            98: ("Cf", "Californium", 251.0, "actinide", "[Rn] 6d¹⁰ 7s²"),
            99: ("Es", "Einsteinium", 252.0, "actinide", "[Rn] 6d¹⁰ 7s²"),
            100: ("Fm", "Fermium", 257.0, "actinide", "[Rn] 6d¹¹ 7s²"),
            101: ("Md", "Mendelevium", 258.0, "actinide", "[Rn] 6d¹² 7s²"),
            102: ("No", "Nobelium", 259.0, "actinide", "[Rn] 6d¹³ 7s²"),
            103: ("Lr", "Lawrencium", 262.0, "actinide", "[Rn] 6d¹⁴ 7s²"),
            104: ("Rf", "Rutherfordium", 267.0, "transition_metal", "[Rn] 5f¹ 6d¹ 7s²"),
            105: ("Db", "Dubnium", 270.0, "transition_metal", "[Rn] 5f¹ 6d² 7s²"),
            106: ("Sg", "Seaborgium", 271.0, "transition_metal", "[Rn] 5f¹ 6d³ 7s²"),
            107: ("Bh", "Bohrium", 270.0, "transition_metal", "[Rn] 5f¹ 6d⁴ 7s²"),
            108: ("Hs", "Hassium", 277.0, "transition_metal", "[Rn] 5f¹ 6d⁵ 7s²"),
            109: ("Mt", "Meitnerium", 276.0, "transition_metal", "[Rn] 5f¹ 6d⁶ 7s²"),
            110: ("Ds", "Darmstadtium", 281.0, "transition_metal", "[Rn] 5f¹ 6d⁷ 7s²"),
            111: ("Rg", "Roentgenium", 280.0, "transition_metal", "[Rn] 5f¹ 6d⁸ 7s²"),
            112: ("Cn", "Copernicium", 285.0, "transition_metal", "[Rn] 5f¹ 6d⁹ 7s²"),
            113: ("Nh", "Nihonium", 286.0, "post_transition_metal", "[Rn] 5f¹ 7s²"),
            114: ("Fl", "Flerovium", 289.0, "post_transition_metal", "[Rn] 5f¹ 7s²"),
            115: ("Mc", "Moscovium", 290.0, "post_transition_metal", "[Rn] 5f¹ 7s²"),
            116: ("Lv", "Livermorium", 293.0, "post_transition_metal", "[Rn] 5f¹ 7s²"),
            117: ("Ts", "Tennessine", 294.0, "metalloid", "[Rn] 5f¹ 7s²"),
            118: ("Og", "Oganesson", 294.0, "noble_gas", "[Rn] 5f¹ 7s²")
        }
        
        # Define the positions of elements in the periodic table
        element_positions = {
            # Period 1
            1: (0, 0), 2: (0, 17),
            # Period 2
            3: (1, 0), 4: (1, 1), 5: (1, 12), 6: (1, 13), 7: (1, 14), 8: (1, 15), 9: (1, 16), 10: (1, 17),
            # Period 3
            11: (2, 0), 12: (2, 1), 13: (2, 12), 14: (2, 13), 15: (2, 14), 16: (2, 15), 17: (2, 16), 18: (2, 17),
            # Period 4
            19: (3, 0), 20: (3, 1), 21: (3, 2), 22: (3, 3), 23: (3, 4), 24: (3, 5), 25: (3, 6), 26: (3, 7), 
            27: (3, 8), 28: (3, 9), 29: (3, 10), 30: (3, 11), 31: (3, 12), 32: (3, 13), 33: (3, 14), 34: (3, 15), 
            35: (3, 16), 36: (3, 17),
            # Period 5
            37: (4, 0), 38: (4, 1), 39: (4, 2), 40: (4, 3), 41: (4, 4), 42: (4, 5), 43: (4, 6), 44: (4, 7), 
            45: (4, 8), 46: (4, 9), 47: (4, 10), 48: (4, 11), 49: (4, 12), 50: (4, 13), 51: (4, 14), 52: (4, 15), 
            53: (4, 16), 54: (4, 17),
            # Period 6
            55: (5, 0), 56: (5, 1), 57: (5, 2), 72: (5, 3), 73: (5, 4), 74: (5, 5), 75: (5, 6), 76: (5, 7), 
            77: (5, 8), 78: (5, 9), 79: (5, 10), 80: (5, 11), 81: (5, 12), 82: (5, 13), 83: (5, 14), 84: (5, 15), 
            85: (5, 16), 86: (5, 17),
            # Period 7
            87: (6, 0), 88: (6, 1), 89: (6, 2), 104: (6, 3), 105: (6, 4), 106: (6, 5), 107: (6, 6), 108: (6, 7), 
            109: (6, 8), 110: (6, 9), 111: (6, 10), 112: (6, 11), 113: (6, 12), 114: (6, 13), 115: (6, 14), 116: (6, 15), 
            117: (6, 16), 118: (6, 17),
            # Lanthanides
            58: (8, 3), 59: (8, 4), 60: (8, 5), 61: (8, 6), 62: (8, 7), 63: (8, 8), 64: (8, 9), 65: (8, 10),
            66: (8, 11), 67: (8, 12), 68: (8, 13), 69: (8, 14), 70: (8, 15), 71: (8, 16),
            # Actinides
            90: (9, 3), 91: (9, 4), 92: (9, 5), 93: (9, 6), 94: (9, 7), 95: (9, 8), 96: (9, 9), 97: (9, 10),
            98: (9, 11), 99: (9, 12), 100: (9, 13), 101: (9, 14), 102: (9, 15), 103: (9, 16)
        }
        
        # Add labels for Lanthanides and Actinides
        la_label = ctk.CTkLabel(
            self.scrollable_frame,
            text="*La",
            text_color=self.accent_color,
            font=("Arial", 14, "bold")
        )
        la_label.grid(row=9, column=2, padx=2, pady=2)

        ac_label = ctk.CTkLabel(
            self.scrollable_frame,
            text="*Ac",
            text_color=self.accent_color,
            font=("Arial", 14, "bold")
        )
        ac_label.grid(row=10, column=2, padx=2, pady=2)

        #Periods
        period_labels = [
            ctk.CTkLabel(self.scrollable_frame, 
                         text=f"Period {i+1}", 
                         text_color=self.accent_color, 
                         font=("Arial", 14, "bold"))
            for i in range(7)
        ]
        for i, label in enumerate(period_labels):
            label.grid(row=i+1, column=18, padx=2, pady=2)

        # Group numbers 
        group_numbers = {
            0: "1",
            1: "2",
            2: "3",
            3: "4",
            4: "5", 
            5: "6",
            6: "7",
            7: "8",
            8: "9",
            9: "10",
            10: "11",
            11: "12",
            12: "13",
            13: "14",
            14: "15",
            15: "16",
            16: "17",
            17: "18"
        }

        # Create and position group numbers 
        for col, num in group_numbers.items():
            label = ctk.CTkLabel(
                self.scrollable_frame,
                text=num,
                text_color=self.accent_color,
                font=("Arial", 12, "bold")
            )
            label.grid(row=0, column=col, padx=2, pady=(2, 5))

        # Offset element positions by 1 row
        element_positions = {
            k: (v[0] + 1, v[1]) for k, v in element_positions.items()
        }
        
        # Create element buttons with proper positioning
        for atomic_number, (symbol, name, atomic_mass, category, electron_config) in self.elements.items():
            button_color = self.category_colors.get(category, "#ffffff")
            button = ctk.CTkButton(
                self.scrollable_frame,
                text=f"{symbol}\n{atomic_number}",  # Removed electron_config
                width=50,  # Reduced width since we removed electron_config
                height=50,  # Reduced height
                fg_color=button_color,
                text_color="black",
                font=("Arial", 12),  # Increased font size since we have less text
                hover_color=self.lighten_color(button_color),
                command=lambda an=atomic_number: self.show_element_details(an)
            )
            # Position elements according to their actual positions in the periodic table
            if atomic_number in element_positions:
                row, col = element_positions[atomic_number]
                button.grid(row=row, column=col, padx=2, pady=2)
            else:
                # Fallback for any elements not in the position map
                row = (atomic_number - 1) // 18
                col = (atomic_number - 1) % 18
                button.grid(row=row, column=col, padx=2, pady=2)
            
    def show_element_details(self, atomic_number):
        # Get element data (now includes electronic configuration)
        symbol, name, atomic_mass, category, electron_config = self.elements[atomic_number]
        
        # Update details label to include electronic configuration
        details_text = f"{name} ({symbol})\nAtomic Number: {atomic_number} | Mass: {atomic_mass:.3f}\nCategory: {category.replace('_', ' ').title()}\nElectronic Configuration: {electron_config}"
        self.details_label.configure(text=details_text)

    def lighten_color(self, hex_color, factor=0.3):
        # Convert hex to RGB
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Lighten
        rgb_new = [min(int(x + (255 - x) * factor), 255) for x in rgb]
        
        # Convert back to hex
        return '#{:02x}{:02x}{:02x}'.format(*rgb_new)
            
if __name__ == "__main__":
    app = window()
    app.mainloop()