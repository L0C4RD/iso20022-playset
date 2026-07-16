# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Agreement4
from . import CollateralSubstitution7
from . import CollateralSubstitution8
from . import Max35Text
from . import Obligation9
from . import SupplementaryData1

class CollateralSubstitutionRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Agrmt", "_CollSbstitnDlvr", "_CollSbstitnRtr", "_Oblgtn", "_SplmtryData", "_TxId"]
	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if value is not None else base_types.UninitialisedField(self, 'Agrmt', Agreement4, False)

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = base_types.UninitialisedField(self, 'Agrmt', Agreement4, False)

	@property
	def CollSbstitnDlvr(self):
		return self._CollSbstitnDlvr

	@CollSbstitnDlvr.setter
	def CollSbstitnDlvr(self, value):
		self._CollSbstitnDlvr = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnDlvr', CollateralSubstitution8, False)

	@CollSbstitnDlvr.deleter
	def CollSbstitnDlvr(self):
		del self._CollSbstitnDlvr
		self._CollSbstitnDlvr = base_types.UninitialisedField(self, 'CollSbstitnDlvr', CollateralSubstitution8, False)

	@property
	def CollSbstitnRtr(self):
		return self._CollSbstitnRtr

	@CollSbstitnRtr.setter
	def CollSbstitnRtr(self, value):
		self._CollSbstitnRtr = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnRtr', CollateralSubstitution7, False)

	@CollSbstitnRtr.deleter
	def CollSbstitnRtr(self):
		del self._CollSbstitnRtr
		self._CollSbstitnRtr = base_types.UninitialisedField(self, 'CollSbstitnRtr', CollateralSubstitution7, False)

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
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnDlvr', type=CollateralSubstitution8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnRtr', type=CollateralSubstitution7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))