import base_types
import RemittanceAmount2
import ReferredDocumentInformation7
import Garnishment3
import PartyIdentification135
import CreditorReferenceInformation2
import TaxInformation7
import Max140Text

class StructuredRemittanceInformation16(base_types._BaseFieldType):

	__slots__ = ["_TaxRmt", "_RfrdDocInf", "_AddtlRmtInf", "_RfrdDocAmt", "_CdtrRefInf", "_Invcee", "_Invcr", "_GrnshmtRmt"]
	@property
	def TaxRmt(self):
		return self._TaxRmt

	@TaxRmt.setter
	def TaxRmt(self, value):
		self._TaxRmt = value if type(value) != auto else self.make_default("TaxRmt")

	@TaxRmt.deleter
	def TaxRmt(self):
		del self._TaxRmt
		self._TaxRmt = None

	@property
	def RfrdDocInf(self):
		return self._RfrdDocInf

	@RfrdDocInf.setter
	def RfrdDocInf(self, value):
		self._RfrdDocInf = value if type(value) != auto else self.make_default("RfrdDocInf")

	@RfrdDocInf.deleter
	def RfrdDocInf(self):
		del self._RfrdDocInf
		self._RfrdDocInf = None

	@property
	def AddtlRmtInf(self):
		return self._AddtlRmtInf

	@AddtlRmtInf.setter
	def AddtlRmtInf(self, value):
		self._AddtlRmtInf = value if type(value) != auto else self.make_default("AddtlRmtInf")

	@AddtlRmtInf.deleter
	def AddtlRmtInf(self):
		del self._AddtlRmtInf
		self._AddtlRmtInf = None

	@property
	def RfrdDocAmt(self):
		return self._RfrdDocAmt

	@RfrdDocAmt.setter
	def RfrdDocAmt(self, value):
		self._RfrdDocAmt = value if type(value) != auto else self.make_default("RfrdDocAmt")

	@RfrdDocAmt.deleter
	def RfrdDocAmt(self):
		del self._RfrdDocAmt
		self._RfrdDocAmt = None

	@property
	def CdtrRefInf(self):
		return self._CdtrRefInf

	@CdtrRefInf.setter
	def CdtrRefInf(self, value):
		self._CdtrRefInf = value if type(value) != auto else self.make_default("CdtrRefInf")

	@CdtrRefInf.deleter
	def CdtrRefInf(self):
		del self._CdtrRefInf
		self._CdtrRefInf = None

	@property
	def Invcee(self):
		return self._Invcee

	@Invcee.setter
	def Invcee(self, value):
		self._Invcee = value if type(value) != auto else self.make_default("Invcee")

	@Invcee.deleter
	def Invcee(self):
		del self._Invcee
		self._Invcee = None

	@property
	def Invcr(self):
		return self._Invcr

	@Invcr.setter
	def Invcr(self, value):
		self._Invcr = value if type(value) != auto else self.make_default("Invcr")

	@Invcr.deleter
	def Invcr(self):
		del self._Invcr
		self._Invcr = None

	@property
	def GrnshmtRmt(self):
		return self._GrnshmtRmt

	@GrnshmtRmt.setter
	def GrnshmtRmt(self, value):
		self._GrnshmtRmt = value if type(value) != auto else self.make_default("GrnshmtRmt")

	@GrnshmtRmt.deleter
	def GrnshmtRmt(self):
		del self._GrnshmtRmt
		self._GrnshmtRmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxRmt', type=TaxInformation7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDocInf', type=ReferredDocumentInformation7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlRmtInf', type=Max140Text, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='RfrdDocAmt', type=RemittanceAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrRefInf', type=CreditorReferenceInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcee', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcr', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrnshmtRmt', type=Garnishment3, min=0, max=1, mutex_group=None, array=False),
	))

