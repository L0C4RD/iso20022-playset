from . import base_types
from .DeliveringPartiesAndAccount22 import DeliveringPartiesAndAccount22
from .ReceivingPartiesAndAccount22 import ReceivingPartiesAndAccount22

class SettlementParties38Choice(base_types._BaseFieldType):

	__slots__ = ["_DlvrgSttlmPties", "_RcvgSttlmPties"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgSttlmPties', type=DeliveringPartiesAndAccount22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=ReceivingPartiesAndAccount22, min=0, max=1, mutex_group=1, array=False),
	))

