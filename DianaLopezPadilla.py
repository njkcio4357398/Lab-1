def vote_menu():
    option = ""
    while option not in ['v', 'x']:
        print('\nVOTE MENU')
        print('v: Vote')
        print('x: Exit')
        option = input('Option: ').strip().lower()
        if option not in ['v', 'x']:
            print('\nInvalid option. Please enter "v" to vote or "x" to exit.')
    return option


def candidate_menu():
    choice = ""
    while choice not in ['1', '2', '3']:
        print('\nCANDIDATE MENU:')
        print('1: Bianca')
        print('2: Edward')
        print('3: Felicia')
        choice = input('Option: ').strip()
        if choice not in ['1', '2', '3']:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
    return choice


def main():
    votes = {'Bianca': 0, 'Edward': 0, 'Felicia': 0}

    option = vote_menu()
    while option == 'v':
        choice = candidate_menu()
        if choice == '1':
            votes['Bianca'] += 1
            print('Voted Bianca.')
        elif choice == '2':
            votes['Edward'] += 1
            print('Voted Edward.')
        elif choice == '3':
            votes['Felicia'] += 1
            print('Voted Felicia.')

        option = vote_menu()

    print('\nFinal Votes:')
    total_votes = sum(votes.values())
    for candidate, count in votes.items():
        print(f'{candidate}: {count} votes')
    print(f'Grand Total: {total_votes} votes')


if __name__ == "__main__":
    main()
