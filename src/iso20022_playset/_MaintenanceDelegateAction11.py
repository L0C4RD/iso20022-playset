# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetIdentification11
from . import Max3000Binary
from . import Max35Text
from . import NetworkParameters7
from . import ProcessRetry3
from . import TMSAction14
from . import TrueFalseIndicator

class MaintenanceDelegateAction11(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_AddtlInf", "_DataSetId", "_PrdcActn", "_ReTry", "_TMRmotAccs", "_TMSPrtcol", "_TMSPrtcolVrsn"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', TMSAction14, True)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', TMSAction14, True)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max3000Binary, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max3000Binary, True)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification11, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification11, False)

	@property
	def PrdcActn(self):
		return self._PrdcActn

	@PrdcActn.setter
	def PrdcActn(self, value):
		self._PrdcActn = value if value is not None else base_types.UninitialisedField(self, 'PrdcActn', TrueFalseIndicator, False)

	@PrdcActn.deleter
	def PrdcActn(self):
		del self._PrdcActn
		self._PrdcActn = base_types.UninitialisedField(self, 'PrdcActn', TrueFalseIndicator, False)

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if value is not None else base_types.UninitialisedField(self, 'ReTry', ProcessRetry3, False)

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = base_types.UninitialisedField(self, 'ReTry', ProcessRetry3, False)

	@property
	def TMRmotAccs(self):
		return self._TMRmotAccs

	@TMRmotAccs.setter
	def TMRmotAccs(self, value):
		self._TMRmotAccs = value if value is not None else base_types.UninitialisedField(self, 'TMRmotAccs', NetworkParameters7, False)

	@TMRmotAccs.deleter
	def TMRmotAccs(self):
		del self._TMRmotAccs
		self._TMRmotAccs = base_types.UninitialisedField(self, 'TMRmotAccs', NetworkParameters7, False)

	@property
	def TMSPrtcol(self):
		return self._TMSPrtcol

	@TMSPrtcol.setter
	def TMSPrtcol(self, value):
		self._TMSPrtcol = value if value is not None else base_types.UninitialisedField(self, 'TMSPrtcol', Max35Text, False)

	@TMSPrtcol.deleter
	def TMSPrtcol(self):
		del self._TMSPrtcol
		self._TMSPrtcol = base_types.UninitialisedField(self, 'TMSPrtcol', Max35Text, False)

	@property
	def TMSPrtcolVrsn(self):
		return self._TMSPrtcolVrsn

	@TMSPrtcolVrsn.setter
	def TMSPrtcolVrsn(self, value):
		self._TMSPrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'TMSPrtcolVrsn', Max35Text, False)

	@TMSPrtcolVrsn.deleter
	def TMSPrtcolVrsn(self):
		del self._TMSPrtcolVrsn
		self._TMSPrtcolVrsn = base_types.UninitialisedField(self, 'TMSPrtcolVrsn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=TMSAction14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max3000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdcActn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMRmotAccs', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcol', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcolVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))