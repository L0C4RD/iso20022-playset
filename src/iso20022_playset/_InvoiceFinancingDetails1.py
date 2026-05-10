from . import base_types
from .InstalmentFinancingInformation1 import InstalmentFinancingInformation1
from .PartyIdentification8 import PartyIdentification8
from .OriginalInvoiceInformation1 import OriginalInvoiceInformation1
from .FinancingResult1 import FinancingResult1

class InvoiceFinancingDetails1(base_types._BaseFieldType):

	__slots__ = ["_OrgnlInvcInf", "_InstlmtFincgInf", "_Spplr", "_InvcFincgRslt"]
	@property
	def OrgnlInvcInf(self):
		return self._OrgnlInvcInf

	@OrgnlInvcInf.setter
	def OrgnlInvcInf(self, value):
		self._OrgnlInvcInf = value if type(value) != base_types.auto else self.make_default("OrgnlInvcInf")

	@OrgnlInvcInf.deleter
	def OrgnlInvcInf(self):
		del self._OrgnlInvcInf
		self._OrgnlInvcInf = None

	@property
	def InstlmtFincgInf(self):
		return self._InstlmtFincgInf

	@InstlmtFincgInf.setter
	def InstlmtFincgInf(self, value):
		self._InstlmtFincgInf = value if type(value) != base_types.auto else self.make_default("InstlmtFincgInf")

	@InstlmtFincgInf.deleter
	def InstlmtFincgInf(self):
		del self._InstlmtFincgInf
		self._InstlmtFincgInf = None

	@property
	def Spplr(self):
		return self._Spplr

	@Spplr.setter
	def Spplr(self, value):
		self._Spplr = value if type(value) != base_types.auto else self.make_default("Spplr")

	@Spplr.deleter
	def Spplr(self):
		del self._Spplr
		self._Spplr = None

	@property
	def InvcFincgRslt(self):
		return self._InvcFincgRslt

	@InvcFincgRslt.setter
	def InvcFincgRslt(self, value):
		self._InvcFincgRslt = value if type(value) != base_types.auto else self.make_default("InvcFincgRslt")

	@InvcFincgRslt.deleter
	def InvcFincgRslt(self):
		del self._InvcFincgRslt
		self._InvcFincgRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlInvcInf', type=OriginalInvoiceInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtFincgInf', type=InstalmentFinancingInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Spplr', type=PartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcFincgRslt', type=FinancingResult1, min=1, max=1, mutex_group=None, array=False),
	))

