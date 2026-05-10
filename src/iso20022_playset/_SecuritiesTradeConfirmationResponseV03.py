from . import base_types
from ._Clearing6 import Clearing6
from ._StatusAndReason46 import StatusAndReason46
from ._ConfirmationParties8 import ConfirmationParties8
from ._SupplementaryData1 import SupplementaryData1
from ._Linkages76 import Linkages76
from ._TransactiontIdentification4 import TransactiontIdentification4

class SecuritiesTradeConfirmationResponseV03(base_types._BaseFieldType):

	__slots__ = ["_Refs", "_ConfPties", "_Id", "_Sts", "_SplmtryData", "_ClrDtls"]
	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if type(value) != base_types.auto else self.make_default("ConfPties")

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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
	def ClrDtls(self):
		return self._ClrDtls

	@ClrDtls.setter
	def ClrDtls(self, value):
		self._ClrDtls = value if type(value) != base_types.auto else self.make_default("ClrDtls")

	@ClrDtls.deleter
	def ClrDtls(self):
		del self._ClrDtls
		self._ClrDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Refs', type=Linkages76, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=TransactiontIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=StatusAndReason46, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrDtls', type=Clearing6, min=0, max=1, mutex_group=None, array=False),
	))

