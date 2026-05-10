from . import base_types
from ._AccountNotification24 import AccountNotification24
from ._GroupHeader116 import GroupHeader116
from ._SupplementaryData1 import SupplementaryData1

class BankToCustomerDebitCreditNotificationV13(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_Ntfctn", "_SplmtryData"]
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
	def Ntfctn(self):
		return self._Ntfctn

	@Ntfctn.setter
	def Ntfctn(self, value):
		self._Ntfctn = value if type(value) != base_types.auto else self.make_default("Ntfctn")

	@Ntfctn.deleter
	def Ntfctn(self):
		del self._Ntfctn
		self._Ntfctn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader116, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntfctn', type=AccountNotification24, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

