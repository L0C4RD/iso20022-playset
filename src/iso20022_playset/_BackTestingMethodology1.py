# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import Max2000Text
from . import ModelType1Choice
from . import TrueFalseIndicator

class BackTestingMethodology1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_MdlCnfdncLvl", "_RskMdlTp", "_VartnMrgnCleanInd"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@property
	def MdlCnfdncLvl(self):
		return self._MdlCnfdncLvl

	@MdlCnfdncLvl.setter
	def MdlCnfdncLvl(self, value):
		self._MdlCnfdncLvl = value if value is not None else base_types.UninitialisedField(self, 'MdlCnfdncLvl', BaseOneRate, False)

	@MdlCnfdncLvl.deleter
	def MdlCnfdncLvl(self):
		del self._MdlCnfdncLvl
		self._MdlCnfdncLvl = base_types.UninitialisedField(self, 'MdlCnfdncLvl', BaseOneRate, False)

	@property
	def RskMdlTp(self):
		return self._RskMdlTp

	@RskMdlTp.setter
	def RskMdlTp(self, value):
		self._RskMdlTp = value if value is not None else base_types.UninitialisedField(self, 'RskMdlTp', ModelType1Choice, False)

	@RskMdlTp.deleter
	def RskMdlTp(self):
		del self._RskMdlTp
		self._RskMdlTp = base_types.UninitialisedField(self, 'RskMdlTp', ModelType1Choice, False)

	@property
	def VartnMrgnCleanInd(self):
		return self._VartnMrgnCleanInd

	@VartnMrgnCleanInd.setter
	def VartnMrgnCleanInd(self, value):
		self._VartnMrgnCleanInd = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnCleanInd', TrueFalseIndicator, False)

	@VartnMrgnCleanInd.deleter
	def VartnMrgnCleanInd(self):
		del self._VartnMrgnCleanInd
		self._VartnMrgnCleanInd = base_types.UninitialisedField(self, 'VartnMrgnCleanInd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlCnfdncLvl', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskMdlTp', type=ModelType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnCleanInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
	))