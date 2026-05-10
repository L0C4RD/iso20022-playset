import base_types
import BranchAndFinancialInstitutionIdentification8
import BalanceCounterparty1Code
import DateAndDateTimeSearch4Choice
import BalanceType11Choice

class CashBalance14(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_PrcgDt", "_CtrPtyTp", "_ValDt", "_CtrPtyId"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if type(value) != auto else self.make_default("PrcgDt")

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = None

	@property
	def CtrPtyTp(self):
		return self._CtrPtyTp

	@CtrPtyTp.setter
	def CtrPtyTp(self, value):
		self._CtrPtyTp = value if type(value) != auto else self.make_default("CtrPtyTp")

	@CtrPtyTp.deleter
	def CtrPtyTp(self):
		del self._CtrPtyTp
		self._CtrPtyTp = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=BalanceType11Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgDt', type=DateAndDateTimeSearch4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyTp', type=BalanceCounterparty1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTimeSearch4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=None, mutex_group=None, array=True),
	))

