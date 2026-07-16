# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancingResult1
from . import InstalmentFinancingInformation1
from . import OriginalInvoiceInformation1
from . import PartyIdentification8

class InvoiceFinancingDetails1(base_types._BaseFieldType):

	__slots__ = ["_InstlmtFincgInf", "_InvcFincgRslt", "_OrgnlInvcInf", "_Spplr"]
	@property
	def InstlmtFincgInf(self):
		return self._InstlmtFincgInf

	@InstlmtFincgInf.setter
	def InstlmtFincgInf(self, value):
		self._InstlmtFincgInf = value if value is not None else base_types.UninitialisedField(self, 'InstlmtFincgInf', InstalmentFinancingInformation1, True)

	@InstlmtFincgInf.deleter
	def InstlmtFincgInf(self):
		del self._InstlmtFincgInf
		self._InstlmtFincgInf = base_types.UninitialisedField(self, 'InstlmtFincgInf', InstalmentFinancingInformation1, True)

	@property
	def InvcFincgRslt(self):
		return self._InvcFincgRslt

	@InvcFincgRslt.setter
	def InvcFincgRslt(self, value):
		self._InvcFincgRslt = value if value is not None else base_types.UninitialisedField(self, 'InvcFincgRslt', FinancingResult1, False)

	@InvcFincgRslt.deleter
	def InvcFincgRslt(self):
		del self._InvcFincgRslt
		self._InvcFincgRslt = base_types.UninitialisedField(self, 'InvcFincgRslt', FinancingResult1, False)

	@property
	def OrgnlInvcInf(self):
		return self._OrgnlInvcInf

	@OrgnlInvcInf.setter
	def OrgnlInvcInf(self, value):
		self._OrgnlInvcInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInvcInf', OriginalInvoiceInformation1, False)

	@OrgnlInvcInf.deleter
	def OrgnlInvcInf(self):
		del self._OrgnlInvcInf
		self._OrgnlInvcInf = base_types.UninitialisedField(self, 'OrgnlInvcInf', OriginalInvoiceInformation1, False)

	@property
	def Spplr(self):
		return self._Spplr

	@Spplr.setter
	def Spplr(self, value):
		self._Spplr = value if value is not None else base_types.UninitialisedField(self, 'Spplr', PartyIdentification8, False)

	@Spplr.deleter
	def Spplr(self):
		del self._Spplr
		self._Spplr = base_types.UninitialisedField(self, 'Spplr', PartyIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstlmtFincgInf', type=InstalmentFinancingInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcFincgRslt', type=FinancingResult1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvcInf', type=OriginalInvoiceInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Spplr', type=PartyIdentification8, min=0, max=1, mutex_group=None, array=False),
	))