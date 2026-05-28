use std::env;
fn main(){
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("[-] Error: No tsrget specified.");
        println!("[*] Usage: ./target <IP_ADDRESS>");
        return;
    }
    let target_ip = &args[1];
    println!("[+] Weapon armed. Locking onto target: {}", target_ip);
}



