# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceCounterparty1Code
from . import BalanceType11Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import DateAndDateTimeSearch4Choice

class CashBalance14(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_CtrPtyTp", "_PrcgDt", "_Tp", "_ValDt"]
	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', BranchAndFinancialInstitutionIdentification8, True)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', BranchAndFinancialInstitutionIdentification8, True)

	@property
	def CtrPtyTp(self):
		return self._CtrPtyTp

	@CtrPtyTp.setter
	def CtrPtyTp(self, value):
		self._CtrPtyTp = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyTp', BalanceCounterparty1Code, False)

	@CtrPtyTp.deleter
	def CtrPtyTp(self):
		del self._CtrPtyTp
		self._CtrPtyTp = base_types.UninitialisedField(self, 'CtrPtyTp', BalanceCounterparty1Code, False)

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if value is not None else base_types.UninitialisedField(self, 'PrcgDt', DateAndDateTimeSearch4Choice, False)

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = base_types.UninitialisedField(self, 'PrcgDt', DateAndDateTimeSearch4Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BalanceType11Choice, True)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BalanceType11Choice, True)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateAndDateTimeSearch4Choice, True)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateAndDateTimeSearch4Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyTp', type=BalanceCounterparty1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDt', type=DateAndDateTimeSearch4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType11Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTimeSearch4Choice, min=0, max=None, mutex_group=None, array=True),
	))