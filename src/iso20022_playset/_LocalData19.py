# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ISOMax3ALanguageCode import ISOMax3ALanguageCode
from ._LocalAddress1 import LocalAddress1
from ._LocalAddress2 import LocalAddress2
from ._Max200Text import Max200Text
from ._Max210Text import Max210Text
from ._Max35Text import Max35Text
from ._Max512Text import Max512Text
from ._Max70Text import Max70Text

class LocalData19(base_types._BaseFieldType):

	__slots__ = ["_AddtlAdr", "_AddtlCtct", "_Adr", "_BizNm", "_Lang", "_LglCorpNm", "_NcodgFrmt", "_NmAndLctn", "_NtlData", "_PrvtData", "_SvcLctn"]
	@property
	def AddtlAdr(self):
		return self._AddtlAdr

	@AddtlAdr.setter
	def AddtlAdr(self, value):
		self._AddtlAdr = value if type(value) != base_types.auto else self.make_default("AddtlAdr")

	@AddtlAdr.deleter
	def AddtlAdr(self):
		del self._AddtlAdr
		self._AddtlAdr = None

	@property
	def AddtlCtct(self):
		return self._AddtlCtct

	@AddtlCtct.setter
	def AddtlCtct(self, value):
		self._AddtlCtct = value if type(value) != base_types.auto else self.make_default("AddtlCtct")

	@AddtlCtct.deleter
	def AddtlCtct(self):
		del self._AddtlCtct
		self._AddtlCtct = None

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
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

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
	def NcodgFrmt(self):
		return self._NcodgFrmt

	@NcodgFrmt.setter
	def NcodgFrmt(self, value):
		self._NcodgFrmt = value if type(value) != base_types.auto else self.make_default("NcodgFrmt")

	@NcodgFrmt.deleter
	def NcodgFrmt(self):
		del self._NcodgFrmt
		self._NcodgFrmt = None

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if type(value) != base_types.auto else self.make_default("NmAndLctn")

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = None

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

	@property
	def SvcLctn(self):
		return self._SvcLctn

	@SvcLctn.setter
	def SvcLctn(self, value):
		self._SvcLctn = value if type(value) != base_types.auto else self.make_default("SvcLctn")

	@SvcLctn.deleter
	def SvcLctn(self):
		del self._SvcLctn
		self._SvcLctn = None

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