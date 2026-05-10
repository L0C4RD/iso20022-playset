from . import base_types
from ._ReturnBusinessDayInformationV07 import ReturnBusinessDayInformationV07

class CAMT_019_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrBizDayInf"]
		@property
		def RtrBizDayInf(self):
			return self._RtrBizDayInf

		@RtrBizDayInf.setter
		def RtrBizDayInf(self, value):
			self._RtrBizDayInf = value if type(value) != base_types.auto else self.make_default("RtrBizDayInf")

		@RtrBizDayInf.deleter
		def RtrBizDayInf(self):
			del self._RtrBizDayInf
			self._RtrBizDayInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrBizDayInf', type=ReturnBusinessDayInformationV07, min=1, max=1, mutex_group=None, array=False),
		))

