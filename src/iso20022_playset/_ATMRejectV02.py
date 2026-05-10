from . import base_types
from ._Header33 import Header33
from ._ATMReject2 import ATMReject2

class ATMRejectV02(base_types._BaseFieldType):

	__slots__ = ["_ATMRjct", "_Hdr"]
	@property
	def ATMRjct(self):
		return self._ATMRjct

	@ATMRjct.setter
	def ATMRjct(self, value):
		self._ATMRjct = value if type(value) != base_types.auto else self.make_default("ATMRjct")

	@ATMRjct.deleter
	def ATMRjct(self):
		del self._ATMRjct
		self._ATMRjct = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMRjct', type=ATMReject2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header33, min=1, max=1, mutex_group=None, array=False),
	))

