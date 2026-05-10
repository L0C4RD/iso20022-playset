import base_types
import CreditDebitCode
import PartyIdentification2Choice
import SecuritiesBalanceType9FormatChoice
import FormOfSecurity1Code
import Max35Text
import NationalityCode

class SecuritiesAccount10(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrId", "_BalTp", "_AcctOwnrNtlty", "_CdtDbtInd", "_SctyHldgForm", "_AcctId"]
	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def AcctOwnrNtlty(self):
		return self._AcctOwnrNtlty

	@AcctOwnrNtlty.setter
	def AcctOwnrNtlty(self, value):
		self._AcctOwnrNtlty = value if type(value) != auto else self.make_default("AcctOwnrNtlty")

	@AcctOwnrNtlty.deleter
	def AcctOwnrNtlty(self):
		del self._AcctOwnrNtlty
		self._AcctOwnrNtlty = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def SctyHldgForm(self):
		return self._SctyHldgForm

	@SctyHldgForm.setter
	def SctyHldgForm(self, value):
		self._SctyHldgForm = value if type(value) != auto else self.make_default("SctyHldgForm")

	@SctyHldgForm.deleter
	def SctyHldgForm(self):
		del self._SctyHldgForm
		self._SctyHldgForm = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTp', type=SecuritiesBalanceType9FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrNtlty', type=NationalityCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyHldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

