# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorReferenceInformation3
from . import Garnishment4
from . import Max140Text
from . import PartyIdentification272
from . import ReferredDocumentInformation8
from . import RemittanceAmount4
from . import TaxData1

class StructuredRemittanceInformation18(base_types._BaseFieldType):

	__slots__ = ["_AddtlRmtInf", "_CdtrRefInf", "_GrnshmtRmt", "_Invcee", "_Invcr", "_RfrdDocAmt", "_RfrdDocInf", "_TaxRmt"]
	@property
	def AddtlRmtInf(self):
		return self._AddtlRmtInf

	@AddtlRmtInf.setter
	def AddtlRmtInf(self, value):
		self._AddtlRmtInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRmtInf', Max140Text, True)

	@AddtlRmtInf.deleter
	def AddtlRmtInf(self):
		del self._AddtlRmtInf
		self._AddtlRmtInf = base_types.UninitialisedField(self, 'AddtlRmtInf', Max140Text, True)

	@property
	def CdtrRefInf(self):
		return self._CdtrRefInf

	@CdtrRefInf.setter
	def CdtrRefInf(self, value):
		self._CdtrRefInf = value if value is not None else base_types.UninitialisedField(self, 'CdtrRefInf', CreditorReferenceInformation3, False)

	@CdtrRefInf.deleter
	def CdtrRefInf(self):
		del self._CdtrRefInf
		self._CdtrRefInf = base_types.UninitialisedField(self, 'CdtrRefInf', CreditorReferenceInformation3, False)

	@property
	def GrnshmtRmt(self):
		return self._GrnshmtRmt

	@GrnshmtRmt.setter
	def GrnshmtRmt(self, value):
		self._GrnshmtRmt = value if value is not None else base_types.UninitialisedField(self, 'GrnshmtRmt', Garnishment4, False)

	@GrnshmtRmt.deleter
	def GrnshmtRmt(self):
		del self._GrnshmtRmt
		self._GrnshmtRmt = base_types.UninitialisedField(self, 'GrnshmtRmt', Garnishment4, False)

	@property
	def Invcee(self):
		return self._Invcee

	@Invcee.setter
	def Invcee(self, value):
		self._Invcee = value if value is not None else base_types.UninitialisedField(self, 'Invcee', PartyIdentification272, False)

	@Invcee.deleter
	def Invcee(self):
		del self._Invcee
		self._Invcee = base_types.UninitialisedField(self, 'Invcee', PartyIdentification272, False)

	@property
	def Invcr(self):
		return self._Invcr

	@Invcr.setter
	def Invcr(self, value):
		self._Invcr = value if value is not None else base_types.UninitialisedField(self, 'Invcr', PartyIdentification272, False)

	@Invcr.deleter
	def Invcr(self):
		del self._Invcr
		self._Invcr = base_types.UninitialisedField(self, 'Invcr', PartyIdentification272, False)

	@property
	def RfrdDocAmt(self):
		return self._RfrdDocAmt

	@RfrdDocAmt.setter
	def RfrdDocAmt(self, value):
		self._RfrdDocAmt = value if value is not None else base_types.UninitialisedField(self, 'RfrdDocAmt', RemittanceAmount4, False)

	@RfrdDocAmt.deleter
	def RfrdDocAmt(self):
		del self._RfrdDocAmt
		self._RfrdDocAmt = base_types.UninitialisedField(self, 'RfrdDocAmt', RemittanceAmount4, False)

	@property
	def RfrdDocInf(self):
		return self._RfrdDocInf

	@RfrdDocInf.setter
	def RfrdDocInf(self, value):
		self._RfrdDocInf = value if value is not None else base_types.UninitialisedField(self, 'RfrdDocInf', ReferredDocumentInformation8, True)

	@RfrdDocInf.deleter
	def RfrdDocInf(self):
		del self._RfrdDocInf
		self._RfrdDocInf = base_types.UninitialisedField(self, 'RfrdDocInf', ReferredDocumentInformation8, True)

	@property
	def TaxRmt(self):
		return self._TaxRmt

	@TaxRmt.setter
	def TaxRmt(self, value):
		self._TaxRmt = value if value is not None else base_types.UninitialisedField(self, 'TaxRmt', TaxData1, False)

	@TaxRmt.deleter
	def TaxRmt(self):
		del self._TaxRmt
		self._TaxRmt = base_types.UninitialisedField(self, 'TaxRmt', TaxData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRmtInf', type=Max140Text, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtrRefInf', type=CreditorReferenceInformation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrnshmtRmt', type=Garnishment4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcee', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDocAmt', type=RemittanceAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDocInf', type=ReferredDocumentInformation8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRmt', type=TaxData1, min=0, max=1, mutex_group=None, array=False),
	))