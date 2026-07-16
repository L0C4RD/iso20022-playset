# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import LocalData18
from . import Max15AlphaNumericText
from . import Max35Text
from . import Max70Text
from . import Max99Text

class AcceptorData2(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxRefNb", "_ApldAdr", "_BizNm", "_BizRegnId", "_BizRegnIdTp", "_Id", "_LclData", "_LglCorpNm", "_NtlData", "_PrtnrId", "_PrvtData", "_SchmeAssgndId", "_SubmittdAdr"]
	@property
	def AddtlTxRefNb(self):
		return self._AddtlTxRefNb

	@AddtlTxRefNb.setter
	def AddtlTxRefNb(self, value):
		self._AddtlTxRefNb = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxRefNb', Max70Text, False)

	@AddtlTxRefNb.deleter
	def AddtlTxRefNb(self):
		del self._AddtlTxRefNb
		self._AddtlTxRefNb = base_types.UninitialisedField(self, 'AddtlTxRefNb', Max70Text, False)

	@property
	def ApldAdr(self):
		return self._ApldAdr

	@ApldAdr.setter
	def ApldAdr(self, value):
		self._ApldAdr = value if value is not None else base_types.UninitialisedField(self, 'ApldAdr', Address4, False)

	@ApldAdr.deleter
	def ApldAdr(self):
		del self._ApldAdr
		self._ApldAdr = base_types.UninitialisedField(self, 'ApldAdr', Address4, False)

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
	def BizRegnId(self):
		return self._BizRegnId

	@BizRegnId.setter
	def BizRegnId(self, value):
		self._BizRegnId = value if value is not None else base_types.UninitialisedField(self, 'BizRegnId', Max35Text, False)

	@BizRegnId.deleter
	def BizRegnId(self):
		del self._BizRegnId
		self._BizRegnId = base_types.UninitialisedField(self, 'BizRegnId', Max35Text, False)

	@property
	def BizRegnIdTp(self):
		return self._BizRegnIdTp

	@BizRegnIdTp.setter
	def BizRegnIdTp(self, value):
		self._BizRegnIdTp = value if value is not None else base_types.UninitialisedField(self, 'BizRegnIdTp', Max35Text, False)

	@BizRegnIdTp.deleter
	def BizRegnIdTp(self):
		del self._BizRegnIdTp
		self._BizRegnIdTp = base_types.UninitialisedField(self, 'BizRegnIdTp', Max35Text, False)

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
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData18, True)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData18, True)

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
	def PrtnrId(self):
		return self._PrtnrId

	@PrtnrId.setter
	def PrtnrId(self, value):
		self._PrtnrId = value if value is not None else base_types.UninitialisedField(self, 'PrtnrId', Max35Text, False)

	@PrtnrId.deleter
	def PrtnrId(self):
		del self._PrtnrId
		self._PrtnrId = base_types.UninitialisedField(self, 'PrtnrId', Max35Text, False)

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
	def SchmeAssgndId(self):
		return self._SchmeAssgndId

	@SchmeAssgndId.setter
	def SchmeAssgndId(self, value):
		self._SchmeAssgndId = value if value is not None else base_types.UninitialisedField(self, 'SchmeAssgndId', Max15AlphaNumericText, False)

	@SchmeAssgndId.deleter
	def SchmeAssgndId(self):
		del self._SchmeAssgndId
		self._SchmeAssgndId = base_types.UninitialisedField(self, 'SchmeAssgndId', Max15AlphaNumericText, False)

	@property
	def SubmittdAdr(self):
		return self._SubmittdAdr

	@SubmittdAdr.setter
	def SubmittdAdr(self, value):
		self._SubmittdAdr = value if value is not None else base_types.UninitialisedField(self, 'SubmittdAdr', Address4, False)

	@SubmittdAdr.deleter
	def SubmittdAdr(self):
		del self._SubmittdAdr
		self._SubmittdAdr = base_types.UninitialisedField(self, 'SubmittdAdr', Address4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizRegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizRegnIdTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtnrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SchmeAssgndId', type=Max15AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmittdAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
	))