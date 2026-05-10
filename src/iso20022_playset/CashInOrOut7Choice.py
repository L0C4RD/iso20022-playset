import base_types
import PaymentInstrument21Choice
import PaymentInstrument20Choice

class CashInOrOut7Choice(base_types._BaseFieldType):

	__slots__ = ["_CshOutPmtInstrm", "_CshInPmtInstrm"]
	@property
	def CshOutPmtInstrm(self):
		return self._CshOutPmtInstrm

	@CshOutPmtInstrm.setter
	def CshOutPmtInstrm(self, value):
		self._CshOutPmtInstrm = value if type(value) != auto else self.make_default("CshOutPmtInstrm")

	@CshOutPmtInstrm.deleter
	def CshOutPmtInstrm(self):
		del self._CshOutPmtInstrm
		self._CshOutPmtInstrm = None

	@property
	def CshInPmtInstrm(self):
		return self._CshInPmtInstrm

	@CshInPmtInstrm.setter
	def CshInPmtInstrm(self, value):
		self._CshInPmtInstrm = value if type(value) != auto else self.make_default("CshInPmtInstrm")

	@CshInPmtInstrm.deleter
	def CshInPmtInstrm(self):
		del self._CshInPmtInstrm
		self._CshInPmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshOutPmtInstrm', type=PaymentInstrument21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshInPmtInstrm', type=PaymentInstrument20Choice, min=0, max=1, mutex_group=1, array=False),
	))

