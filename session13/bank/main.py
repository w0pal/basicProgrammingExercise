from banksystem import BankSystem
import createAccount
import deposit
import withdraw
import checkBalance

def main():
    bank_system = BankSystem()
    
    while True:
        print("\nBanking System Menu:")
        print("1. Buat Rekening")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Periksa Saldo")
        print("5. Keluar")
        
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            createAccount.create_account(bank_system)
        elif choice == '2':
            deposit.deposit(bank_system)
        elif choice == '3':
            withdraw.withdraw(bank_system)
        elif choice == '4':
            checkBalance.check_balance(bank_system)
        elif choice == '5':
            print("Terima kasih telah menggunakan sistem perbankan kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
