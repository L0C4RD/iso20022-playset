from . import base_types
from .ReturnStandingOrderV06 import ReturnStandingOrderV06

class CAMT_070_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrStgOrdr"]
		@property
		def RtrStgOrdr(self):
			return self._RtrStgOrdr

		@RtrStgOrdr.setter
		def RtrStgOrdr(self, value):
			self._RtrStgOrdr = value if type(value) != auto else self.make_default("RtrStgOrdr")

		@RtrStgOrdr.deleter
		def RtrStgOrdr(self):
			del self._RtrStgOrdr
			self._RtrStgOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrStgOrdr', type=ReturnStandingOrderV06, min=1, max=1, mutex_group=None, array=False),
		))

