from . import base_types
from ._Case6 import Case6
from ._ExternalInvestigationExecutionConfirmation1Code import ExternalInvestigationExecutionConfirmation1Code
from ._ModificationStatusReason1Choice import ModificationStatusReason1Choice
from ._YesNoIndicator import YesNoIndicator

class InvestigationStatus6Choice(base_types._BaseFieldType):

	__slots__ = ["_AssgnmtCxlConf", "_Conf", "_DplctOf", "_RjctdMod"]
	@property
	def AssgnmtCxlConf(self):
		return self._AssgnmtCxlConf

	@AssgnmtCxlConf.setter
	def AssgnmtCxlConf(self, value):
		self._AssgnmtCxlConf = value if type(value) != base_types.auto else self.make_default("AssgnmtCxlConf")

	@AssgnmtCxlConf.deleter
	def AssgnmtCxlConf(self):
		del self._AssgnmtCxlConf
		self._AssgnmtCxlConf = None

	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if type(value) != base_types.auto else self.make_default("Conf")

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = None

	@property
	def DplctOf(self):
		return self._DplctOf

	@DplctOf.setter
	def DplctOf(self, value):
		self._DplctOf = value if type(value) != base_types.auto else self.make_default("DplctOf")

	@DplctOf.deleter
	def DplctOf(self):
		del self._DplctOf
		self._DplctOf = None

	@property
	def RjctdMod(self):
		return self._RjctdMod

	@RjctdMod.setter
	def RjctdMod(self, value):
		self._RjctdMod = value if type(value) != base_types.auto else self.make_default("RjctdMod")

	@RjctdMod.deleter
	def RjctdMod(self):
		del self._RjctdMod
		self._RjctdMod = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssgnmtCxlConf', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Conf', type=ExternalInvestigationExecutionConfirmation1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DplctOf', type=Case6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdMod', type=ModificationStatusReason1Choice, min=1, max=None, mutex_group=1, array=True),
	))

