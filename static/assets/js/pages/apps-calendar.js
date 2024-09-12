class Calendar {
    constructor() {
        this.body = document.body;
        this.calendar = document.getElementById("calendar");
        this.formEvent = document.getElementById("forms-event");
        this.btnNewEvent = document.getElementById("btn-new-event");
        this.btnDeleteEvent = document.getElementById("btn-delete-event");
        this.btnSaveEvent = document.getElementById("btn-save-event");
        this.calendarObj = null;
        this.selectedEvent = null;
        this.newEventData = null;
    }

    onEventClick(e) {
        this.formEvent?.reset();
        this.formEvent.classList.remove("was-validated");
        this.newEventData = null;
        this.btnDeleteEvent.style.display = "block";
        this.selectedEvent = e.event;
        document.getElementById("event-title").value = this.selectedEvent.title;
        document.getElementById("event-category").value = this.selectedEvent.classNames[0];
    }

    // Function to fetch all events from the server
    fetchAllEvents() {
        return fetch('/all_events/')  // Your Django view that returns the events as JSON
            .then(response => response.json())
            .then(data => {
                // Transform the fetched events to FullCalendar's format
                return data.map(event => ({
                    title: event.name,
                    start: event.date + 'T' + event.start_time,  // Combine date and time
                    end: event.date + 'T' + event.end_time,
                    className: 'bg-primary',  // You can adjust the class based on the event
                }));
            })
            .catch(error => {
                console.error('Error fetching events:', error);
                return [];  // Return an empty array if there was an error
            });
    }

    async init() {
        const t = this;
        const fetchedEvents = await this.fetchAllEvents();  // Fetch events before initializing the calendar

        // Initialize the calendar
        t.calendarObj = new FullCalendar.Calendar(t.calendar, {
            plugins: [],
            slotDuration: "00:30:00",
            slotMinTime: "07:00:00",
            slotMaxTime: "19:00:00",
            themeSystem: "default",
            buttonText: {
                today: "Today",
                month: "Month",
                week: "Week",
                day: "Day",
                list: "List",
                prev: "Prev",
                next: "Next"
            },
            initialView: "dayGridMonth",
            handleWindowResize: true,
            height: window.innerHeight - 300,
            headerToolbar: {
                left: "prev,next today",
                center: "title",
                right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth"
            },
            events: fetchedEvents,  // Load fetched events here
            editable: true,
            droppable: true,
            selectable: true,
            eventClick: function (e) {
                t.onEventClick(e);
            }
        });

        t.calendarObj.render();  // Render the calendar
    }
}

document.addEventListener("DOMContentLoaded", function () {
    (new Calendar()).init();  // Initialize the Calendar class when the DOM is fully loaded
});
