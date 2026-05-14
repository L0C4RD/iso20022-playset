from . import base_types
from ._PaymentInstrument29Choice import PaymentInstrument29Choice

class PaymentTransaction180(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrm"]
	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != base_types.auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrument29Choice, min=1, max=1, mutex_group=None, array=False),
	))

