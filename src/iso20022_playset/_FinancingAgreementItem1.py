# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgreementItemAction1Code
from . import FinancialItemParameters1
from . import GuaranteeDetails1
from . import Max2000Text
from . import PaymentInstrumentCode
from . import ValidationStatusInformation1
from . import YesNoIndicator
from . import xs:IDREF

class FinancingAgreementItem1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AssoctdDoc", "_Grnt", "_GrntSts", "_ItmActn", "_ItmCntxt", "_PmtInstrm", "_Ratg", "_ReopIndctn", "_RltdGrntLttr", "_VldtnStsInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@property
	def Grnt(self):
		return self._Grnt

	@Grnt.setter
	def Grnt(self, value):
		self._Grnt = value if value is not None else base_types.UninitialisedField(self, 'Grnt', GuaranteeDetails1, True)

	@Grnt.deleter
	def Grnt(self):
		del self._Grnt
		self._Grnt = base_types.UninitialisedField(self, 'Grnt', GuaranteeDetails1, True)

	@property
	def GrntSts(self):
		return self._GrntSts

	@GrntSts.setter
	def GrntSts(self, value):
		self._GrntSts = value if value is not None else base_types.UninitialisedField(self, 'GrntSts', ValidationStatusInformation1, False)

	@GrntSts.deleter
	def GrntSts(self):
		del self._GrntSts
		self._GrntSts = base_types.UninitialisedField(self, 'GrntSts', ValidationStatusInformation1, False)

	@property
	def ItmActn(self):
		return self._ItmActn

	@ItmActn.setter
	def ItmActn(self, value):
		self._ItmActn = value if value is not None else base_types.UninitialisedField(self, 'ItmActn', AgreementItemAction1Code, False)

	@ItmActn.deleter
	def ItmActn(self):
		del self._ItmActn
		self._ItmActn = base_types.UninitialisedField(self, 'ItmActn', AgreementItemAction1Code, False)

	@property
	def ItmCntxt(self):
		return self._ItmCntxt

	@ItmCntxt.setter
	def ItmCntxt(self, value):
		self._ItmCntxt = value if value is not None else base_types.UninitialisedField(self, 'ItmCntxt', FinancialItemParameters1, False)

	@ItmCntxt.deleter
	def ItmCntxt(self):
		del self._ItmCntxt
		self._ItmCntxt = base_types.UninitialisedField(self, 'ItmCntxt', FinancialItemParameters1, False)

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentCode, False)

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentCode, False)

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if value is not None else base_types.UninitialisedField(self, 'Ratg', YesNoIndicator, False)

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = base_types.UninitialisedField(self, 'Ratg', YesNoIndicator, False)

	@property
	def ReopIndctn(self):
		return self._ReopIndctn

	@ReopIndctn.setter
	def ReopIndctn(self, value):
		self._ReopIndctn = value if value is not None else base_types.UninitialisedField(self, 'ReopIndctn', YesNoIndicator, False)

	@ReopIndctn.deleter
	def ReopIndctn(self):
		del self._ReopIndctn
		self._ReopIndctn = base_types.UninitialisedField(self, 'ReopIndctn', YesNoIndicator, False)

	@property
	def RltdGrntLttr(self):
		return self._RltdGrntLttr

	@RltdGrntLttr.setter
	def RltdGrntLttr(self, value):
		self._RltdGrntLttr = value if value is not None else base_types.UninitialisedField(self, 'RltdGrntLttr', xs:IDREF, False)

	@RltdGrntLttr.deleter
	def RltdGrntLttr(self):
		del self._RltdGrntLttr
		self._RltdGrntLttr = base_types.UninitialisedField(self, 'RltdGrntLttr', xs:IDREF, False)

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if value is not None else base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grnt', type=GuaranteeDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrntSts', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmActn', type=AgreementItemAction1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCntxt', type=FinancialItemParameters1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ratg', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReopIndctn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdGrntLttr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
	))