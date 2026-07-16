# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import ExternalInvestigationExecutionConfirmation1Code
from . import ModificationStatusReason1Choice
from . import YesNoIndicator

class InvestigationStatus6Choice(base_types._BaseFieldType):

	__slots__ = ["_AssgnmtCxlConf", "_Conf", "_DplctOf", "_RjctdMod"]
	@property
	def AssgnmtCxlConf(self):
		return self._AssgnmtCxlConf

	@AssgnmtCxlConf.setter
	def AssgnmtCxlConf(self, value):
		self._AssgnmtCxlConf = value if value is not None else base_types.UninitialisedField(self, 'AssgnmtCxlConf', YesNoIndicator, False)

	@AssgnmtCxlConf.deleter
	def AssgnmtCxlConf(self):
		del self._AssgnmtCxlConf
		self._AssgnmtCxlConf = base_types.UninitialisedField(self, 'AssgnmtCxlConf', YesNoIndicator, False)

	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if value is not None else base_types.UninitialisedField(self, 'Conf', ExternalInvestigationExecutionConfirmation1Code, False)

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = base_types.UninitialisedField(self, 'Conf', ExternalInvestigationExecutionConfirmation1Code, False)

	@property
	def DplctOf(self):
		return self._DplctOf

	@DplctOf.setter
	def DplctOf(self, value):
		self._DplctOf = value if value is not None else base_types.UninitialisedField(self, 'DplctOf', Case6, False)

	@DplctOf.deleter
	def DplctOf(self):
		del self._DplctOf
		self._DplctOf = base_types.UninitialisedField(self, 'DplctOf', Case6, False)

	@property
	def RjctdMod(self):
		return self._RjctdMod

	@RjctdMod.setter
	def RjctdMod(self, value):
		self._RjctdMod = value if value is not None else base_types.UninitialisedField(self, 'RjctdMod', ModificationStatusReason1Choice, True)

	@RjctdMod.deleter
	def RjctdMod(self):
		del self._RjctdMod
		self._RjctdMod = base_types.UninitialisedField(self, 'RjctdMod', ModificationStatusReason1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssgnmtCxlConf', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Conf', type=ExternalInvestigationExecutionConfirmation1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DplctOf', type=Case6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdMod', type=ModificationStatusReason1Choice, min=1, max=None, mutex_group=1, array=True),
	))