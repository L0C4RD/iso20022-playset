from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .OriginalGroupHeader19 import OriginalGroupHeader19
from .PaymentTransaction163 import PaymentTransaction163
from .GroupHeader123 import GroupHeader123

class PaymentReturnV14(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_GrpHdr", "_OrgnlGrpInf", "_TxInf"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if type(value) != base_types.auto else self.make_default("TxInf")

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader123, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupHeader19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInf', type=PaymentTransaction163, min=0, max=None, mutex_group=None, array=True),
	))

