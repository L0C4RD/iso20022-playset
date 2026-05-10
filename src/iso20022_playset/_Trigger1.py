from . import base_types
from ._FixedOrRecurrentDate1Choice import FixedOrRecurrentDate1Choice
from ._Document10 import Document10

class Trigger1(base_types._BaseFieldType):

	__slots__ = ["_DcmntryEvt", "_DtChc"]
	@property
	def DcmntryEvt(self):
		return self._DcmntryEvt

	@DcmntryEvt.setter
	def DcmntryEvt(self, value):
		self._DcmntryEvt = value if type(value) != base_types.auto else self.make_default("DcmntryEvt")

	@DcmntryEvt.deleter
	def DcmntryEvt(self):
		del self._DcmntryEvt
		self._DcmntryEvt = None

	@property
	def DtChc(self):
		return self._DtChc

	@DtChc.setter
	def DtChc(self, value):
		self._DtChc = value if type(value) != base_types.auto else self.make_default("DtChc")

	@DtChc.deleter
	def DtChc(self):
		del self._DtChc
		self._DtChc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DcmntryEvt', type=Document10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtChc', type=FixedOrRecurrentDate1Choice, min=0, max=1, mutex_group=None, array=False),
	))

