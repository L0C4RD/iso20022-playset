from . import base_types
from ._AlternatePartyIdentification9 import AlternatePartyIdentification9
from ._BeneficiaryCertificationType11Choice import BeneficiaryCertificationType11Choice
from ._CountryCode import CountryCode
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._LEIIdentifier import LEIIdentifier
from ._PartyIdentification259Choice import PartyIdentification259Choice
from ._RateAndAmountFormat63Choice import RateAndAmountFormat63Choice
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text

class PartyIdentification317(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_CertfctnBrkdwn", "_CertfctnTp", "_DmclCtry", "_LEIId", "_NonDmclCtry", "_OwndSctiesQty", "_OwnrId", "_WhldgTaxRate"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != base_types.auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if type(value) != base_types.auto else self.make_default("CertfctnBrkdwn")

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != base_types.auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def DmclCtry(self):
		return self._DmclCtry

	@DmclCtry.setter
	def DmclCtry(self, value):
		self._DmclCtry = value if type(value) != base_types.auto else self.make_default("DmclCtry")

	@DmclCtry.deleter
	def DmclCtry(self):
		del self._DmclCtry
		self._DmclCtry = None

	@property
	def LEIId(self):
		return self._LEIId

	@LEIId.setter
	def LEIId(self, value):
		self._LEIId = value if type(value) != base_types.auto else self.make_default("LEIId")

	@LEIId.deleter
	def LEIId(self):
		del self._LEIId
		self._LEIId = None

	@property
	def NonDmclCtry(self):
		return self._NonDmclCtry

	@NonDmclCtry.setter
	def NonDmclCtry(self, value):
		self._NonDmclCtry = value if type(value) != base_types.auto else self.make_default("NonDmclCtry")

	@NonDmclCtry.deleter
	def NonDmclCtry(self):
		del self._NonDmclCtry
		self._NonDmclCtry = None

	@property
	def OwndSctiesQty(self):
		return self._OwndSctiesQty

	@OwndSctiesQty.setter
	def OwndSctiesQty(self, value):
		self._OwndSctiesQty = value if type(value) != base_types.auto else self.make_default("OwndSctiesQty")

	@OwndSctiesQty.deleter
	def OwndSctiesQty(self):
		del self._OwndSctiesQty
		self._OwndSctiesQty = None

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if type(value) != base_types.auto else self.make_default("OwnrId")

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = None

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if type(value) != base_types.auto else self.make_default("WhldgTaxRate")

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = None

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

