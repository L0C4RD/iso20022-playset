from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .ActivationHeader3 import ActivationHeader3
from .DebtorActivationCancellation3 import DebtorActivationCancellation3

class RequestToPayDebtorActivationCancellationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_CxlData", "_SplmtryData", "_Hdr"]
	@property
	def CxlData(self):
		return self._CxlData

	@CxlData.setter
	def CxlData(self, value):
		self._CxlData = value if type(value) != base_types.auto else self.make_default("CxlData")

	@CxlData.deleter
	def CxlData(self):
		del self._CxlData
		self._CxlData = None

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
		base_types.FieldEntry(name='CxlData', type=DebtorActivationCancellation3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
	))

