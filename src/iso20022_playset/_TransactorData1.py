# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import ExternalTransactorType1Code
from . import LocalData20
from . import Max11NumericText
from . import Max15AlphaNumericText
from . import Max35Text
from . import Max99Text
from . import SubMerchant1

class TransactorData1(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_BizId", "_BizNm", "_Id", "_LclData", "_LglCorpNm", "_NtlData", "_PrvtData", "_SubMrchnt", "_Tp"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address4, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address4, False)

	@property
	def BizId(self):
		return self._BizId

	@BizId.setter
	def BizId(self, value):
		self._BizId = value if value is not None else base_types.UninitialisedField(self, 'BizId', Max15AlphaNumericText, False)

	@BizId.deleter
	def BizId(self):
		del self._BizId
		self._BizId = base_types.UninitialisedField(self, 'BizId', Max15AlphaNumericText, False)

	@property
	def BizNm(self):
		return self._BizNm

	@BizNm.setter
	def BizNm(self, value):
		self._BizNm = value if value is not None else base_types.UninitialisedField(self, 'BizNm', Max35Text, False)

	@BizNm.deleter
	def BizNm(self):
		del self._BizNm
		self._BizNm = base_types.UninitialisedField(self, 'BizNm', Max35Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max11NumericText, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max11NumericText, False)

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData20, True)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData20, True)

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'LglCorpNm', Max99Text, False)

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = base_types.UninitialisedField(self, 'LglCorpNm', Max99Text, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def SubMrchnt(self):
		return self._SubMrchnt

	@SubMrchnt.setter
	def SubMrchnt(self, value):
		self._SubMrchnt = value if value is not None else base_types.UninitialisedField(self, 'SubMrchnt', SubMerchant1, True)

	@SubMrchnt.deleter
	def SubMrchnt(self):
		del self._SubMrchnt
		self._SubMrchnt = base_types.UninitialisedField(self, 'SubMrchnt', SubMerchant1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ExternalTransactorType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ExternalTransactorType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizId', type=Max15AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max11NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubMrchnt', type=SubMerchant1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ExternalTransactorType1Code, min=1, max=1, mutex_group=None, array=False),
	))