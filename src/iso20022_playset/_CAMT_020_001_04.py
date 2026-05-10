from . import base_types
from .GetGeneralBusinessInformationV04 import GetGeneralBusinessInformationV04

class CAMT_020_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetGnlBizInf"]
		@property
		def GetGnlBizInf(self):
			return self._GetGnlBizInf

		@GetGnlBizInf.setter
		def GetGnlBizInf(self, value):
			self._GetGnlBizInf = value if type(value) != base_types.auto else self.make_default("GetGnlBizInf")

		@GetGnlBizInf.deleter
		def GetGnlBizInf(self):
			del self._GetGnlBizInf
			self._GetGnlBizInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetGnlBizInf', type=GetGeneralBusinessInformationV04, min=1, max=1, mutex_group=None, array=False),
		))

