from . import base_types
import Max2000Text
import BaseOneRate
import ModelType1Choice
import TrueFalseIndicator

class BackTestingMethodology1(base_types._BaseFieldType):

	__slots__ = ["_VartnMrgnCleanInd", "_MdlCnfdncLvl", "_RskMdlTp", "_Desc"]
	@property
	def VartnMrgnCleanInd(self):
		return self._VartnMrgnCleanInd

	@VartnMrgnCleanInd.setter
	def VartnMrgnCleanInd(self, value):
		self._VartnMrgnCleanInd = value if type(value) != auto else self.make_default("VartnMrgnCleanInd")

	@VartnMrgnCleanInd.deleter
	def VartnMrgnCleanInd(self):
		del self._VartnMrgnCleanInd
		self._VartnMrgnCleanInd = None

	@property
	def MdlCnfdncLvl(self):
		return self._MdlCnfdncLvl

	@MdlCnfdncLvl.setter
	def MdlCnfdncLvl(self, value):
		self._MdlCnfdncLvl = value if type(value) != auto else self.make_default("MdlCnfdncLvl")

	@MdlCnfdncLvl.deleter
	def MdlCnfdncLvl(self):
		del self._MdlCnfdncLvl
		self._MdlCnfdncLvl = None

	@property
	def RskMdlTp(self):
		return self._RskMdlTp

	@RskMdlTp.setter
	def RskMdlTp(self, value):
		self._RskMdlTp = value if type(value) != auto else self.make_default("RskMdlTp")

	@RskMdlTp.deleter
	def RskMdlTp(self):
		del self._RskMdlTp
		self._RskMdlTp = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VartnMrgnCleanInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlCnfdncLvl', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskMdlTp', type=ModelType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
	))

