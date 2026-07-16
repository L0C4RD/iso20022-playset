# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternatePartyIdentification9
from . import BeneficiaryCertificationType11Choice
from . import CountryCode
from . import FinancialInstrumentQuantity36Choice
from . import LEIIdentifier
from . import PartyIdentification259Choice
from . import RateAndAmountFormat63Choice
from . import RestrictedFINXMax350Text

class PartyIdentification317(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_CertfctnBrkdwn", "_CertfctnTp", "_DmclCtry", "_LEIId", "_NonDmclCtry", "_OwndSctiesQty", "_OwnrId", "_WhldgTaxRate"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification9, True)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification9, True)

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwn', RestrictedFINXMax350Text, True)

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = base_types.UninitialisedField(self, 'CertfctnBrkdwn', RestrictedFINXMax350Text, True)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType11Choice, True)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType11Choice, True)

	@property
	def DmclCtry(self):
		return self._DmclCtry

	@DmclCtry.setter
	def DmclCtry(self, value):
		self._DmclCtry = value if value is not None else base_types.UninitialisedField(self, 'DmclCtry', CountryCode, False)

	@DmclCtry.deleter
	def DmclCtry(self):
		del self._DmclCtry
		self._DmclCtry = base_types.UninitialisedField(self, 'DmclCtry', CountryCode, False)

	@property
	def LEIId(self):
		return self._LEIId

	@LEIId.setter
	def LEIId(self, value):
		self._LEIId = value if value is not None else base_types.UninitialisedField(self, 'LEIId', LEIIdentifier, False)

	@LEIId.deleter
	def LEIId(self):
		del self._LEIId
		self._LEIId = base_types.UninitialisedField(self, 'LEIId', LEIIdentifier, False)

	@property
	def NonDmclCtry(self):
		return self._NonDmclCtry

	@NonDmclCtry.setter
	def NonDmclCtry(self, value):
		self._NonDmclCtry = value if value is not None else base_types.UninitialisedField(self, 'NonDmclCtry', CountryCode, True)

	@NonDmclCtry.deleter
	def NonDmclCtry(self):
		del self._NonDmclCtry
		self._NonDmclCtry = base_types.UninitialisedField(self, 'NonDmclCtry', CountryCode, True)

	@property
	def OwndSctiesQty(self):
		return self._OwndSctiesQty

	@OwndSctiesQty.setter
	def OwndSctiesQty(self, value):
		self._OwndSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'OwndSctiesQty', FinancialInstrumentQuantity36Choice, False)

	@OwndSctiesQty.deleter
	def OwndSctiesQty(self):
		del self._OwndSctiesQty
		self._OwndSctiesQty = base_types.UninitialisedField(self, 'OwndSctiesQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if value is not None else base_types.UninitialisedField(self, 'OwnrId', PartyIdentification259Choice, False)

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = base_types.UninitialisedField(self, 'OwnrId', PartyIdentification259Choice, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat63Choice, False)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat63Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnBrkdwn', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType11Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DmclCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEIId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDmclCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OwndSctiesQty', type=FinancialInstrumentQuantity36Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrId', type=PartyIdentification259Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat63Choice, min=0, max=1, mutex_group=None, array=False),
	))