from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform

class VolumeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        btn_up = Button(text='Volume UP', font_size=40, background_color=(0.2, 0.6, 1, 1))
        btn_up.bind(on_press=self.volume_up)
        
        btn_down = Button(text='Volume DOWN', font_size=40, background_color=(1, 0.3, 0.3, 1))
        btn_down.bind(on_press=self.volume_down)
        
        layout.add_widget(btn_up)
        layout.add_widget(btn_down)
        return layout

    def volume_up(self, instance):
        if platform == 'android':
            from jnius import autoclass
            Context = autoclass('android.content.Context')
            AudioManager = autoclass('android.media.AudioManager')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            audio_manager = PythonActivity.mActivity.getSystemService(Context.AUDIO_SERVICE)
            audio_manager.adjustStreamVolume(AudioManager.STREAM_MUSIC, AudioManager.ADJUST_RAISE, AudioManager.FLAG_SHOW_UI)

    def volume_down(self, instance):
        if platform == 'android':
            from jnius import autoclass
            Context = autoclass('android.content.Context')
            AudioManager = autoclass('android.media.AudioManager')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            audio_manager = PythonActivity.mActivity.getSystemService(Context.AUDIO_SERVICE)
            audio_manager.adjustStreamVolume(AudioManager.STREAM_MUSIC, AudioManager.ADJUST_LOWER, AudioManager.FLAG_SHOW_UI)

if __name__ == '__main__':
    VolumeApp().run()
