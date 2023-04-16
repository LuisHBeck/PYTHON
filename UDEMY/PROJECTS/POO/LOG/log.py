from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log():
    def _log(self, msg: str):
        raise NotImplementedError("Inplement the log method")
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg: str):
        formated_msg = f'{msg} ({self.__class__.__name__})'
        print(f'Saving to log: {formated_msg}')
        with open(LOG_FILE, 'a') as archive:
            archive.write(formated_msg)
            archive.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg: str):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error('anything')
    lp.log_success('something')

    lf = LogFileMixin()
    lf.log_error('anything')
    lf.log_success('something')
    