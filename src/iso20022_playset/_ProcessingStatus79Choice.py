from . import base_types
from ._RejectionOrRepairStatus31Choice import RejectionOrRepairStatus31Choice
from ._AcknowledgedAcceptedStatus33Choice import AcknowledgedAcceptedStatus33Choice

class ProcessingStatus79Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Rjctd"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != base_types.auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus33Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionOrRepairStatus31Choice, min=0, max=1, mutex_group=1, array=False),
	))

