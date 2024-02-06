import tkinter as tk
from tkinter import messagebox
import time

import tkinter as tk
import time
from tkinter import messagebox

class PomodoroTimer:
    """
    A class to represent a Pomodoro Timer.

    ...

    Attributes
    ----------
    master : tkinter.Tk
        The main window of the timer.
    work_time : int
        The duration of the work session in seconds.
    break_time : int
        The duration of the break session in seconds.
    current_time : int
        The current time remaining in the session in seconds.
    is_break : bool
        A flag indicating whether the current session is a break session.
    is_paused : bool
        A flag indicating whether the timer is currently paused.
    start_time : float
        The time at which the current session started.
    elapsed_time : float
        The time elapsed since the current session started.

    Methods
    -------
    start_timer():
        Starts the timer.
    stop_timer():
        Stops the timer and resets it to the default work session.
    pause_timer():
        Pauses the timer.
    log_timer():
        Logs the current session to a file.
    update_timer():
        Updates the timer display every second.
    """

    def __init__(self, master):
        """
        Constructs all the necessary attributes for the PomodoroTimer object.

        Parameters
        ----------
            master : tkinter.Tk
                The main window of the timer.
        """

        self.master = master
        master.title("Pomodoro Timer")

        # Set default session durations
        self.work_time = 1 * 60
        self.break_time = 1 * 60

        # Set initial session state
        self.current_time = self.work_time
        self.is_break = False
        self.is_paused = True
        self.start_time = None
        self.elapsed_time = 0

        # Create timer label
        self.timer_label = tk.Label(master, text="25:00", font=("Arial", 50))
        self.timer_label.pack(pady=20)

        # Create control buttons
        self.start_button = tk.Button(master, text="Start", command=self.start_timer, activebackground='green', activeforeground='white')
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED, activebackground='red', activeforeground='white')
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, state=tk.DISABLED, activebackground='yellow', activeforeground='white')
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.log_button = tk.Button(master, text="Log", command=self.log_timer, state=tk.DISABLED, activebackground='blue', activeforeground='white')
        self.log_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        """
        Starts the timer.
        """

        if self.is_paused:
            self.start_time = time.time() - self.elapsed_time
        else:
            self.start_time = time.time()

        self.is_paused = False
        self.update_timer()

        # Disable start button and enable other buttons
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.NORMAL)
        self.log_button.config(state=tk.DISABLED)

    def stop_timer(self):
        """
        Stops the timer and resets it to the default work session.
        """

        self.is_paused = True
        self.current_time = self.work_time
        self.is_break = False
        self.timer_label.config(text="25:00")

        # Disable all buttons except start button
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.log_button.config(state=tk.DISABLED)

    def pause_timer(self):
        """
        Pauses the timer.
        """

        self.is_paused = True
        self.elapsed_time = time.time() - self.start_time

        # Enable start and stop buttons and disable pause button
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.log_button.config(state=tk.NORMAL)

    def log_timer(self):
        """
        Logs the current session to a file.
        """

        if not self.is_paused:
            with open("pomodoro_log.txt", "a") as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

            messagebox.showinfo("Pomodoro Timer", "Pomodoro session logged!")
        else:
            messagebox.showwarning("Pomodoro Timer", "Cannot log session while timer is paused.")

    def update_timer(self):
        """
        Updates the timer display every second.
        """

        if not self.is_paused:
            self.elapsed_time = time.time() - self.start_time
            remaining_time = self.current_time - self.elapsed_time

            if remaining_time <= 0:
                self.is_break = not self.is_break

                if self.is_break:
                    self.current_time = self.break_time
                else:
                    self.current_time = self.work_time

                remaining_time = self.current_time

            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)

            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

            # Schedule the next update in 1 second
            self.master.after(1000, self.update_timer)

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
