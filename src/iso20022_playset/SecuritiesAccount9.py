import base_types
import Max35Text
import PartyIdentification2Choice
import FormOfSecurity1Code
import SecuritiesBalanceType10FormatChoice
import Exact3NumericText
import CorporateActionOption1FormatChoice
import CreditDebitCode

class SecuritiesAccount9(base_types._BaseFieldType):

	__slots__ = ["_SctyHldgForm", "_OptnTp", "_CdtDbtInd", "_AcctOwnrId", "_OptnNb", "_AcctId", "_BalTp"]
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
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

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
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyHldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTp', type=SecuritiesBalanceType10FormatChoice, min=0, max=1, mutex_group=None, array=False),
	))

