from . import base_types
import Max350Text
import BeneficiaryCertificationType1FormatChoice
import YesNoIndicator
import PartyIdentification2Choice
import ProceedsDelivery1
import BeneficialOwner1

class CorporateActionAdditionalInformation1(base_types._BaseFieldType):

	__slots__ = ["_DlvryDtls", "_AddtlInstr", "_CertfctnTp", "_RegnDtls", "_RcvrId", "_BnfclOwnrDtls", "_CertfctnInd"]
	@property
	def DlvryDtls(self):
		return self._DlvryDtls

	@DlvryDtls.setter
	def DlvryDtls(self, value):
		self._DlvryDtls = value if type(value) != auto else self.make_default("DlvryDtls")

	@DlvryDtls.deleter
	def DlvryDtls(self):
		del self._DlvryDtls
		self._DlvryDtls = None

	@property
	def AddtlInstr(self):
		return self._AddtlInstr

	@AddtlInstr.setter
	def AddtlInstr(self, value):
		self._AddtlInstr = value if type(value) != auto else self.make_default("AddtlInstr")

	@AddtlInstr.deleter
	def AddtlInstr(self):
		del self._AddtlInstr
		self._AddtlInstr = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if type(value) != auto else self.make_default("RegnDtls")

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = None

	@property
	def RcvrId(self):
		return self._RcvrId

	@RcvrId.setter
	def RcvrId(self, value):
		self._RcvrId = value if type(value) != auto else self.make_default("RcvrId")

	@RcvrId.deleter
	def RcvrId(self):
		del self._RcvrId
		self._RcvrId = None

	@property
	def BnfclOwnrDtls(self):
		return self._BnfclOwnrDtls

	@BnfclOwnrDtls.setter
	def BnfclOwnrDtls(self, value):
		self._BnfclOwnrDtls = value if type(value) != auto else self.make_default("BnfclOwnrDtls")

	@BnfclOwnrDtls.deleter
	def BnfclOwnrDtls(self):
		del self._BnfclOwnrDtls
		self._BnfclOwnrDtls = None

	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if type(value) != auto else self.make_default("CertfctnInd")

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryDtls', type=ProceedsDelivery1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInstr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrDtls', type=BeneficialOwner1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

