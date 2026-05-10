from . import base_types
from .InvestigationRejection1Code import InvestigationRejection1Code

class InvestigationRejectionJustification1(base_types._BaseFieldType):

	__slots__ = ["_RjctnRsn"]
	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnRsn', type=InvestigationRejection1Code, min=1, max=1, mutex_group=None, array=False),
	))

