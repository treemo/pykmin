import yaml
import logging.config

class TagsFilter(logging.Filter):
    def filter(self, record):
        if hasattr(record, 'tags'):
            record.msg += ' Tags: %s' % repr(record.tags)
        return record