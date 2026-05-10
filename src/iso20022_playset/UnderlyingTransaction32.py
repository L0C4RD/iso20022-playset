from . import base_types
from .PaymentTransaction152 import PaymentTransaction152
from .OriginalPaymentInstruction48 import OriginalPaymentInstruction48
from .OriginalGroupHeader23 import OriginalGroupHeader23

class UnderlyingTransaction32(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPmtInfAndSts", "_OrgnlGrpInfAndSts", "_TxInfAndSts"]
	@property
	def OrgnlPmtInfAndSts(self):
		return self._OrgnlPmtInfAndSts

	@OrgnlPmtInfAndSts.setter
	def OrgnlPmtInfAndSts(self, value):
		self._OrgnlPmtInfAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfAndSts")

	@OrgnlPmtInfAndSts.deleter
	def OrgnlPmtInfAndSts(self):
		del self._OrgnlPmtInfAndSts
		self._OrgnlPmtInfAndSts = None

	@property
	def OrgnlGrpInfAndSts(self):
		return self._OrgnlGrpInfAndSts

	@OrgnlGrpInfAndSts.setter
	def OrgnlGrpInfAndSts(self, value):
		self._OrgnlGrpInfAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInfAndSts")

	@OrgnlGrpInfAndSts.deleter
	def OrgnlGrpInfAndSts(self):
		del self._OrgnlGrpInfAndSts
		self._OrgnlGrpInfAndSts = None

	@property
	def TxInfAndSts(self):
		return self._TxInfAndSts

	@TxInfAndSts.setter
	def TxInfAndSts(self, value):
		self._TxInfAndSts = value if type(value) != base_types.auto else self.make_default("TxInfAndSts")

	@TxInfAndSts.deleter
	def TxInfAndSts(self):
		del self._TxInfAndSts
		self._TxInfAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPmtInfAndSts', type=OriginalPaymentInstruction48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlGrpInfAndSts', type=OriginalGroupHeader23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction152, min=0, max=None, mutex_group=None, array=True),
	))

