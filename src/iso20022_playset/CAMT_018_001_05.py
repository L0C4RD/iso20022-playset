from . import base_types
from .GetBusinessDayInformationV05 import GetBusinessDayInformationV05

class CAMT_018_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetBizDayInf"]
		@property
		def GetBizDayInf(self):
			return self._GetBizDayInf

		@GetBizDayInf.setter
		def GetBizDayInf(self, value):
			self._GetBizDayInf = value if type(value) != auto else self.make_default("GetBizDayInf")

		@GetBizDayInf.deleter
		def GetBizDayInf(self):
			del self._GetBizDayInf
			self._GetBizDayInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetBizDayInf', type=GetBusinessDayInformationV05, min=1, max=1, mutex_group=None, array=False),
		))

