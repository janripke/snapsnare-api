from datetime import datetime


class EpochTime:

    @classmethod
    def epochtime(cls, datetime_):
        return int(datetime.timestamp(datetime_) * 1000)

    @classmethod
    def from_epochtime(cls, epochtime_):
        return datetime.fromtimestamp(epochtime_ / 1000)
