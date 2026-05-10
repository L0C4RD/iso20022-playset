from . import base_types
from .Max35Text import Max35Text
from .LocalAddress1 import LocalAddress1
from .ISOMax3ALanguageCode import ISOMax3ALanguageCode
from .CardholderName2 import CardholderName2
from .AdditionalData1 import AdditionalData1

class LocalData15(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Nm", "_NcodgFrmt", "_Lang", "_AddtlData"]
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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

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
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=LocalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=CardholderName2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
	))

