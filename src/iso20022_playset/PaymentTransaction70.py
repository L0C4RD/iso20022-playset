import base_types
import PaymentInstrument20Choice

class PaymentTransaction70(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrm"]
	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrument20Choice, min=1, max=1, mutex_group=None, array=False),
	))

