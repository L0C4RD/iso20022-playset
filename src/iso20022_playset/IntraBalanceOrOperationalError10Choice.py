from . import base_types
from .ErrorHandling5 import ErrorHandling5
from .IntraBalanceCancellation7 import IntraBalanceCancellation7

class IntraBalanceOrOperationalError10Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_Cxls"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def Cxls(self):
		return self._Cxls

	@Cxls.setter
	def Cxls(self, value):
		self._Cxls = value if type(value) != base_types.auto else self.make_default("Cxls")

	@Cxls.deleter
	def Cxls(self):
		del self._Cxls
		self._Cxls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Cxls', type=IntraBalanceCancellation7, min=1, max=None, mutex_group=1, array=True),
	))

