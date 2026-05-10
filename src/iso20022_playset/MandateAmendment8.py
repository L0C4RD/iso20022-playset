from . import base_types
from .OriginalMandate10Choice import OriginalMandate10Choice
from .Mandate21 import Mandate21
from .MandateAmendmentReason3 import MandateAmendmentReason3
from .OriginalMessageInformation1 import OriginalMessageInformation1
from .SupplementaryData1 import SupplementaryData1

class MandateAmendment8(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_OrgnlMsgInf", "_Mndt", "_OrgnlMndt", "_AmdmntRsn"]
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
	def OrgnlMsgInf(self):
		return self._OrgnlMsgInf

	@OrgnlMsgInf.setter
	def OrgnlMsgInf(self, value):
		self._OrgnlMsgInf = value if type(value) != base_types.auto else self.make_default("OrgnlMsgInf")

	@OrgnlMsgInf.deleter
	def OrgnlMsgInf(self):
		del self._OrgnlMsgInf
		self._OrgnlMsgInf = None

	@property
	def Mndt(self):
		return self._Mndt

	@Mndt.setter
	def Mndt(self, value):
		self._Mndt = value if type(value) != base_types.auto else self.make_default("Mndt")

	@Mndt.deleter
	def Mndt(self):
		del self._Mndt
		self._Mndt = None

	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if type(value) != base_types.auto else self.make_default("OrgnlMndt")

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = None

	@property
	def AmdmntRsn(self):
		return self._AmdmntRsn

	@AmdmntRsn.setter
	def AmdmntRsn(self, value):
		self._AmdmntRsn = value if type(value) != base_types.auto else self.make_default("AmdmntRsn")

	@AmdmntRsn.deleter
	def AmdmntRsn(self):
		del self._AmdmntRsn
		self._AmdmntRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlMsgInf', type=OriginalMessageInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mndt', type=Mandate21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMndt', type=OriginalMandate10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntRsn', type=MandateAmendmentReason3, min=1, max=1, mutex_group=None, array=False),
	))

