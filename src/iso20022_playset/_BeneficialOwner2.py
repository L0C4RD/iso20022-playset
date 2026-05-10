from . import base_types
from ._AlternateIdentification4 import AlternateIdentification4
from ._BeneficiaryCertificationType9Choice import BeneficiaryCertificationType9Choice
from ._CountryCode import CountryCode
from ._Max350Text import Max350Text
from ._PartyIdentification100 import PartyIdentification100
from ._YesNoIndicator import YesNoIndicator

class BeneficialOwner2(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_BnfclOwnrId", "_CertfctnInd", "_CertfctnTp", "_DclrtnDtls", "_DmclCtry", "_NonDmclCtry", "_Ntlty"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != base_types.auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	@property
	def BnfclOwnrId(self):
		return self._BnfclOwnrId

	@BnfclOwnrId.setter
	def BnfclOwnrId(self, value):
		self._BnfclOwnrId = value if type(value) != base_types.auto else self.make_default("BnfclOwnrId")

	@BnfclOwnrId.deleter
	def BnfclOwnrId(self):
		del self._BnfclOwnrId
		self._BnfclOwnrId = None

	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if type(value) != base_types.auto else self.make_default("CertfctnInd")

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = None

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
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if type(value) != base_types.auto else self.make_default("DclrtnDtls")

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = None

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
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if type(value) != base_types.auto else self.make_default("Ntlty")

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=AlternateIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrId', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmclCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDmclCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

