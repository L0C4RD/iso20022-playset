from . import base_types
from .ATMRejectV02 import ATMRejectV02

class CATP_005_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMRjct"]
		@property
		def ATMRjct(self):
			return self._ATMRjct

		@ATMRjct.setter
		def ATMRjct(self, value):
			self._ATMRjct = value if type(value) != auto else self.make_default("ATMRjct")

		@ATMRjct.deleter
		def ATMRjct(self):
			del self._ATMRjct
			self._ATMRjct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRjct', type=ATMRejectV02, min=1, max=1, mutex_group=None, array=False),
		))

