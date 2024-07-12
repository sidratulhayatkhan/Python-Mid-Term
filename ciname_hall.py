class Star_cinema:
    hall_list=[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]
        self.entry_hall(self)

    def entry_show(self,show_id,movie_name,time):
        my_tuple=(show_id,movie_name,time)
        self.show_list.append(my_tuple)
        matrix=[[0 for _ in range(self.cols)]for _ in range(self.rows)] 
        self.seats[show_id]=matrix

    def book_seats(self,show_id,seat_list):
        if show_id not in self.seats.keys():
            print(f'{show_id} doesnt match.Give me correct id now.')
            return

        show_seats=self.seats[show_id]

        for (row,col) in seat_list:
            if row>=self.rows or col>=self.cols or row<0 or col<0:
                print(f'{row}{col} not exist give correct rows and colums')
                continue
            if show_seats[row][col]==1:
                print(f'this seat {row}{col} has already booked')
            else:
                show_seats[row][col]=1
                print(f'This seat {row}{col} has succesfully booked') 
  
    def view_show_list(self):
        if not self.show_list:
            print(f'This Show is not running yet')
            return
        print(f'For Show Details the hall_no {self.hall_no}: ')
        for show in self.show_list:
            show_id,movie_name,show_time=show
            print(f'Show_id:{show_id},Movie:{movie_name},Time:{show_time}')

    def view_available_seats(self,show_id):
        if show_id not in self.seats:
            print(f'This {show_id} seat not available here')
            return
        print(f'Available seat for {show_id}:')
        show_seats=self.seats[show_id]
        for row in range(self.rows):
            for col in range(self.cols):
                seat_status='0'if show_seats[row][col] == 0 else '1'
                print(seat_status,end=" ")
            print()

class Counter:
    def __init__(self,cinema) -> None:
        self.cinema=cinema

    def view_all_shows(self):
        if not self.cinema.hall_list:
            print(f'No halls in the movie.')
            return
        for hall in self.cinema.hall_list:
            hall.view_show_list()

    def view_seats_for_show(self,hall_no,show_id):
        hall=self._find_hall(hall_no)
        if hall:
            hall.view_available_seats(show_id)
    
    def book_tickets(self,hall_no,show_id,seat_list):
        hall=self._find_hall(hall_no)
        if hall:
            hall.book_seats(show_id,seat_list)

    def _find_hall(self,hall_no):
        for hall in self.cinema.hall_list:
            if hall.hall_no==hall_no:
                return hall
        print(f'Hall {hall_no} not exist')
        return None
    
hall1=Hall(5,5,'Chayabani')
hall2=Hall(4,4,'Purabi')
hall1.entry_show('1','Monpura','6:00')
hall1.entry_show('2','Television','9:00')
hall2.entry_show('1','Durbin','12:00')

counter=Counter(Star_cinema)

while True:
    print('\nWelcome to Star Cinema !')
    print('1. View all shows')
    print('2. View available seats for a show')
    print('3. Book Now')
    print('4. Exit')

    choice=input('Chose your option: ')

    if choice=='1':
        counter.view_all_shows()
    elif choice=='2':
        hall_no=input('hall no: ')
        show_id=input('id: ')
        counter.view_seats_for_show(hall_no,show_id)
    elif choice=='3':
        hall_no=input('hall no or name: ')
        show_id=input('id: ')
        seats=int(input('total: '))
        seat_list=[]
        for _ in range(seats):
            row=int(input('row: '))
            col=int(input('col: '))
            seat_list.append((row,col))
        counter.book_tickets(hall_no,show_id,seat_list)
    elif choice=='4':
        print('Exit.Thank you')
        break
    else:
        print('Invalid. Try after some time')    

