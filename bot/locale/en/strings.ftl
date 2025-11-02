no = No

user-info =
    Name: { $name }
    ID: { NUMBER($id, useGrouping: 0) }
    Username: { $username }

user-banned =
    ID { NUMBER($id, useGrouping: 0) } added to banned list.
    When trying to send a message, the user will receive a notification that they are blocked.

user-shadowbanned =
    ID { NUMBER($id, useGrouping: 0) } added to shadowbanned list.
    When trying to send a message, the user will not know they are blocked.

user-unbanned = ID { NUMBER($id, useGrouping: 0) } unbanned.

no-banned = No banned users.

list-banned-title = Banned users list:

list-shadowbanned-title = Shadowbanned users list:

sent-confirmation = Message sent!

intro =
    Hello! 👋
    I am a support assistant. Through me you can contact technical support and get help with any questions.
    To do this, simply write your question in full in the chat <3