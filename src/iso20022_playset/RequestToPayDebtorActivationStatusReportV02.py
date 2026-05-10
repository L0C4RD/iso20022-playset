from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .ActivationStatus3 import ActivationStatus3
from .ActivationHeader3 import ActivationHeader3

class RequestToPayDebtorActivationStatusReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_OrgnlActvtnAndSts", "_Hdr"]
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
	def OrgnlActvtnAndSts(self):
		return self._OrgnlActvtnAndSts

	@OrgnlActvtnAndSts.setter
	def OrgnlActvtnAndSts(self, value):
		self._OrgnlActvtnAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlActvtnAndSts")

	@OrgnlActvtnAndSts.deleter
	def OrgnlActvtnAndSts(self):
		del self._OrgnlActvtnAndSts
		self._OrgnlActvtnAndSts = None

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
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlActvtnAndSts', type=ActivationStatus3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
	))

