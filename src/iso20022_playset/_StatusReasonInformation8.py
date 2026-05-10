from . import base_types
from ._PartyIdentification32 import PartyIdentification32
from ._StatusReason6Choice import StatusReason6Choice
from ._Max105Text import Max105Text

class StatusReasonInformation8(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_Orgtr", "_AddtlInf"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != base_types.auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=StatusReason6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
	))

