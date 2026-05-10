from . import base_types
from ._ContactIdentification2 import ContactIdentification2
from ._NameAndAddress4 import NameAndAddress4
from ._YesNoIndicator import YesNoIndicator

class DeliveryParameters4(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_NmAndAdr", "_RegdAdrInd"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != base_types.auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def RegdAdrInd(self):
		return self._RegdAdrInd

	@RegdAdrInd.setter
	def RegdAdrInd(self, value):
		self._RegdAdrInd = value if type(value) != base_types.auto else self.make_default("RegdAdrInd")

	@RegdAdrInd.deleter
	def RegdAdrInd(self):
		del self._RegdAdrInd
		self._RegdAdrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdAdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

