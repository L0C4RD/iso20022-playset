import base_types
import AdditionalData1
import Max70Text
import LocalAddress1
import Max280Text
import Max35Text
import Max512Text
import Max210Text
import ISOMax3ALanguageCode

class LocalData12(base_types._BaseFieldType):

	__slots__ = ["_Lang", "_ShrtNm", "_AddtlAdr", "_NcodgFrmt", "_Adr", "_LglCorpNm", "_AddtlData", "_CmonNm"]
	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def AddtlAdr(self):
		return self._AddtlAdr

	@AddtlAdr.setter
	def AddtlAdr(self, value):
		self._AddtlAdr = value if type(value) != auto else self.make_default("AddtlAdr")

	@AddtlAdr.deleter
	def AddtlAdr(self):
		del self._AddtlAdr
		self._AddtlAdr = None

	@property
	def NcodgFrmt(self):
		return self._NcodgFrmt

	@NcodgFrmt.setter
	def NcodgFrmt(self, value):
		self._NcodgFrmt = value if type(value) != auto else self.make_default("NcodgFrmt")

	@NcodgFrmt.deleter
	def NcodgFrmt(self):
		del self._NcodgFrmt
		self._NcodgFrmt = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if type(value) != auto else self.make_default("LglCorpNm")

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def CmonNm(self):
		return self._CmonNm

	@CmonNm.setter
	def CmonNm(self, value):
		self._CmonNm = value if type(value) != auto else self.make_default("CmonNm")

	@CmonNm.deleter
	def CmonNm(self):
		del self._CmonNm
		self._CmonNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAdr', type=Max512Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=LocalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCorpNm', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmonNm', type=Max280Text, min=0, max=1, mutex_group=None, array=False),
	))

