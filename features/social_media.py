def socials_cmd(username=None):
    # if user didn't provide username with command
    if not username:
        username = input("Enter username to hack: ").strip()
        if not username:
            print("No username provided. Aborting.")
            return

    # confirmation after receiving username
    ans = input(f"Proceed with simulated socials flow for '{username}'? (y/n): ").strip().lower()
    if not ans or ans[0] != "y":
        print("Cancelled.")
        return

    print(f"Starting hack on {username}...")
