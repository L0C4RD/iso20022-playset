from . import base_types
import YesNoIndicator
import PaymentInstrumentCode
import AgreementItemAction1Code
import GuaranteeDetails1
import ValidationStatusInformation1
import xs:IDREF
import Max2000Text
import FinancialItemParameters1

class FinancingAgreementItem1(base_types._BaseFieldType):

	__slots__ = ["_GrntSts", "_ItmCntxt", "_ReopIndctn", "_Ratg", "_ItmActn", "_AssoctdDoc", "_AddtlInf", "_Grnt", "_VldtnStsInf", "_RltdGrntLttr", "_PmtInstrm"]
	@property
	def GrntSts(self):
		return self._GrntSts

	@GrntSts.setter
	def GrntSts(self, value):
		self._GrntSts = value if type(value) != auto else self.make_default("GrntSts")

	@GrntSts.deleter
	def GrntSts(self):
		del self._GrntSts
		self._GrntSts = None

	@property
	def ItmCntxt(self):
		return self._ItmCntxt

	@ItmCntxt.setter
	def ItmCntxt(self, value):
		self._ItmCntxt = value if type(value) != auto else self.make_default("ItmCntxt")

	@ItmCntxt.deleter
	def ItmCntxt(self):
		del self._ItmCntxt
		self._ItmCntxt = None

	@property
	def ReopIndctn(self):
		return self._ReopIndctn

	@ReopIndctn.setter
	def ReopIndctn(self, value):
		self._ReopIndctn = value if type(value) != auto else self.make_default("ReopIndctn")

	@ReopIndctn.deleter
	def ReopIndctn(self):
		del self._ReopIndctn
		self._ReopIndctn = None

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if type(value) != auto else self.make_default("Ratg")

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = None

	@property
	def ItmActn(self):
		return self._ItmActn

	@ItmActn.setter
	def ItmActn(self, value):
		self._ItmActn = value if type(value) != auto else self.make_default("ItmActn")

	@ItmActn.deleter
	def ItmActn(self):
		del self._ItmActn
		self._ItmActn = None

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if type(value) != auto else self.make_default("AssoctdDoc")

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Grnt(self):
		return self._Grnt

	@Grnt.setter
	def Grnt(self, value):
		self._Grnt = value if type(value) != auto else self.make_default("Grnt")

	@Grnt.deleter
	def Grnt(self):
		del self._Grnt
		self._Grnt = None

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if type(value) != auto else self.make_default("VldtnStsInf")

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = None

	@property
	def RltdGrntLttr(self):
		return self._RltdGrntLttr

	@RltdGrntLttr.setter
	def RltdGrntLttr(self, value):
		self._RltdGrntLttr = value if type(value) != auto else self.make_default("RltdGrntLttr")

	@RltdGrntLttr.deleter
	def RltdGrntLttr(self):
		del self._RltdGrntLttr
		self._RltdGrntLttr = None

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrntSts', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCntxt', type=FinancialItemParameters1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReopIndctn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ratg', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmActn', type=AgreementItemAction1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grnt', type=GuaranteeDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdGrntLttr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentCode, min=0, max=1, mutex_group=None, array=False),
	))

