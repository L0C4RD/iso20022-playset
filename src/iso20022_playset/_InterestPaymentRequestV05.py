# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Agreement4
from . import InterestAmount4
from . import InterestResult1
from . import Max35Text
from . import Obligation9
from . import SupplementaryData1

class InterestPaymentRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Agrmt", "_IntrstDueToA", "_IntrstDueToB", "_NetAmtDtls", "_Oblgtn", "_SplmtryData", "_TxId"]
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
	def IntrstDueToA(self):
		return self._IntrstDueToA

	@IntrstDueToA.setter
	def IntrstDueToA(self, value):
		self._IntrstDueToA = value if value is not None else base_types.UninitialisedField(self, 'IntrstDueToA', InterestAmount4, False)

	@IntrstDueToA.deleter
	def IntrstDueToA(self):
		del self._IntrstDueToA
		self._IntrstDueToA = base_types.UninitialisedField(self, 'IntrstDueToA', InterestAmount4, False)

	@property
	def IntrstDueToB(self):
		return self._IntrstDueToB

	@IntrstDueToB.setter
	def IntrstDueToB(self, value):
		self._IntrstDueToB = value if value is not None else base_types.UninitialisedField(self, 'IntrstDueToB', InterestAmount4, False)

	@IntrstDueToB.deleter
	def IntrstDueToB(self):
		del self._IntrstDueToB
		self._IntrstDueToB = base_types.UninitialisedField(self, 'IntrstDueToB', InterestAmount4, False)

	@property
	def NetAmtDtls(self):
		return self._NetAmtDtls

	@NetAmtDtls.setter
	def NetAmtDtls(self, value):
		self._NetAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'NetAmtDtls', InterestResult1, False)

	@NetAmtDtls.deleter
	def NetAmtDtls(self):
		del self._NetAmtDtls
		self._NetAmtDtls = base_types.UninitialisedField(self, 'NetAmtDtls', InterestResult1, False)

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
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstDueToA', type=InterestAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstDueToB', type=InterestAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmtDtls', type=InterestResult1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))