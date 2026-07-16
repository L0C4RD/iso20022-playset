# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BeneficialOwner1
from . import BeneficiaryCertificationType1FormatChoice
from . import Max350Text
from . import PartyIdentification2Choice
from . import ProceedsDelivery1
from . import YesNoIndicator

class CorporateActionAdditionalInformation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInstr", "_BnfclOwnrDtls", "_CertfctnInd", "_CertfctnTp", "_DlvryDtls", "_RcvrId", "_RegnDtls"]
	@property
	def AddtlInstr(self):
		return self._AddtlInstr

	@AddtlInstr.setter
	def AddtlInstr(self, value):
		self._AddtlInstr = value if value is not None else base_types.UninitialisedField(self, 'AddtlInstr', Max350Text, False)

	@AddtlInstr.deleter
	def AddtlInstr(self):
		del self._AddtlInstr
		self._AddtlInstr = base_types.UninitialisedField(self, 'AddtlInstr', Max350Text, False)

	@property
	def BnfclOwnrDtls(self):
		return self._BnfclOwnrDtls

	@BnfclOwnrDtls.setter
	def BnfclOwnrDtls(self, value):
		self._BnfclOwnrDtls = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrDtls', BeneficialOwner1, True)

	@BnfclOwnrDtls.deleter
	def BnfclOwnrDtls(self):
		del self._BnfclOwnrDtls
		self._BnfclOwnrDtls = base_types.UninitialisedField(self, 'BnfclOwnrDtls', BeneficialOwner1, True)

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
	def DlvryDtls(self):
		return self._DlvryDtls

	@DlvryDtls.setter
	def DlvryDtls(self, value):
		self._DlvryDtls = value if value is not None else base_types.UninitialisedField(self, 'DlvryDtls', ProceedsDelivery1, True)

	@DlvryDtls.deleter
	def DlvryDtls(self):
		del self._DlvryDtls
		self._DlvryDtls = base_types.UninitialisedField(self, 'DlvryDtls', ProceedsDelivery1, True)

	@property
	def RcvrId(self):
		return self._RcvrId

	@RcvrId.setter
	def RcvrId(self, value):
		self._RcvrId = value if value is not None else base_types.UninitialisedField(self, 'RcvrId', PartyIdentification2Choice, False)

	@RcvrId.deleter
	def RcvrId(self):
		del self._RcvrId
		self._RcvrId = base_types.UninitialisedField(self, 'RcvrId', PartyIdentification2Choice, False)

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if value is not None else base_types.UninitialisedField(self, 'RegnDtls', Max350Text, False)

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = base_types.UninitialisedField(self, 'RegnDtls', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInstr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrDtls', type=BeneficialOwner1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDtls', type=ProceedsDelivery1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))