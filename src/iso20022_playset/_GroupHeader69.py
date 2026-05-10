from . import base_types
from ._PartyIdentification116 import PartyIdentification116
from ._ExternalDocumentType1Code import ExternalDocumentType1Code
from ._Max35Text import Max35Text
from ._LanguageCode import LanguageCode
from ._ISODate import ISODate

class GroupHeader69(base_types._BaseFieldType):

	__slots__ = ["_TaxRptPurp", "_OrgnlId", "_SellrTaxRprtv", "_BuyrTaxRprtv", "_Id", "_RptCtgy", "_LangCd", "_IssdDt"]
	@property
	def TaxRptPurp(self):
		return self._TaxRptPurp

	@TaxRptPurp.setter
	def TaxRptPurp(self, value):
		self._TaxRptPurp = value if type(value) != base_types.auto else self.make_default("TaxRptPurp")

	@TaxRptPurp.deleter
	def TaxRptPurp(self):
		del self._TaxRptPurp
		self._TaxRptPurp = None

	@property
	def OrgnlId(self):
		return self._OrgnlId

	@OrgnlId.setter
	def OrgnlId(self, value):
		self._OrgnlId = value if type(value) != base_types.auto else self.make_default("OrgnlId")

	@OrgnlId.deleter
	def OrgnlId(self):
		del self._OrgnlId
		self._OrgnlId = None

	@property
	def SellrTaxRprtv(self):
		return self._SellrTaxRprtv

	@SellrTaxRprtv.setter
	def SellrTaxRprtv(self, value):
		self._SellrTaxRprtv = value if type(value) != base_types.auto else self.make_default("SellrTaxRprtv")

	@SellrTaxRprtv.deleter
	def SellrTaxRprtv(self):
		del self._SellrTaxRprtv
		self._SellrTaxRprtv = None

	@property
	def BuyrTaxRprtv(self):
		return self._BuyrTaxRprtv

	@BuyrTaxRprtv.setter
	def BuyrTaxRprtv(self, value):
		self._BuyrTaxRprtv = value if type(value) != base_types.auto else self.make_default("BuyrTaxRprtv")

	@BuyrTaxRprtv.deleter
	def BuyrTaxRprtv(self):
		del self._BuyrTaxRprtv
		self._BuyrTaxRprtv = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def RptCtgy(self):
		return self._RptCtgy

	@RptCtgy.setter
	def RptCtgy(self, value):
		self._RptCtgy = value if type(value) != base_types.auto else self.make_default("RptCtgy")

	@RptCtgy.deleter
	def RptCtgy(self):
		del self._RptCtgy
		self._RptCtgy = None

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if type(value) != base_types.auto else self.make_default("LangCd")

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = None

	@property
	def IssdDt(self):
		return self._IssdDt

	@IssdDt.setter
	def IssdDt(self, value):
		self._IssdDt = value if type(value) != base_types.auto else self.make_default("IssdDt")

	@IssdDt.deleter
	def IssdDt(self):
		del self._IssdDt
		self._IssdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxRptPurp', type=ExternalDocumentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrTaxRprtv', type=PartyIdentification116, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrTaxRprtv', type=PartyIdentification116, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptCtgy', type=ExternalDocumentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssdDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

