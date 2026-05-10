from . import base_types
from .ReceivingPartiesAndAccount19 import ReceivingPartiesAndAccount19
from .DeliveringPartiesAndAccount19 import DeliveringPartiesAndAccount19

class SettlementParties36Choice(base_types._BaseFieldType):

	__slots__ = ["_RcvgSttlmPties", "_DlvrgSttlmPties"]
	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != base_types.auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvgSttlmPties', type=ReceivingPartiesAndAccount19, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=DeliveringPartiesAndAccount19, min=0, max=1, mutex_group=1, array=False),
	))

