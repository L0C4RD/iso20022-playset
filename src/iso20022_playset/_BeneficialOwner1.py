# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BeneficiaryCertificationType1FormatChoice
from . import CountryCode
from . import GenericIdentification16
from . import Max350Text
from . import PartyIdentification2Choice
from . import SecurityIdentification7
from . import UnitOrFaceAmount1Choice
from . import YesNoIndicator

class BeneficialOwner1(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_BnfclOwnrId", "_CertfctnInd", "_CertfctnTp", "_DclrtnDtls", "_DmclCtry", "_ElctdSctiesQty", "_NonDmclCtry", "_Ntlty", "_SctyId"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', GenericIdentification16, False)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', GenericIdentification16, False)

	@property
	def BnfclOwnrId(self):
		return self._BnfclOwnrId

	@BnfclOwnrId.setter
	def BnfclOwnrId(self, value):
		self._BnfclOwnrId = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrId', PartyIdentification2Choice, False)

	@BnfclOwnrId.deleter
	def BnfclOwnrId(self):
		del self._BnfclOwnrId
		self._BnfclOwnrId = base_types.UninitialisedField(self, 'BnfclOwnrId', PartyIdentification2Choice, False)

	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if value is not None else base_types.UninitialisedField(self, 'CertfctnInd', YesNoIndicator, False)

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = base_types.UninitialisedField(self, 'CertfctnInd', YesNoIndicator, False)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType1FormatChoice, False)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType1FormatChoice, False)

	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if value is not None else base_types.UninitialisedField(self, 'DclrtnDtls', Max350Text, False)

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = base_types.UninitialisedField(self, 'DclrtnDtls', Max350Text, False)

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
	def ElctdSctiesQty(self):
		return self._ElctdSctiesQty

	@ElctdSctiesQty.setter
	def ElctdSctiesQty(self, value):
		self._ElctdSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'ElctdSctiesQty', UnitOrFaceAmount1Choice, False)

	@ElctdSctiesQty.deleter
	def ElctdSctiesQty(self):
		del self._ElctdSctiesQty
		self._ElctdSctiesQty = base_types.UninitialisedField(self, 'ElctdSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def NonDmclCtry(self):
		return self._NonDmclCtry

	@NonDmclCtry.setter
	def NonDmclCtry(self, value):
		self._NonDmclCtry = value if value is not None else base_types.UninitialisedField(self, 'NonDmclCtry', CountryCode, False)

	@NonDmclCtry.deleter
	def NonDmclCtry(self):
		del self._NonDmclCtry
		self._NonDmclCtry = base_types.UninitialisedField(self, 'NonDmclCtry', CountryCode, False)

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if value is not None else base_types.UninitialisedField(self, 'Ntlty', CountryCode, False)

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = base_types.UninitialisedField(self, 'Ntlty', CountryCode, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=GenericIdentification16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmclCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctdSctiesQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDmclCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=0, max=1, mutex_group=None, array=False),
	))