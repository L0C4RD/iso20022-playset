# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ISOMax3ALanguageCode
from . import LocalAddress1
from . import LocalAddress2
from . import Max200Text
from . import Max210Text
from . import Max35Text
from . import Max512Text
from . import Max70Text

class LocalData19(base_types._BaseFieldType):

	__slots__ = ["_AddtlAdr", "_AddtlCtct", "_Adr", "_BizNm", "_Lang", "_LglCorpNm", "_NcodgFrmt", "_NmAndLctn", "_NtlData", "_PrvtData", "_SvcLctn"]
	@property
	def AddtlAdr(self):
		return self._AddtlAdr

	@AddtlAdr.setter
	def AddtlAdr(self, value):
		self._AddtlAdr = value if value is not None else base_types.UninitialisedField(self, 'AddtlAdr', Max512Text, False)

	@AddtlAdr.deleter
	def AddtlAdr(self):
		del self._AddtlAdr
		self._AddtlAdr = base_types.UninitialisedField(self, 'AddtlAdr', Max512Text, False)

	@property
	def AddtlCtct(self):
		return self._AddtlCtct

	@AddtlCtct.setter
	def AddtlCtct(self, value):
		self._AddtlCtct = value if value is not None else base_types.UninitialisedField(self, 'AddtlCtct', Max512Text, False)

	@AddtlCtct.deleter
	def AddtlCtct(self):
		del self._AddtlCtct
		self._AddtlCtct = base_types.UninitialisedField(self, 'AddtlCtct', Max512Text, False)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', LocalAddress2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', LocalAddress2, False)

	@property
	def BizNm(self):
		return self._BizNm

	@BizNm.setter
	def BizNm(self, value):
		self._BizNm = value if value is not None else base_types.UninitialisedField(self, 'BizNm', Max70Text, False)

	@BizNm.deleter
	def BizNm(self):
		del self._BizNm
		self._BizNm = base_types.UninitialisedField(self, 'BizNm', Max70Text, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'LglCorpNm', Max210Text, False)

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = base_types.UninitialisedField(self, 'LglCorpNm', Max210Text, False)

	@property
	def NcodgFrmt(self):
		return self._NcodgFrmt

	@NcodgFrmt.setter
	def NcodgFrmt(self, value):
		self._NcodgFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@NcodgFrmt.deleter
	def NcodgFrmt(self):
		del self._NcodgFrmt
		self._NcodgFrmt = base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if value is not None else base_types.UninitialisedField(self, 'NmAndLctn', Max200Text, False)

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = base_types.UninitialisedField(self, 'NmAndLctn', Max200Text, False)

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
	def SvcLctn(self):
		return self._SvcLctn

	@SvcLctn.setter
	def SvcLctn(self, value):
		self._SvcLctn = value if value is not None else base_types.UninitialisedField(self, 'SvcLctn', LocalAddress1, False)

	@SvcLctn.deleter
	def SvcLctn(self):
		del self._SvcLctn
		self._SvcLctn = base_types.UninitialisedField(self, 'SvcLctn', LocalAddress1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAdr', type=Max512Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCtct', type=Max512Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=LocalAddress2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCorpNm', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndLctn', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcLctn', type=LocalAddress1, min=0, max=1, mutex_group=None, array=False),
	))