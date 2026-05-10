from . import base_types
from ._ReturnMemberV05 import ReturnMemberV05

class CAMT_014_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrMmb"]
		@property
		def RtrMmb(self):
			return self._RtrMmb

		@RtrMmb.setter
		def RtrMmb(self, value):
			self._RtrMmb = value if type(value) != base_types.auto else self.make_default("RtrMmb")

		@RtrMmb.deleter
		def RtrMmb(self):
			del self._RtrMmb
			self._RtrMmb = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrMmb', type=ReturnMemberV05, min=1, max=1, mutex_group=None, array=False),
		))

