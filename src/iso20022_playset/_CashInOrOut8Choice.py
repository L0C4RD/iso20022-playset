from . import base_types
from ._PaymentInstrument28Choice import PaymentInstrument28Choice
from ._PaymentInstrument30Choice import PaymentInstrument30Choice

class CashInOrOut8Choice(base_types._BaseFieldType):

	__slots__ = ["_CshInPmtInstrm", "_CshOutPmtInstrm"]
	@property
	def CshInPmtInstrm(self):
		return self._CshInPmtInstrm

	@CshInPmtInstrm.setter
	def CshInPmtInstrm(self, value):
		self._CshInPmtInstrm = value if type(value) != base_types.auto else self.make_default("CshInPmtInstrm")

	@CshInPmtInstrm.deleter
	def CshInPmtInstrm(self):
		del self._CshInPmtInstrm
		self._CshInPmtInstrm = None

	@property
	def CshOutPmtInstrm(self):
		return self._CshOutPmtInstrm

	@CshOutPmtInstrm.setter
	def CshOutPmtInstrm(self, value):
		self._CshOutPmtInstrm = value if type(value) != base_types.auto else self.make_default("CshOutPmtInstrm")

	@CshOutPmtInstrm.deleter
	def CshOutPmtInstrm(self):
		del self._CshOutPmtInstrm
		self._CshOutPmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInPmtInstrm', type=PaymentInstrument30Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshOutPmtInstrm', type=PaymentInstrument28Choice, min=0, max=1, mutex_group=1, array=False),
	))

