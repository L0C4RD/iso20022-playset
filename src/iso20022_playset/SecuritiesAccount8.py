from . import base_types
import CorporateActionOption1FormatChoice
import PartyIdentification2Choice
import Exact3NumericText
import Max35Text
import SecuritiesBalanceType10FormatChoice
import CreditDebitCode
import StampDutyType1FormatChoice
import FormOfSecurity1Code

class SecuritiesAccount8(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrId", "_CdtDbtInd", "_BalTp", "_AcctId", "_OptnNb", "_OptnTp", "_SctyHldgForm", "_StmpDty"]
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
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if type(value) != auto else self.make_default("StmpDty")

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTp', type=SecuritiesBalanceType10FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyHldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=StampDutyType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
	))

