import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kivy.require('1.11.1')

Builder.load_string('''
<TimePickerRoot>:
    time_picker: time_picker
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        Label:
            text: 'Select Time:'
        TimePicker:
            id: time_picker
            on_time: root.on_time_select(time_picker.time)
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        Button:
            text: 'OK'
            on_release: root.dismiss()
''')

class TimePickerRoot(BoxLayout):
    time_picker = ObjectProperty()

    def __init__(self, **kwargs):
        super(TimePickerRoot, self).__init__(**kwargs)

    def on_time_select(self, time):
        print('Selected time: ', str(time))

class TimePickerApp(App):
    def build(self):
        return TimePickerRoot()

if __name__ == '__main__':
    TimePickerApp().run()
