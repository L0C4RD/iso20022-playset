# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralProposalResponse4Choice
from . import Max35Text
from . import Obligation9
from . import SupplementaryData1

class CollateralProposalResponseV06(base_types._BaseFieldType):

	__slots__ = ["_Oblgtn", "_PrpslRspn", "_SplmtryData", "_TxId"]
	@property
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if value is not None else base_types.UninitialisedField(self, 'Oblgtn', Obligation9, False)

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = base_types.UninitialisedField(self, 'Oblgtn', Obligation9, False)

	@property
	def PrpslRspn(self):
		return self._PrpslRspn

	@PrpslRspn.setter
	def PrpslRspn(self, value):
		self._PrpslRspn = value if value is not None else base_types.UninitialisedField(self, 'PrpslRspn', CollateralProposalResponse4Choice, False)

	@PrpslRspn.deleter
	def PrpslRspn(self):
		del self._PrpslRspn
		self._PrpslRspn = base_types.UninitialisedField(self, 'PrpslRspn', CollateralProposalResponse4Choice, False)

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
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrpslRspn', type=CollateralProposalResponse4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))