# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Clearing6
from . import ConfirmationParties8
from . import Linkages76
from . import StatusAndReason46
from . import SupplementaryData1
from . import TransactiontIdentification4

class SecuritiesTradeConfirmationResponseV03(base_types._BaseFieldType):

	__slots__ = ["_ClrDtls", "_ConfPties", "_Id", "_Refs", "_SplmtryData", "_Sts"]
	@property
	def ClrDtls(self):
		return self._ClrDtls

	@ClrDtls.setter
	def ClrDtls(self, value):
		self._ClrDtls = value if value is not None else base_types.UninitialisedField(self, 'ClrDtls', Clearing6, False)

	@ClrDtls.deleter
	def ClrDtls(self):
		del self._ClrDtls
		self._ClrDtls = base_types.UninitialisedField(self, 'ClrDtls', Clearing6, False)

	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if value is not None else base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties8, True)

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties8, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', TransactiontIdentification4, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', TransactiontIdentification4, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', Linkages76, True)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', Linkages76, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', StatusAndReason46, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', StatusAndReason46, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrDtls', type=Clearing6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=TransactiontIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Linkages76, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=StatusAndReason46, min=1, max=1, mutex_group=None, array=False),
	))