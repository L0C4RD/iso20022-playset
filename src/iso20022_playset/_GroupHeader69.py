# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalDocumentType1Code
from . import ISODate
from . import LanguageCode
from . import Max35Text
from . import PartyIdentification116

class GroupHeader69(base_types._BaseFieldType):

	__slots__ = ["_BuyrTaxRprtv", "_Id", "_IssdDt", "_LangCd", "_OrgnlId", "_RptCtgy", "_SellrTaxRprtv", "_TaxRptPurp"]
	@property
	def BuyrTaxRprtv(self):
		return self._BuyrTaxRprtv

	@BuyrTaxRprtv.setter
	def BuyrTaxRprtv(self, value):
		self._BuyrTaxRprtv = value if value is not None else base_types.UninitialisedField(self, 'BuyrTaxRprtv', PartyIdentification116, False)

	@BuyrTaxRprtv.deleter
	def BuyrTaxRprtv(self):
		del self._BuyrTaxRprtv
		self._BuyrTaxRprtv = base_types.UninitialisedField(self, 'BuyrTaxRprtv', PartyIdentification116, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def IssdDt(self):
		return self._IssdDt

	@IssdDt.setter
	def IssdDt(self, value):
		self._IssdDt = value if value is not None else base_types.UninitialisedField(self, 'IssdDt', ISODate, False)

	@IssdDt.deleter
	def IssdDt(self):
		del self._IssdDt
		self._IssdDt = base_types.UninitialisedField(self, 'IssdDt', ISODate, False)

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if value is not None else base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@property
	def OrgnlId(self):
		return self._OrgnlId

	@OrgnlId.setter
	def OrgnlId(self, value):
		self._OrgnlId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlId', Max35Text, False)

	@OrgnlId.deleter
	def OrgnlId(self):
		del self._OrgnlId
		self._OrgnlId = base_types.UninitialisedField(self, 'OrgnlId', Max35Text, False)

	@property
	def RptCtgy(self):
		return self._RptCtgy

	@RptCtgy.setter
	def RptCtgy(self, value):
		self._RptCtgy = value if value is not None else base_types.UninitialisedField(self, 'RptCtgy', ExternalDocumentType1Code, False)

	@RptCtgy.deleter
	def RptCtgy(self):
		del self._RptCtgy
		self._RptCtgy = base_types.UninitialisedField(self, 'RptCtgy', ExternalDocumentType1Code, False)

	@property
	def SellrTaxRprtv(self):
		return self._SellrTaxRprtv

	@SellrTaxRprtv.setter
	def SellrTaxRprtv(self, value):
		self._SellrTaxRprtv = value if value is not None else base_types.UninitialisedField(self, 'SellrTaxRprtv', PartyIdentification116, False)

	@SellrTaxRprtv.deleter
	def SellrTaxRprtv(self):
		del self._SellrTaxRprtv
		self._SellrTaxRprtv = base_types.UninitialisedField(self, 'SellrTaxRprtv', PartyIdentification116, False)

	@property
	def TaxRptPurp(self):
		return self._TaxRptPurp

	@TaxRptPurp.setter
	def TaxRptPurp(self, value):
		self._TaxRptPurp = value if value is not None else base_types.UninitialisedField(self, 'TaxRptPurp', ExternalDocumentType1Code, False)

	@TaxRptPurp.deleter
	def TaxRptPurp(self):
		del self._TaxRptPurp
		self._TaxRptPurp = base_types.UninitialisedField(self, 'TaxRptPurp', ExternalDocumentType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrTaxRprtv', type=PartyIdentification116, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssdDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptCtgy', type=ExternalDocumentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrTaxRprtv', type=PartyIdentification116, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRptPurp', type=ExternalDocumentType1Code, min=1, max=1, mutex_group=None, array=False),
	))