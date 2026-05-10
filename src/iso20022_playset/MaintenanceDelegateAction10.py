from . import base_types
from .Max35Text import Max35Text
from .TMSAction13 import TMSAction13
from .ProcessRetry3 import ProcessRetry3
from .Max3000Binary import Max3000Binary
from .TrueFalseIndicator import TrueFalseIndicator
from .NetworkParameters7 import NetworkParameters7
from .DataSetIdentification11 import DataSetIdentification11

class MaintenanceDelegateAction10(base_types._BaseFieldType):

	__slots__ = ["_PrdcActn", "_Actn", "_TMRmotAccs", "_TMSPrtcolVrsn", "_ReTry", "_TMSPrtcol", "_AddtlInf", "_DataSetId"]
	@property
	def PrdcActn(self):
		return self._PrdcActn

	@PrdcActn.setter
	def PrdcActn(self, value):
		self._PrdcActn = value if type(value) != auto else self.make_default("PrdcActn")

	@PrdcActn.deleter
	def PrdcActn(self):
		del self._PrdcActn
		self._PrdcActn = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def TMRmotAccs(self):
		return self._TMRmotAccs

	@TMRmotAccs.setter
	def TMRmotAccs(self, value):
		self._TMRmotAccs = value if type(value) != auto else self.make_default("TMRmotAccs")

	@TMRmotAccs.deleter
	def TMRmotAccs(self):
		del self._TMRmotAccs
		self._TMRmotAccs = None

	@property
	def TMSPrtcolVrsn(self):
		return self._TMSPrtcolVrsn

	@TMSPrtcolVrsn.setter
	def TMSPrtcolVrsn(self, value):
		self._TMSPrtcolVrsn = value if type(value) != auto else self.make_default("TMSPrtcolVrsn")

	@TMSPrtcolVrsn.deleter
	def TMSPrtcolVrsn(self):
		del self._TMSPrtcolVrsn
		self._TMSPrtcolVrsn = None

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if type(value) != auto else self.make_default("ReTry")

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = None

	@property
	def TMSPrtcol(self):
		return self._TMSPrtcol

	@TMSPrtcol.setter
	def TMSPrtcol(self, value):
		self._TMSPrtcol = value if type(value) != auto else self.make_default("TMSPrtcol")

	@TMSPrtcol.deleter
	def TMSPrtcol(self):
		del self._TMSPrtcol
		self._TMSPrtcol = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrdcActn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=TMSAction13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMRmotAccs', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcolVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcol', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max3000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification11, min=0, max=1, mutex_group=None, array=False),
	))

