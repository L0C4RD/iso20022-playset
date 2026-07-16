# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitCode
from . import FormOfSecurity1Code
from . import Max35Text
from . import NationalityCode
from . import PartyIdentification2Choice
from . import SecuritiesBalanceType9FormatChoice

class SecuritiesAccount10(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnrId", "_AcctOwnrNtlty", "_BalTp", "_CdtDbtInd", "_SctyHldgForm"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@property
	def AcctOwnrNtlty(self):
		return self._AcctOwnrNtlty

	@AcctOwnrNtlty.setter
	def AcctOwnrNtlty(self, value):
		self._AcctOwnrNtlty = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrNtlty', NationalityCode, False)

	@AcctOwnrNtlty.deleter
	def AcctOwnrNtlty(self):
		del self._AcctOwnrNtlty
		self._AcctOwnrNtlty = base_types.UninitialisedField(self, 'AcctOwnrNtlty', NationalityCode, False)

	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if value is not None else base_types.UninitialisedField(self, 'BalTp', SecuritiesBalanceType9FormatChoice, False)

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = base_types.UninitialisedField(self, 'BalTp', SecuritiesBalanceType9FormatChoice, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def SctyHldgForm(self):
		return self._SctyHldgForm

	@SctyHldgForm.setter
	def SctyHldgForm(self, value):
		self._SctyHldgForm = value if value is not None else base_types.UninitialisedField(self, 'SctyHldgForm', FormOfSecurity1Code, False)

	@SctyHldgForm.deleter
	def SctyHldgForm(self):
		del self._SctyHldgForm
		self._SctyHldgForm = base_types.UninitialisedField(self, 'SctyHldgForm', FormOfSecurity1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrNtlty', type=NationalityCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTp', type=SecuritiesBalanceType9FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyHldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
	))