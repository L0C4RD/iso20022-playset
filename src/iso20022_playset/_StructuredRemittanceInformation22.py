# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreditorReferenceInformation3 import CreditorReferenceInformation3
from ._Garnishment4 import Garnishment4
from ._Max140Text import Max140Text
from ._PartyIdentification272 import PartyIdentification272
from ._ReferredDocumentInformation8 import ReferredDocumentInformation8
from ._RemittanceAmount4 import RemittanceAmount4
from ._SecuritiesAttributes1 import SecuritiesAttributes1
from ._TaxData1 import TaxData1

class StructuredRemittanceInformation22(base_types._BaseFieldType):

	__slots__ = ["_AddtlRmtInf", "_CdtrRefInf", "_GrnshmtRmt", "_Invcee", "_Invcr", "_RfrdDocAmt", "_RfrdDocInf", "_SctiesData", "_TaxRmt"]
	@property
	def AddtlRmtInf(self):
		return self._AddtlRmtInf

	@AddtlRmtInf.setter
	def AddtlRmtInf(self, value):
		self._AddtlRmtInf = value if type(value) != base_types.auto else self.make_default("AddtlRmtInf")

	@AddtlRmtInf.deleter
	def AddtlRmtInf(self):
		del self._AddtlRmtInf
		self._AddtlRmtInf = None

	@property
	def CdtrRefInf(self):
		return self._CdtrRefInf

	@CdtrRefInf.setter
	def CdtrRefInf(self, value):
		self._CdtrRefInf = value if type(value) != base_types.auto else self.make_default("CdtrRefInf")

	@CdtrRefInf.deleter
	def CdtrRefInf(self):
		del self._CdtrRefInf
		self._CdtrRefInf = None

	@property
	def GrnshmtRmt(self):
		return self._GrnshmtRmt

	@GrnshmtRmt.setter
	def GrnshmtRmt(self, value):
		self._GrnshmtRmt = value if type(value) != base_types.auto else self.make_default("GrnshmtRmt")

	@GrnshmtRmt.deleter
	def GrnshmtRmt(self):
		del self._GrnshmtRmt
		self._GrnshmtRmt = None

	@property
	def Invcee(self):
		return self._Invcee

	@Invcee.setter
	def Invcee(self, value):
		self._Invcee = value if type(value) != base_types.auto else self.make_default("Invcee")

	@Invcee.deleter
	def Invcee(self):
		del self._Invcee
		self._Invcee = None

	@property
	def Invcr(self):
		return self._Invcr

	@Invcr.setter
	def Invcr(self, value):
		self._Invcr = value if type(value) != base_types.auto else self.make_default("Invcr")

	@Invcr.deleter
	def Invcr(self):
		del self._Invcr
		self._Invcr = None

	@property
	def RfrdDocAmt(self):
		return self._RfrdDocAmt

	@RfrdDocAmt.setter
	def RfrdDocAmt(self, value):
		self._RfrdDocAmt = value if type(value) != base_types.auto else self.make_default("RfrdDocAmt")

	@RfrdDocAmt.deleter
	def RfrdDocAmt(self):
		del self._RfrdDocAmt
		self._RfrdDocAmt = None

	@property
	def RfrdDocInf(self):
		return self._RfrdDocInf

	@RfrdDocInf.setter
	def RfrdDocInf(self, value):
		self._RfrdDocInf = value if type(value) != base_types.auto else self.make_default("RfrdDocInf")

	@RfrdDocInf.deleter
	def RfrdDocInf(self):
		del self._RfrdDocInf
		self._RfrdDocInf = None

	@property
	def SctiesData(self):
		return self._SctiesData

	@SctiesData.setter
	def SctiesData(self, value):
		self._SctiesData = value if type(value) != base_types.auto else self.make_default("SctiesData")

	@SctiesData.deleter
	def SctiesData(self):
		del self._SctiesData
		self._SctiesData = None

	@property
	def TaxRmt(self):
		return self._TaxRmt

	@TaxRmt.setter
	def TaxRmt(self, value):
		self._TaxRmt = value if type(value) != base_types.auto else self.make_default("TaxRmt")

	@TaxRmt.deleter
	def TaxRmt(self):
		del self._TaxRmt
		self._TaxRmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRmtInf', type=Max140Text, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtrRefInf', type=CreditorReferenceInformation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrnshmtRmt', type=Garnishment4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcee', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDocAmt', type=RemittanceAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDocInf', type=ReferredDocumentInformation8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesData', type=SecuritiesAttributes1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRmt', type=TaxData1, min=0, max=1, mutex_group=None, array=False),
	))