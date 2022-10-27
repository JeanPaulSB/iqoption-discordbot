# IQOPTION DISCORD BOT
**- Programming language: Python**<br>
**- Author: JeanPaulSB**<br>
**- Current stage: Alpha**
# Main features
- Allows you to schedule operations at specific timestamps
- Automated Martin Gala algorithm
- Offers you a visual approach when interacting with the Iq option broker
- Customizable 
- Efficiency, since all the operations are performed instantanously
- Easy to get into

# Commands:
**All the commands start with the '$' prefix!**

## Account related commands:
### - $log iqemail password
    - description : it logs into you the IQOPTION broker (required for any command)
### - $real
    - description : sets your account to the real mode
### - $pratice
    - description : sets your account to the practice mode
### - $checkmode
    - description : returns the current account mode
### - $balance
    - description : it returns your balance in the current account mode
### - $setmgON
    - description : turns ON martin gala algorithm
### - $setmgOFF
    - description : turns OFF martin gala algorithm
### - $checkmg 
    - description : returns the martin gala user's preference current status (ON/OFF)
## Operations related commands:
### - $signal money active direction expiration
    - description : buys instantaneously an active with the specified parameters
    - example: $signal 5 AUDUSD put 1
### - $schedulesignal money active direction expiration timestamp
    - description : allows you to schedule an operation at a specific timestamp
    - note: is almost the same as $signal except that it needs a timestamp argument in 24hr format
    - example: $schedulesignal 10 AUDUSD call 3 19:05
### - $getscheduleds
    - description : returns all your scheduled operations
### - $getopen
    - description : returns your current active operations
### - $getclosed:
    - description : returns your five last operations with its results
## Misc commands
### - $now
    - description : returns current time (GMT -5:00)
