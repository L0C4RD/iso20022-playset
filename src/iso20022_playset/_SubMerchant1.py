from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._GeographicPointInDecimalDegreesText import GeographicPointInDecimalDegreesText
from ._ISO3NumericCountryCode import ISO3NumericCountryCode
from ._LocalData20 import LocalData20
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._Max3Text import Max3Text
from ._Max99Text import Max99Text

class SubMerchant1(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Assgnr", "_BizNm", "_Ctry", "_Frgn", "_GeogcLctn", "_Id", "_LclData", "_LglCorpNm", "_NtlData", "_PrvtData"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def BizNm(self):
		return self._BizNm

	@BizNm.setter
	def BizNm(self, value):
		self._BizNm = value if type(value) != base_types.auto else self.make_default("BizNm")

	@BizNm.deleter
	def BizNm(self):
		del self._BizNm
		self._BizNm = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def Frgn(self):
		return self._Frgn

	@Frgn.setter
	def Frgn(self, value):
		self._Frgn = value if type(value) != base_types.auto else self.make_default("Frgn")

	@Frgn.deleter
	def Frgn(self):
		del self._Frgn
		self._Frgn = None

	@property
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if type(value) != base_types.auto else self.make_default("GeogcLctn")

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = None

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
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != base_types.auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if type(value) != base_types.auto else self.make_default("LglCorpNm")

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frgn', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegreesText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
	))

