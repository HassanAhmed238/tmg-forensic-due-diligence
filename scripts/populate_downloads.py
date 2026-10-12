import os, shutil

src_root = r"F:\Mr Hesham\TMG"
dest_downloads = r"F:\Mr Hesham\TMG\downloads"
os.makedirs(dest_downloads, exist_ok=True)

files_to_copy = [
    (r"TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx", r"TMG_Key_Risk_Assessments_and_Weibull_Analysis.xlsx"),
    (r"TMG_Master_Forensic_Audit_Model.xlsx", r"TMG_Master_Forensic_Audit_Model.xlsx"),
    (os.path.join("RISK", "TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx"), r"TMG_Audited_Balance_Sheet_and_Financial_Analysis.xlsx"),
    (os.path.join("RISK", "Balance sheet and TMG Real Data.xlsx"), r"TMG_Balance_Sheet_and_Real_Data.xlsx"),
    (os.path.join("RISK", "TMG_Project_Companies_Contacts_One_Sheet.xlsx"), r"TMG_Project_Companies_Contacts_One_Sheet.xlsx"),
    (r"TMG_Company_Relationships_Database_AR.xlsx", r"TMG_Company_Relationships_Database_AR.xlsx"),
    (os.path.join("RISK", "TMG_Deep_Research_Contractor_Network.xlsx"), r"TMG_Deep_Research_Contractor_Network.xlsx"),
    (os.path.join("RISK", "tmg_swot_analysis.xlsx"), r"TMG_SWOT_and_TOWS_Analysis.xlsx")
]

for src_rel, dest_name in files_to_copy:
    src_full = os.path.join(src_root, src_rel)
    dest_full = os.path.join(dest_downloads, dest_name)
    if os.path.exists(src_full):
        shutil.copy2(src_full, dest_full)
        size_kb = os.path.getsize(dest_full) / 1024
        print(f"Copied {dest_name} ({size_kb:.1f} KB)")
    else:
        print(f"Warning: {src_full} not found")
