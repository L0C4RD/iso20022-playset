from . import base_types
from .CreditDebitCode import CreditDebitCode
from .FormOfSecurity1Code import FormOfSecurity1Code
from .Max35Text import Max35Text
from .PartyIdentification2Choice import PartyIdentification2Choice
from .SecuritiesBalanceType6FormatChoice import SecuritiesBalanceType6FormatChoice

class SecuritiesAccount12(base_types._BaseFieldType):

	__slots__ = ["_BalTp", "_SctyHldgForm", "_AcctId", "_AcctOwnrId", "_CdtDbtInd"]
	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != base_types.auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def SctyHldgForm(self):
		return self._SctyHldgForm

	@SctyHldgForm.setter
	def SctyHldgForm(self, value):
		self._SctyHldgForm = value if type(value) != base_types.auto else self.make_default("SctyHldgForm")

	@SctyHldgForm.deleter
	def SctyHldgForm(self):
		del self._SctyHldgForm
		self._SctyHldgForm = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != base_types.auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTp', type=SecuritiesBalanceType6FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyHldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
	))

