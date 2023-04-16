from log import LogPrintMixin, LogFileMixin

class Electronic():
    def __init__(self, name) -> None:
        self._name = name
        self._on = False

    def turn_on(self):
        if not self._on:
            self._on = True
        
    def turn_off(self):
        if self._on:
            self._on = False


class Smartphone(Electronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._on:
            msg = f"{self._name} it's on"
            self.log_success(msg)

    def turn_off(self):
        super().turn_off()

        if not self._on:
            msg = f"{self._name} it's off"
            self.log_error(msg)
